import logging
import textwrap
import traceback
from enum import IntFlag, auto
from pathlib import Path
from typing import Optional

from functions import ensure_spoken, ensure_value_completed, ensure_command_executed
from functions.check_signiture_in_loop import check_signiture_in_loop
from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
from functions.ensure_env_var_completed import ensure_env_var_completed
from functions.ensure_env_var_completed_advanced import ensure_env_var_completed_advanced
from functions.ensure_value_completed_advanced import ensure_value_completed_advanced
from functions.get_caller_n import get_caller_n
from functions.get_easy_speakable_text import get_easy_speakable_text
from functions.get_env_var_name_id import get_env_var_id
from functions.get_text_cyan import get_text_cyan
from functions.get_text_yellow import get_text_yellow
from functions.is_internet_connected import is_internet_connected
from functions.is_os_windows import is_os_windows
from objects.device_identifiers import PkDevice, PkDeviceIdentifiers
from objects.pk_local_test_activate import LTA
from objects.pk_map_texts import PkTexts
from objects.task_orchestrator_cli_files import F_WSL_SSHD_CONFIG
from objects.pk_target import PkTarget
from objects.pk_ttl_cache_manager import ensure_function_return_ttl_cached
from objects.pk_ubuntu_package_name import UbuntuPakageName
from task_orchestrator_cli_sensitive.task_orchestrator_cli_sensitive_pnxs import F_LOCAL_SSH_PUBLIC_KEY, F_LOCAL_SSH_PRIVATE_KEY


class SetupOps(IntFlag):
    NONE = 0
    SELF = auto()
    TARGET = auto()
    WSL = auto()
    ALL = SELF | TARGET | WSL


class PkTargetManager(PkDevice):
    """
        programmer : programmer device is working for flashing target device
        target : target device flashed
    """
    _wsl: PkTarget = None
    target: PkTarget = None

    from functions.ensure_seconds_measured import ensure_seconds_measured

    def __init__(self, identifier: "PkDeviceIdentifiers", ip=None, pw=None, hostname=None, port=None, user_n=None, f_local_ssh_public_key=None, f_local_ssh_private_key=None, nick_name=None, setup_ops: "SetupOps" = SetupOps.ALL):
        super().__init__(identifier)

        connected = is_internet_connected()
        if not connected:
            ensure_spoken("network is not connected")
            return

        # self.set_self(ip=ip, pw=pw, hostname=hostname, port=port, user_n=user_n, f_local_ssh_public_key=f_local_ssh_public_key, f_local_ssh_private_key=f_local_ssh_private_key, nick_name=nick_name)
        # self.set_target()
        # self.set_wsl()

        # 저장해두면 이후 메서드에서 기본값처럼 재사용 가능
        self._setup_ops_default = setup_ops
        self._init_kwargs = dict(ip=ip, pw=pw, hostname=hostname, port=port, user_n=user_n, f_local_ssh_public_key=f_local_ssh_public_key, f_local_ssh_private_key=f_local_ssh_private_key, nick_name=nick_name)
        # 필요한 단계만 실행
        self._setup_successful = False  # Initialize setup status
        self._run_setups(setup_ops, **self._init_kwargs)
        if self._wsl is not None:  # Check if WSL was successfully set up
            self._setup_successful = True

        logging.debug(f'{get_caller_n()} is initialized')

    def _run_setups(self, setup_ops: "SetupOps", *, ip=None, pw=None, hostname=None, port=None, user_n=None, f_local_ssh_public_key=None, f_local_ssh_private_key=None, nick_name=None) -> None:
        import logging
        from objects.device_identifiers import PkDeviceIdentifiers

        if setup_ops & SetupOps.SELF:
            self.set_self(
                ip=ip, pw=pw, hostname=hostname, port=port, user_n=user_n,
                f_local_ssh_public_key=f_local_ssh_public_key,
                f_local_ssh_private_key=f_local_ssh_private_key,
                nick_name=nick_name,
            )
            logging.debug("set_self() done")

        if setup_ops & SetupOps.TARGET:
            # 기존 로직: identifier가 기본 WSL이면 target 설정 생략
            if not self.identifier == PkDeviceIdentifiers.undefined:
                self.set_target()
                logging.debug("set_target() done")
            else:
                logging.debug("set_target() skipped for wsl_distro_default")

        if setup_ops & SetupOps.WSL:
            self.setup_wsl()
            logging.debug("setup_wsl() done")
            if self._wsl is None:
                logging.error("WSL setup failed. Cannot proceed with WSL-dependent operations.")
                return  # Exit _run_setups if WSL setup failed
            self.wsl = self._wsl  # Assign the internal _wsl to the public wsl attribute

    def set_self(self, ip=None, pw=None, hostname=None, port=None, user_n=None, f_local_ssh_public_key=None, f_local_ssh_private_key=None, nick_name=None):
        self.ip = ip
        self.pw = pw
        self.hostname = hostname
        self.port = port
        self.user_n = user_n
        self.f_local_ssh_public_key = f_local_ssh_public_key
        self.f_local_ssh_private_key = f_local_ssh_private_key
        self.nick_name = nick_name

    @ensure_seconds_measured
    def ensure_usbipd_enabled(self):
        if not self.get_uspipd_version():
            self.ensure_usbipd_installed()

        if not self.is_usbipd_enabled():
            self.ensure_usbipd_installed()

        if not self.get_uspipd_version() and not self.is_usbipd_enabled():
            logging.info("usbipd 가 활성화 되어 있지 않습니다")
            return False

        logging.debug("usbipd가 이미 설치 및 활성화되어 있습니다.")
        return True

    def is_wsl_installed(self):
        import logging
        import subprocess
        try:
            subprocess.run(["wsl", "--status"], check=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
            logging.debug("WSL is installed and accessible.")
            return True
        except FileNotFoundError:
            logging.debug("wsl.exe not found. WSL is not installed or not in PATH.")
            return False
        except subprocess.CalledProcessError as e:
            logging.debug(f"WSL command failed: {e.stderr}. WSL might be installed but not functioning correctly.")
            return False
        except Exception as e:
            logging.error(f"An unexpected error occurred while checking WSL installation: {e}")
            return False

    def get_wsl_distro_name_default(self):
        from functions.ensure_env_var_completed import ensure_env_var_completed

        # pk_*
        # 명시적 초기화, ⚠️ 수동 초기화
        # env_var_name = "selected"
        # selected = ensure_value_completed_advanced(env_var_name=env_var_name, prompt_message=f"{env_var_name}=", options=get_wsl_distro_names_installed())

        # pk_*
        # 자동 초기화, ⚠️ 환경변수 selected 를 수정하기 위해서는 selected 수동 수정 필요
        env_var_name = "wsl_distro_name_default"
        selected = ensure_env_var_completed(env_var_name=env_var_name, prompt_message=f"{env_var_name}=", options=self.get_wsl_distro_names_installed())
        wsl_distro_name_default = selected
        return wsl_distro_name_default

    def get_wsl_distro_names_installed(self):
        import logging
        import subprocess
        try:
            result = subprocess.run(["wsl", "--list", "--quiet"], capture_output=True, text=True, encoding='utf-8', errors='ignore')
            if result.returncode != 0:
                logging.error(f"Failed to list WSL distros: {result.stderr}")
                return []
            output = result.stdout.replace('\x00', '').strip()
            return [line.strip() for line in output.splitlines() if line.strip()]
        except FileNotFoundError:
            logging.error("wsl.exe not found. WSL is not installed or not in PATH.")
            return []
        except Exception as e:
            logging.error(f"An unexpected error occurred while getting WSL distro names: {e}")
            return []

    def get_wsl_distro_hostname(self, distro_name):
        import logging
        import subprocess
        try:
            cmd = ["wsl", "-d", distro_name, "--", "hostname"]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, encoding='utf-8', errors='ignore')
            hostname = result.stdout.strip()
            return hostname
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to get hostname for {distro_name}: {e.stderr}")
            return None
        except FileNotFoundError:
            logging.error("wsl.exe not found. Is WSL installed and in your PATH?")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred while getting WSL distro hostname: {e}")
            return None

    def get_wsl_distro_ip(self, distro_name):
        import logging
        import subprocess
        import re
        try:
            cmd = ["wsl", "-d", distro_name, "--", "ip", "addr", "show", "eth0"]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, encoding='utf-8', errors='ignore')
            output = result.stdout
            ip_match = re.search(r'inet (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', output)
            if ip_match:
                return ip_match.group(1)
            else:
                logging.warning(f"Could not find IP address for {distro_name}.")
                return None
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to get IP address for {distro_name}: {e.stderr}")
            return None
        except FileNotFoundError:
            logging.error("wsl.exe not found. Is WSL installed and in your PATH?")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred while getting WSL distro IP: {e}")
            return None

    def get_wsl_distro_port(self, distro_name: str) -> Optional[str]:
        """
        WSL 배포판의 sshd_config 파일에서 SSH 포트 번호를 추출합니다.
        파일이 없으면 openssh-server 설치를 시도하고, 포트가 주석처리된 경우 주석을 해제합니다.
        """
        import subprocess
        from sources.objects.pk_local_test_activate import LTA

        # 1. Ensure the config file exists and get its path
        f_ssh_config = self.ensure_wsl_sshd_config_created(distro_name=distro_name)
        if not f_ssh_config:
            logging.error(f"[{distro_name}] sshd_config 파일을 확보하는데 최종 실패했습니다.")
            return None

        # 2. Read the file content from WSL
        try:
            logging.debug(f"sshd_config 파일 내용을 WSL에서 읽습니다: {f_ssh_config}")
            cmd = ["wsl", "-d", distro_name, "--", "cat", str(f_ssh_config)]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True, encoding='utf-8', errors='ignore')
            config_content = result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"WSL에서 sshd_config 파일 읽기 실패: {e.stderr}")
            return None
        except FileNotFoundError:
            logging.error("wsl.exe not found. Is WSL installed and in your PATH?")
            return None
        except Exception as e:
            logging.error(f"sshd_config 파일 읽기 중 예상치 못한 오류 발생: {e}")
            return None

        # 3. Auto-fix logic: Uncomment the default port if no other port is active
        PORT_SIGNATURE_COMMENTED = "#Port 22"
        PORT_TO_SET = "Port 22"

        has_commented_port = PORT_SIGNATURE_COMMENTED in config_content
        has_active_port = any(line.strip().startswith("Port") and not line.strip().startswith("#") for line in config_content.splitlines())

        if has_commented_port and not has_active_port:
            logging.warning(f"[{distro_name}] 활성 포트 없이 기본 포트가 주석 처리되어 있습니다. 자동 수정을 시도합니다.")
            try:
                new_content = config_content.replace(PORT_SIGNATURE_COMMENTED, PORT_TO_SET, 1)
                f_ssh_config.write_text(new_content, encoding='utf-8')
                logging.info(f"sshd_config 파일을 수정했습니다. '{PORT_SIGNATURE_COMMENTED}' -> '{PORT_TO_SET}'")
                return "22"  # We know the port is 22 now
            except Exception as e:
                logging.error(f"sshd_config 파일 수정 중 오류 발생: {e}. 권한 문제일 수 있습니다.")
                # Fall through to parsing, which will likely return None.

        # 4. Parse the content to find the active port
        stdout_lines = config_content.splitlines()
        PORT_PREFIX = "Port"
        port_wsl = None

        for line in stdout_lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            if line.startswith(PORT_PREFIX):
                try:
                    port_wsl = line.replace(PORT_PREFIX, "").strip().split()[0]
                    if port_wsl.isdigit():
                        logging.debug(f"추출된 WSL SSH 포트: {port_wsl} {'%%%FOO%%%' if LTA else ''}")
                        return port_wsl
                    else:
                        logging.warning(f"추출된 포트 값 '{port_wsl}'이 유효한 숫자가 아닙니다.")
                        port_wsl = None
                except Exception as e:
                    logging.error(f"포트 추출 중 오류 발생: {e}")
                    port_wsl = None

        if port_wsl is None:
            logging.debug("sshd_config 파일에서 활성화된 유효한 SSH 포트 설정을 찾을 수 없습니다.")

        return port_wsl

    def get_wsl_distro_pw(self, distro_name):
        import logging
        func_n = get_caller_n()
        try:
            key_name = f'wsl_pw_of_{distro_name}'
            selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n)
            wsl_pw_of_distro_name = selected
            return wsl_pw_of_distro_name
        except Exception as e:
            logging.error(f"An unexpected error occurred while getting WSL distro password: {e}")
            return None

    def ensure_wsl_distro_executed_with_persistent_session(self, distro_name):
        import logging
        import re
        import subprocess

        from sources.functions.ensure_command_executed import ensure_command_executed
        try:
            cmd = rf'wsl -l -v'
            stdout_list, _ = ensure_command_executed(cmd=cmd, encoding='utf-16-le')

            logging.debug(f"WSL 배포판 목록 파싱 시작")
            lines = [line.strip() for line in stdout_list if line.strip() and not line.strip().startswith("NAME")]
            for line in lines:
                match = re.match(r"^\*?\s*(?P<name>[^\s]+)\s+(?P<state>[^\s]+)\s+(?P<version>\d+)$", line)
                if match:
                    name = match.group("name")
                    state = match.group("state")
                    if name == distro_name and state == "Running":
                        logging.info(f"WSL 배포판 '{name}'이(가) 설치되어 있고 실행 중입니다.")
                        return True
                    elif name == distro_name and state == "Stopped":
                        logging.info(f"WSL 배포판 '{name}'이(가) 설치되어 있지만 중지 상태입니다. 시작을 시도합니다.")
                        try:
                            # keep wsl session at background for next wsl starting without_cold_start
                            subprocess.Popen(["wsl", "-d", distro_name, "--exec", "sleep", "infinity"])
                            logging.info(f"WSL 배포판 '{name}' 시작 성공.")
                            return True
                        except:
                            ensure_debug_loged_verbose(traceback)
                            return False
                else:
                    logging.debug(f"WSL 배포판 라인 파싱 실패: '{line}'")

            logging.info(f"❌ WSL 배포판 '{distro_name}'이(가) 설치되어 있지 않거나 실행 중이 아닙니다.")
            return False




        except FileNotFoundError:
            logging.error("wsl.exe not found. Is WSL installed and in your PATH?")
            return False
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to ensure persistent session for {distro_name}: {e.stderr}")
            return False
        except Exception as e:
            logging.error(f"An unexpected error occurred while ensuring WSL persistent session: {e}")
            return False

    def ensure_wsl_sshd_config_created(self, distro_name):
        import logging
        import subprocess
        import textwrap
        try:
            check_cmd = ["wsl", "-d", distro_name, "--", "test", "-f", str(F_WSL_SSHD_CONFIG)]
            result = subprocess.run(check_cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore')
            if result.returncode == 0:
                logging.debug(f"sshd_config already exists in {distro_name}.")
                return F_WSL_SSHD_CONFIG
            sshd_config_content = textwrap.dedent("""
            Port 22
            ListenAddress 0.0.0.0
            ListenAddress ::
            PermitRootLogin yes
            PasswordAuthentication yes
            ChallengeResponseAuthentication no
            UsePAM yes
            X11Forwarding yes
            PrintMotd no
            AcceptEnv LANG LC_*
            Subsystem       sftp    /usr/lib/openssh/sftp-server
        """)
            temp_file_path = "/tmp/sshd_config_temp"
            # Use tee to write content, which is more robust for multi-line strings
            write_cmd = ["wsl", "-d", distro_name, "--", "tee", temp_file_path]
            subprocess.run(write_cmd, input=sshd_config_content.encode('utf-8'), check=True, capture_output=True)
            move_cmd = ["wsl", "-d", distro_name, "--", "sudo", "mv", temp_file_path, str(F_WSL_SSHD_CONFIG)]
            subprocess.run(move_cmd, check=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
            chmod_cmd = ["wsl", "-d", distro_name, "--", "sudo", "chmod", "644", str(F_WSL_SSHD_CONFIG)]
            subprocess.run(chmod_cmd, check=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
            logging.info(f"sshd_config created and configured in {distro_name}.")
            return F_WSL_SSHD_CONFIG
        except FileNotFoundError:
            logging.error("wsl.exe not found. Is WSL installed and in your PATH?")
            return False
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to create sshd_config for {distro_name}: {e.stderr}")
            return False
        except Exception as e:
            logging.error(f"An unexpected error occurred while creating sshd_config: {e}")
            return False

    def get_wsl_distro_config(self):
        wsl_distro_config = self.wsl.to_dict()
        return wsl_distro_config

    def get_wsl_distro_ssh_config_file_contents(self):
        """지정된 WSL 배포판의 SSH 설정 파일 내용을 가져옵니다."""
        import logging
        import subprocess

        distro_name = self.wsl.distro_name

        cmd = f"wsl -d {distro_name} -- cat {str(F_WSL_SSHD_CONFIG)}"
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True, check=True, encoding='utf-8', errors='ignore')
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to get SSH config from {distro_name}: {e.stderr}")
            return None
        except FileNotFoundError:
            logging.error("`wsl.exe` not found. Is WSL installed and in your PATH?")
            return None

    # def get_wsl_distros_data(self):
    #     import logging
    #     import re
    #
    #     func_n = get_caller_n()
    #
    #     """WSL 배포판의 상세 정보를 구조화된 데이터로 반환합니다."""
    #     distro_info_list = self.get_wsl_distro_info_std_list()
    #     if not distro_info_list or len(distro_info_list) < 2:
    #         logging.info("Could not retrieve WSL distro information.")
    #         return None
    #
    #     key_name = 'wsl_distro_name'
    #     options = self.get_wsl_distro_names_installed()
    #     selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n, options=options)
    #     wsl_distro_name = selected
    #
    #     key_name = f'distro_pw_of_{self.get_wsl_distro_names_installed()}'
    #     selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n)
    #     distro_pw_of_distro = selected
    #
    #     distros = distro_info_list[1:]
    #     data = {"distros": []}
    #     for line in distros:
    #         line = line.lstrip('*').strip()
    #         parts = re.split(r'\s+', line, 2)  # 공백 기준으로 최대 2번 분리
    #         if len(parts) >= 3:
    #             name = parts[0]
    #             state = parts[1]
    #             version = parts[2]
    #             data["distros"].append({
    #                 "name": name,
    #                 "state": state,
    #                 "version": version,
    #             })
    #     return data

    def get_wsl_version(self):
        import logging
        import subprocess

        wsl_version = None
        try:
            result = subprocess.run(
                ["wsl", "--version"],
                capture_output=True,
                text=True,
                check=True,
                encoding='utf-8',
                errors='ignore'
            )

            output = result.stdout

            for line in output.splitlines():
                if line.strip().startswith("WSL 버전:") or line.strip().startswith("WSL version:"):
                    wsl_version = line.split(':')[-1].strip()
                    break

            if not wsl_version:
                logging.warning("Could not parse WSL version from 'wsl --version'.")

        except FileNotFoundError:
            logging.error("`wsl.exe` not found. Is WSL installed and in your PATH?")
            wsl_version = "Not Installed"
        except subprocess.CalledProcessError as e:
            logging.warning(f"'wsl --version' failed, possibly an older WSL. Error: {e.stderr}")
            wsl_version = "Unknown (command failed)"

        logging.debug(f"wsl_version={wsl_version}")
        return wsl_version

    def get_wsl_distro_info_std_list(self) -> list[str]:
        import logging
        import subprocess

        try:
            if not self.is_wsl_installed():
                ensure_spoken("wsl is not installed")
                return []

            result = subprocess.run(['wsl', '-l', '-v'], capture_output=True, text=True, encoding='utf-8', errors='ignore')

            if result.returncode != 0:
                logging.debug(f"WSL command failed with return code: {result.returncode}")
                if result.stderr:
                    logging.debug(f"WSL error: {result.stderr}")
                return []

            output = result.stdout
            if not output.strip():
                logging.debug("WSL command returned empty output")
                return []

            cleaned_output = output.replace('\x00', '').strip()
            std_list = [line.strip() for line in cleaned_output.splitlines() if line.strip()]

            if LTA:
                logging.debug(f"WSL output lines: {len(std_list)}")
                for i, line in enumerate(std_list):
                    logging.debug(f"Line {i}: '{line}'")

            return std_list

        except FileNotFoundError:
            logging.debug("WSL command not found")
            return []
        except:
            ensure_debug_loged_verbose(traceback)
            return []

    def get_wsl_distro_names(self, distro_name) -> list[str]:
        import subprocess

        try:
            if not self.is_wsl_distro_installed(distro_name): return []
            result = subprocess.run(['wsl', '--list', '--quiet'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
            if result.returncode != 0: return []

            output = result.stdout.replace('\x00', '').strip()
            return [line.strip() for line in output.splitlines() if line.strip()]
        except:
            ensure_debug_loged_verbose(traceback)
            return []

    def ensure_wsl_distro_executed(self, distro_name) -> bool:
        import logging
        import subprocess
        # Removed re and ensure_command_executed imports as they are now in _get_wsl_distro_status

        status = self._get_wsl_distro_status(distro_name)

        if status == "Running":
            logging.info(f"WSL 배포판 '{distro_name}'이(가) 설치되어 있고 실행 중입니다.")
            return True
        elif status == "Stopped":
            logging.info(f"WSL 배포판 '{distro_name}'이(가) 설치되어 있지만 중지 상태입니다. 시작을 시도합니다.")
            try:
                subprocess.run(["wsl", "-d", distro_name, "--exec", "true"], check=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
                logging.info(f"WSL 배포판 '{distro_name}' 시작 성공.")
                return True
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to start WSL distro '{distro_name}': {e.stderr}")
                return False
            except FileNotFoundError:
                logging.error("wsl.exe not found. Is WSL installed and in your PATH?")
                return False
            except Exception as e:
                logging.error(f"An unexpected error occurred while starting WSL distro '{distro_name}': {e}")
                return False
        else:  # status is None (not found or error)
            logging.info(f"❌ WSL 배포판 '{distro_name}'이(가) 설치되어 있지 않거나 실행 중이 아닙니다.")
            return False

    def is_wsl_distro_installed(self, distro_name):
        import logging
        from sources.functions.get_enabled_wsl_distros import get_enabled_wsl_distros

        enabled_distros = get_enabled_wsl_distros()
        for distro in enabled_distros:
            if distro['name'].strip().lower() == distro_name.strip().lower():
                logging.debug(f'"{distro_name} is installed"')
                return True
        logging.debug(f'"{distro_name} is not installed"')
        return False

    def _get_wsl_distro_status(self, distro_name) -> Optional[str]:
        import logging
        import re
        from sources.functions.ensure_command_executed import ensure_command_executed

        try:
            cmd = rf'wsl -l -v'
            stdout_list, _ = ensure_command_executed(cmd=cmd, encoding='utf-16-le')

            logging.debug(f"WSL 배포판 목록 파싱 시작")
            lines = [line.strip() for line in stdout_list if line.strip() and not line.strip().startswith("NAME")]
            for line in lines:
                match = re.match(r"^\*?\s*(?P<name>[^\s]+)\s+(?P<state>[^\s]+)\s+(?P<version>\d+)$", line)
                if match:
                    name = match.group("name")
                    state = match.group("state")
                    if name == distro_name:
                        logging.debug(f"Found WSL distro '{distro_name}' with state '{state}'.")
                        return state
                else:
                    logging.debug(f"WSL 배포판 라인 파싱 실패: '{line}'")
            logging.debug(f"WSL distro '{distro_name}' not found in list.")
            return None  # Distro not found
        except FileNotFoundError:
            logging.error("wsl.exe not found. Is WSL installed and in your PATH?")
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred while getting WSL distro status: {e}")
            return None

    def _start_wsl_distro(self, distro_name, persistent: bool = False) -> bool:
        import logging
        import subprocess
        try:
            if persistent:
                logging.info(f"WSL distro '{distro_name}' is stopped. Attempting to start persistently.")
                subprocess.Popen(["wsl", "-d", distro_name, "--exec", "sleep", "infinity"])
            else:
                logging.info(f"WSL 배포판 '{distro_name}'이(가) 중지 상태입니다. 시작을 시도합니다.")
                subprocess.run(["wsl", "-d", distro_name, "--exec", "true"], check=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')

            logging.info(f"WSL distro '{distro_name}' started successfully.")
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to start WSL distro '{distro_name}': {e.stderr}")
            return False
        except FileNotFoundError:
            logging.error("wsl.exe not found. Is WSL installed and in your PATH?")
            return False
        except Exception as e:
            logging.error(f"An unexpected error occurred while starting WSL distro '{distro_name}': {e}")
            return False

    def getERROR(self) -> PkTarget:
        return self._wsl

    def setup_wsl(self):
        func_n = get_caller_n()

        installed = self.is_wsl_installed()
        if not installed:
            ensure_spoken("this process need wsl, but not installed")
            return

        key_name = 'wsl_distro_name'
        options = self.get_wsl_distro_names_installed()
        selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n, options=options)
        wsl_distro_name = selected

        sessions_enabled = self.ensure_wsl_distro_executed_with_persistent_session(distro_name=wsl_distro_name)
        if not sessions_enabled:
            ensure_spoken("wsl persistaent sessions is not enabled")
            return

        f_ssh_config = self.ensure_wsl_sshd_config_created(distro_name=wsl_distro_name)
        if LTA:
            wsl = PkTarget(
                identifier=wsl_distro_name,
                user_n="pk",
                f_local_ssh_public_key=F_LOCAL_SSH_PUBLIC_KEY,
                f_local_ssh_private_key=F_LOCAL_SSH_PRIVATE_KEY,
                nick_name="wsl_distro_nick_name",
                distro_name=wsl_distro_name,
                hostname=self.get_wsl_distro_hostname(wsl_distro_name),
                ip=self.get_wsl_distro_ip(distro_name=wsl_distro_name),
                pw=self.get_wsl_distro_pw(distro_name=wsl_distro_name),
                port=self.get_wsl_distro_port(distro_name=wsl_distro_name),
            )
            self._wsl = wsl
            return

        key_name = 'wsl_distro_user_n'
        selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n)
        wsl_distro_user_n = selected

        key_name = 'wsl_distro_f_local_ssh_public_key'
        selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n)
        wsl_distro_f_local_ssh_public_key = selected

        key_name = 'wsl_distro_f_local_ssh_private_key'
        selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n)
        wsl_distro_f_local_ssh_private_key = selected

        key_name = 'wsl_distro_nick_name'
        selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n)
        wsl_distro_nick_name = selected

        wsl = PkTarget(
            identifier=wsl_distro_user_n,
            user_n=wsl_distro_user_n,
            f_local_ssh_public_key=wsl_distro_f_local_ssh_public_key,
            f_local_ssh_private_key=wsl_distro_f_local_ssh_private_key,
            nick_name=wsl_distro_nick_name,
            distro_name=wsl_distro_name,
            hostname=self.get_wsl_distro_hostname(wsl_distro_name),
            ip=self.get_wsl_distro_ip(wsl_distro_name),
            pw=self.get_wsl_distro_pw(wsl_distro_name),
            port=self.get_wsl_distro_port(wsl_distro_name),
        )
        self._wsl = wsl

    def get_wsl_distros_data(self):
        import logging
        import re

        """WSL 배포판의 상세 정보를 구조화된 데이터로 반환합니다."""
        distro_info_list = self.get_wsl_distro_info_std_list()
        if not distro_info_list or len(distro_info_list) < 2:
            logging.info("Could not retrieve WSL distro information.")
            return None

        distros = distro_info_list[1:]
        data = {"distros": []}
        for line in distros:
            line = line.lstrip('*').strip()
            parts = re.split(r'\s+', line, 2)
            if len(parts) >= 3:
                name = parts[0]
                state = parts[1]
                version = parts[2]
                data["distros"].append({
                    "name": name,
                    "state": state,
                    "version": version,
                })
        return data

    def get_installed_distro_names(self) -> list[str]:
        import subprocess
        try:
            result = subprocess.run(['wsl', '--list', '--quiet'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
            if result.returncode != 0:
                return []
            output = result.stdout.replace('\x00', '').strip()
            return [line.strip() for line in output.splitlines() if line.strip()]
        except:
            logging.error("Failed to get installed WSL distro names.")
            return []

    def get_distro_names(self, distro_name) -> list[str]:
        import subprocess

        try:
            if not self.is_wsl_distro_installed(distro_name): return []
            result = subprocess.run(['wsl', '--list', '--quiet'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
            if result.returncode != 0: return []

            output = result.stdout.replace('\x00', '').strip()
            return [line.strip() for line in output.splitlines() if line.strip()]
        except:
            ensure_debug_loged_verbose(traceback)
            return []

    @ensure_seconds_measured
    def ensure_usb_bridge_between_windows_and_wsl_established(self):
        import logging

        # wsl distro lsusb 설치
        if self.ensure_wsl_distro_ubuntu_pkg_installed(UbuntuPakageName.usbutils):
            # wsl_distro_ssh_config = self.get_wsl_distro_ssh_config_file_contents()
            self.ensure_command_to_target(cmd='sudo apt install -y usbutils')

        # windows usbipd 설치
        self.ensure_usbipd_enabled()


        # target 리커버리 모드진입
        if not self.ensure_target_recovery_mode_entered():
            logging.warning('device target should be entered to recovery mode for flash jetpack')
            return False

    from sources.functions.ensure_seconds_measured import ensure_seconds_measured

    @ensure_seconds_measured
    def ensure_wsl_distros_enabled(self):
        import logging
        from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
        import traceback
        from sources.functions.get_enabled_wsl_distros import get_enabled_wsl_distros
        try:
            for distro_name in get_enabled_wsl_distros():
                if self.ensure_wsl_distro_executed_with_persistent_session(distro_name):
                    wsl_distros = get_enabled_wsl_distros()
                    if wsl_distros:
                        logging.debug("[ WSL 배포판 목록 ]")
                        for i, distro in enumerate(wsl_distros):
                            logging.debug(f"{i + 1}. {distro.get('name', '')} ({distro.get('state', 'Unknown')}, v{distro.get('version', '?')})")
                else:
                    logging.debug("Failed to start WSL distros with persistent sessions")
                    return False
            return True
        except:
            ensure_debug_loged_verbose(traceback)
        finally:
            pass

    def cmd_to_wsl_os_like_human_deprecated(self, cmd, distro_name, wsl_window_title_seg, exit_mode=False):
        import logging

        from functions import ensure_slept
        from functions.ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard import ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard
        from functions.open_and_move_wsl_console_to_front import open_and_move_wsl_console_to_front
        from sources.functions.ensure_pressed import ensure_pressed
        from sources.functions.ensure_window_to_front import ensure_window_to_front
        from sources.functions.is_window_opened import is_window_opened
        import time
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()

        timeout = 20
        start_time = time.time()
        while 1:
            if is_window_opened(window_title_seg=wsl_window_title_seg):
                break
            open_and_move_wsl_console_to_front(distro_name=distro_name, window_title_seg=wsl_window_title_seg)
            logging.debug(time.time() - start_time)
            if time.time() - start_time > timeout:
                break
            ensure_slept(seconds=0.5)

        std_output_stream = ""
        timeout = 5
        start_time = time.time()
        while 1:
            if ensure_window_to_front(wsl_window_title_seg):
                ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard(text=cmd, wsl_mode=True)
                ensure_pressed("enter")
                break
            ensure_window_to_front(wsl_window_title_seg)

            # 5초가 지났는지 확인
            logging.debug(time.time() - start_time)
            if time.time() - start_time > timeout:
                logging.debug("5 seconds passed. Exiting loop.")
                break
            ensure_slept(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

        if exit_mode == True:
            timeout = 5
            start_time = time.time()
            while 1:
                if ensure_window_to_front(wsl_window_title_seg):
                    ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard(text="exit", wsl_mode=True)
                    ensure_pressed("enter")
                    ensure_text_saved_to_clipboard_and_pasted_with_keeping_clipboard(text="exit", wsl_mode=True)
                    ensure_pressed("enter")
                    break
                else:
                    ensure_window_to_front(wsl_window_title_seg)
                logging.debug(time.time() - start_time)
                if time.time() - start_time > timeout:
                    logging.debug("5 seconds passed. Exiting loop.")
                    break
                ensure_slept(seconds=0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

        # return std_output_stream

    def ensure_wsl_distro_executed_like_human(self, window_title_seg):
        from functions.open_and_move_wsl_console_to_front import open_and_move_wsl_console_to_front
        from sources.functions.ensure_window_to_front import ensure_window_to_front
        from sources.functions.is_window_opened import is_window_opened

        if not is_window_opened(window_title_seg=window_title_seg):
            open_and_move_wsl_console_to_front(distro_name=self.wsl.distro_name, window_title_seg=window_title_seg)
        while 1:
            if ensure_window_to_front(window_title_seg):
                break
            ensure_window_to_front(window_title_seg)

    def ensure_command_to_wsl_distro_like_human(self, cmd, window_title_seg, sleep_time=500):
        from functions import ensure_slept
        from functions.ensure_writen_like_human import ensure_writen_like_human
        from sources.functions.ensure_pressed import ensure_pressed
        self.ensure_wsl_distro_executed_like_human(window_title_seg=window_title_seg)
        ensure_writen_like_human(cmd)
        ensure_slept(milliseconds=sleep_time)
        ensure_pressed('enter')

    def ensure_wsl_distro_ubuntu_pkg_installed(self, ubuntu_pkg_name: "UbuntuPakageName"):
        """WSL 배포판에 지정된 우분투 패키지를 설치합니다."""
        import logging
        import subprocess
        pkg_name = ubuntu_pkg_name.value

        distro_name = self.wsl.distro_name

        # 패키지 설치 여부 확인
        check_cmd = f"wsl -d {distro_name} -- dpkg -s {pkg_name}"
        try:
            result = subprocess.run(check_cmd.split(), capture_output=True, text=True, check=True, encoding='utf-8', errors='ignore')
            if "Status: install ok installed" in result.stdout:
                logging.info(f"Package '{pkg_name}' is already installed in {distro_name}.")
                return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass  # 패키지가 없거나 오류 발생 시 설치 진행

        logging.info(f"Package '{pkg_name}' not found in {distro_name}. Attempting to install...")

        # 패키지 목록 업데이트 및 설치
        update_cmd = f"wsl -d {distro_name} -- sudo apt-get update"
        install_cmd = f"wsl -d {distro_name} -- sudo apt-get install -y {pkg_name}"

        try:
            subprocess.run(update_cmd.split(), check=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
            logging.info("Package list updated successfully.")

            install_result = subprocess.run(install_cmd.split(), check=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')
            logging.info(f"Package '{pkg_name}' installed successfully in {distro_name}.")
            logging.debug(install_result.stdout)
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to install package '{pkg_name}' in {distro_name}.")
            logging.error(f"Command: {' '.join(e.cmd)}")
            logging.error(f"Stderr: {e.stderr}")
            logging.error(f"Stdout: {e.stdout}")
            return False
        except FileNotFoundError:
            logging.error("`wsl.exe` not found. Is WSL installed and in your PATH?")
            return False

    def ensure_wsl_enabled(self, distro_name):
        import logging

        wsl_distro_name_list = self.get_wsl_distro_names(distro_name)
        if not wsl_distro_name_list:
            logging.debug("No WSL distros found.")
            return False, {}

        wsl_cmd_map_dict = {"wsl state": ["wsl", "-l", "-v"]}
        std_list = self.get_wsl_distro_info_std_list()

        for idx, name in enumerate(wsl_distro_name_list):
            clean_name = name.replace('\x00', '').strip()
            if not clean_name: continue

            wsl_cmd_map_dict[f"wsl {idx}"] = ["wsl", "-d", clean_name]

        wsl_cmd_map_dict["wsl shutdown"] = ["wsl", "--shutdown"]
        return True, wsl_cmd_map_dict

    def ensure_wsl_distro_enabled(self, distro_name, f_local_ssh_public_key):
        from sources.functions.ensure_wsl_distro_install import ensure_wsl_distro_install

        import logging
        from sources.functions.is_os_windows import is_os_windows
        from sources.objects.pk_local_test_activate import LTA
        from sources.functions.ensure_command_executed import ensure_command_executed
        import base64

        if is_os_windows():
            if not self.is_wsl_distro_installed(distro_name=distro_name):
                ensure_wsl_distro_install(distro_name=distro_name)
                if not self.is_wsl_distro_installed(distro_name=distro_name):
                    logging.debug(rf"{distro_name} install  {'%%%FOO%%%' if LTA else ''}")
                    raise

            # Ensure openssh-server is installed
            logging.debug(f"Checking openssh-server installation status in {distro_name}...")
            check_ssh_install_cmd = f"wsl -d {distro_name} dpkg -s openssh-server"
            ssh_install_status_outs, ssh_install_status_errs = ensure_command_executed(check_ssh_install_cmd)

            if ssh_install_status_outs and "install ok installed" in " ".join(ssh_install_status_outs):
                logging.debug(f"openssh-server is already installed in {distro_name}. Skipping installation.")
            else:
                logging.debug(f"openssh-server not found or not fully installed. Installing in {distro_name}...")
                install_ssh_cmd = f"wsl -d {distro_name} sudo apt update && wsl -d {distro_name} sudo apt install -y openssh-server"
                install_ssh_outs, install_ssh_errs = ensure_command_executed(install_ssh_cmd)
                if install_ssh_errs:
                    logging.error(f"Failed to install openssh-server in {distro_name}: {install_ssh_errs}")
                    raise RuntimeError(f"Failed to install openssh-server in {distro_name}")
                logging.debug(f"openssh-server installation completed in {distro_name}.")

            # Add public key to authorized_keys
            logging.debug(f"Setting up authorized_keys for {distro_name}...")
            # Create .ssh directory and set permissions
            create_ssh_dir_cmd = f"wsl -d {distro_name} mkdir -p ~/.ssh"
            create_ssh_dir_outs, create_ssh_dir_errs = ensure_command_executed(create_ssh_dir_cmd)
            if create_ssh_dir_errs:
                logging.error(f"Failed to create ~/.ssh directory in {distro_name}: {create_ssh_dir_errs}")
                raise RuntimeError(f"Failed to create ~/.ssh directory in {distro_name}")

            chmod_ssh_dir_cmd = f"wsl -d {distro_name} chmod 700 ~/.ssh"
            chmod_ssh_dir_outs, chmod_ssh_dir_errs = ensure_command_executed(chmod_ssh_dir_cmd)
            if chmod_ssh_dir_errs:
                logging.error(f"Failed to set permissions on ~/.ssh directory in {distro_name}: {chmod_ssh_dir_errs}")
                raise RuntimeError(f"Failed to set permissions on ~/.ssh directory in {distro_name}")

            # Base64 encode the public key content
            encoded_public_key = base64.b64encode(str(f_local_ssh_public_key).encode('utf-8')).decode('utf-8')

            # Define a temporary file path in WSL
            temp_pub_key_file = "/tmp/temp_id_rsa.pub"

            # Write the base64 encoded key to a temp file, then decode it in WSL
            write_pub_key_cmd = f"wsl -d {distro_name} bash -c \"echo '{encoded_public_key}' | base64 -d > {temp_pub_key_file}\""

            write_pub_key_outs, write_pub_key_errs = ensure_command_executed(write_pub_key_cmd)
            if write_pub_key_errs:
                logging.error(f"Failed to write public key to temp file in {distro_name}: {write_pub_key_errs}")
                raise RuntimeError(f"Failed to write public key to temp file in {distro_name}")

            # Check if temp_pub_key_file exists before appending
            check_temp_file_cmd = f"wsl -d {distro_name} test -f {temp_pub_key_file}"
            check_temp_file_outs, check_temp_file_errs = ensure_command_executed(check_temp_file_cmd)
            if check_temp_file_errs:
                logging.error(f"Temporary public key file {temp_pub_key_file} does not exist or is inaccessible in {distro_name}: {check_temp_file_errs}")
                raise RuntimeError(f"Temporary public key file {temp_pub_key_file} not found in {distro_name}")

            append_pub_key_cmd = f"wsl -d {distro_name} bash -c \"cat {temp_pub_key_file} >> ~/.ssh/authorized_keys\""
            append_pub_key_outs, append_pub_key_errs = ensure_command_executed(append_pub_key_cmd)
            if append_pub_key_errs:
                logging.error(f"Failed to append public key to authorized_keys in {distro_name}: {append_pub_key_errs}")
                raise RuntimeError(f"Failed to append public key to authorized_keys in {distro_name}")

            # Set permissions on authorized_keys
            chmod_auth_keys_cmd = f"wsl -d {distro_name} chmod 600 ~/.ssh/authorized_keys"
            chmod_auth_keys_outs, chmod_auth_keys_errs = ensure_command_executed(chmod_auth_keys_cmd)
            if chmod_auth_keys_errs:
                logging.error(f"Failed to set permissions on authorized_keys in {distro_name}: {chmod_auth_keys_errs}")
                raise RuntimeError(f"Failed to set permissions on authorized_keys in {distro_name}")

            # Remove temporary public key file
            rm_temp_pub_key_cmd = f"wsl -d {distro_name} rm {temp_pub_key_file}"
            rm_temp_pub_key_outs, rm_temp_pub_key_errs = ensure_command_executed(rm_temp_pub_key_cmd)
            if rm_temp_pub_key_errs:
                logging.warning(f"Failed to remove temporary public key file in {distro_name}: {rm_temp_pub_key_errs}")
                # Not a critical error, just log warning

            logging.debug(f"authorized_keys setup completed for {distro_name}.")

            # Ensure SSH service is running and enabled
            logging.debug(f"Checking SSH service status in {distro_name}...")
            check_ssh_active_cmd = f"wsl -d {distro_name} sudo systemctl is-active ssh"
            ssh_active_outs, ssh_active_errs = ensure_command_executed(check_ssh_active_cmd)
            if not ssh_active_outs or "active" not in " ".join(ssh_active_outs):
                logging.debug(f"SSH service not active. Starting in {distro_name}...")
                start_ssh_cmd = f"wsl -d {distro_name} sudo systemctl start ssh"
                start_ssh_outs, start_ssh_errs = ensure_command_executed(start_ssh_cmd)
                if start_ssh_errs:
                    logging.error(f"Failed to start SSH service in {distro_name}: {start_ssh_errs}")
                    raise RuntimeError(f"Failed to start SSH service in {distro_name}")
                logging.debug(f"SSH service started in {distro_name}.")

            check_ssh_enabled_cmd = f"wsl -d {distro_name} sudo systemctl is-enabled ssh"
            ssh_enabled_outs, ssh_enabled_errs = ensure_command_executed(check_ssh_enabled_cmd)
            if not ssh_enabled_outs or "enabled" not in " ".join(ssh_enabled_outs):
                logging.debug(f"SSH service not enabled. Enabling in {distro_name}...")
                enable_ssh_cmd = f"wsl -d {distro_name} sudo systemctl enable ssh"
                enable_ssh_outs, enable_ssh_errs = ensure_command_executed(enable_ssh_cmd)
                if enable_ssh_errs:
                    logging.error(f"Failed to enable SSH service in {distro_name}: {enable_ssh_errs}")
                logging.debug(f"SSH service enabled in {distro_name}.")

            # Add check for sudo service ssh status
            logging.debug(f"Final check for SSH service status in {distro_name} using 'sudo service ssh status'...")
            check_service_status_cmd = f"wsl -d {distro_name} sudo service ssh status"
            service_status_outs, service_status_errs = ensure_command_executed(check_service_status_cmd)

            if service_status_outs:
                logging.debug(f"SSH service status output:")
                for line in service_status_outs:
                    logging.debug(f"{line}")
            if service_status_errs:
                logging.error(f"SSH service status error output:")
                for line in service_status_errs:
                    logging.error(f"  {line}")

            # Read and Log sshd_config
            logging.debug(f"Checking sshd_config in {distro_name}...")
            read_sshd_config_cmd = f"wsl -d {distro_name} sudo cat {str(F_WSL_SSHD_CONFIG)}"
            sshd_config_outs, sshd_config_errs = ensure_command_executed(read_sshd_config_cmd)

            if sshd_config_errs:
                logging.error(f"Error reading sshd_config in {distro_name}: {sshd_config_errs}")
            elif sshd_config_outs:
                logging.debug(f"sshd_config content:")
                port_found = False
                listen_address_found = False
                for line in sshd_config_outs:
                    logging.debug(f"{line}")
                    if line.strip().startswith("Port"):  # Check for Port
                        try:
                            port_value = int(line.strip().split()[1])
                            if port_value != 22:
                                logging.warning(f"sshd_config: Port is set to {port_value}, expected 22.")
                            port_found = True
                        except:
                            logging.warning(f"sshd_config: Could not parse Port line: {line}")
                    if line.strip().startswith("ListenAddress"):  # Check for ListenAddress
                        try:
                            address_value = line.strip().split()[1]
                            if address_value not in ["0.0.0.0", "::"]:
                                logging.warning(f"sshd_config: ListenAddress is set to {address_value}, expected 0.0.0.0 or ::.")
                            listen_address_found = True
                        except:
                            logging.warning(f"sshd_config: Could not parse ListenAddress line: {line}")
                if not port_found:
                    logging.warning("sshd_config: Port directive not found. Defaulting to 22.")
                if not listen_address_found:
                    logging.warning("sshd_config: ListenAddress directive not found. Defaulting to all interfaces.")

            # Read and Log ufw status
            logging.debug(f"Checking ufw status in {distro_name}...")
            ufw_status_cmd = f"wsl -d {distro_name} sudo ufw status"
            ufw_status_outs, ufw_status_errs = ensure_command_executed(ufw_status_cmd)

            if ufw_status_errs:
                logging.error(f"Error checking ufw status in {distro_name}: {ufw_status_errs}")
            elif ufw_status_outs:
                logging.debug(f"ufw status output:")
                ufw_active = False
                port_22_allowed = False
                for line in ufw_status_outs:
                    logging.debug(f"{line}")
                    if "Status: active" in line:
                        ufw_active = True
                    if "22/tcp" in line and ("ALLOW" in line or "ALLOW IN" in line):
                        port_22_allowed = True

                if ufw_active and not port_22_allowed:
                    logging.warning(f"ufw is active in {distro_name} and port 22/tcp is not explicitly allowed. This might block SSH.")
                elif ufw_active and port_22_allowed:
                    logging.debug(f"ufw is active and port 22/tcp is allowed in {distro_name}.")
                elif not ufw_active:
                    logging.debug(f"ufw is inactive in {distro_name}.")
        return True

    def ensure_target_distro_pkg_installed(self, distro_pkg_n):
        import logging
        from sources.functions.check_signiture_in_loop import check_signiture_in_loop
        from sources.functions.ensure_general_ubuntu_pkg import ensure_general_ubuntu_pkg
        from sources.functions.is_internet_connected import is_internet_connected
        from sources.functions.todo import todo
        from sources.objects.pk_local_test_activate import LTA

        if not is_internet_connected():
            logging.debug(f'''can not install ubuntu pakage ({distro_pkg_n}) for internet not connected  {'%%%FOO%%%' if LTA else ''}''')
            raise
        if distro_pkg_n == 'docker':
            std_outs, std_err_list = self.ensure_command_to_target_with_pubkey(cmd='docker --version')
            if std_outs is None:  # Added check for None
                logging.error(f"Failed to get docker version from remote OS. SSH connection might be down.")
                return False  # Indicate failure
            if check_signiture_in_loop(time_limit=10, working_list=std_outs,
                                       signiture="The cmd 'docker' could not be found in this WSL 2 distro.",
                                       signiture_found_ment="docker is not installed in wsl"):
                self.ensure_target_distro_docker_installed()
        elif distro_pkg_n == 'net-tools':
            todo('%%%FOO%%%')
        else:
            # std_outs, std_err_list = ensure_command_to_remote_os_with_pubkey(cmd=f'{ubuntu_pkg_n} --version')
            std_outs, std_err_list = self.ensure_command_to_target_with_pubkey(
                cmd=f'sudo apt list --installed | grep {distro_pkg_n}')
            if std_outs is None:  # Added check for None
                logging.error(f"Failed to list installed packages for {distro_pkg_n} from remote OS. SSH connection might be down.")
                return False  # Indicate failure
            signiture = 'installed'
            if check_signiture_in_loop(time_limit=10, working_list=std_outs, signiture=signiture,
                                       signiture_found_ment=f"{distro_pkg_n} is installed in {self.target.distro_name}"):
                ensure_general_ubuntu_pkg(ubuntu_pkg_n=distro_pkg_n)
        return True  # Indicate success

    def ensure_target_distro_docker_installed(self):
        std_outs, std_err_list = self.ensure_command_to_target_with_pubkey(cmd='sudo usermod -aG docker $USER')
        std_outs, std_err_list = self.ensure_command_to_target_with_pubkey(cmd='sudo apt update')
        std_outs, std_err_list = self.ensure_command_to_target_with_pubkey(
            cmd='curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg')  # GPG 키 추가
        std_outs, std_err_list = self.ensure_command_to_target_with_pubkey(
            cmd='sudo apt install -y apt-transport-https ca-certificates curl software-properties-common gnupg lsb-release')  # wsl docker dependency
        std_outs, std_err_list = self.ensure_command_to_target_with_pubkey(
            cmd='echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')  # Docker 리포지토리 추가
        std_outs, std_err_list = self.ensure_command_to_target_with_pubkey(cmd='sudo apt update')
        std_outs, std_err_list = self.ensure_command_to_target_with_pubkey(
            cmd='sudo apt install -y docker-ce docker-ce-cli containerd.io')

    def ensure_command_to_target(self, cmd):
        return self.ensure_command_to_target_with_pubkey(cmd=cmd)

    def ensure_command_to_target_with_pubkey(self, cmd):
        from functions.ensure_state_printed import ensure_state_printed
        import logging

        from sources.functions.does_pnx_exist import is_pnx_existing
        from sources.functions.ensure_command_executed import ensure_command_executed
        from sources.functions.is_os_windows import is_os_windows
        from sources.objects.pk_local_test_activate import LTA
        import paramiko
        # func_n = get_caller_n()
        try:

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 호스트 키 자동 수락

            # TODO...
            # key_name = 'f_local_ssh_public_key_content'
            # local_ssh_public_key_content = ensure_local_ssh_public_key_content_created(f_local_ssh_private_key=F_LOCAL_SSH_PRIVATE_KEY, f_local_ssh_public_key=F_LOCAL_SSH_PUBLIC_KEY)
            # selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n)
            # f_local_ssh_public_key_content = selected

            # TODO...
            # packages_to_install = ["ufw"]

            key_path = self.f_local_ssh_private_key
            if not is_pnx_existing(pnx=key_path):
                state = is_os_windows()
                ensure_state_printed(state=state, pk_id="%%%FOO%%%")
                if state:
                    ensure_command_executed(f'ssh-keygen -t ed25519 -b 4096 -C "pk_ssh_key"')
                else:
                    ensure_command_executed(f'ssh-keygen -t ed25519 -C "pk_ssh_key"')
            key_private = paramiko.Ed25519Key(filename=key_path)

            logging.debug(f'self.target.ip={self.target.ip}')
            logging.debug(f'self.target.port={self.target.port}')
            logging.debug(f'self.target.user_n={self.target.user_n}')

            if not self.target.ip:
                logging.debug(f'''self.target.ip ] is None ''')
                return None, None

            ssh.connect(hostname=self.target.ip, port=self.target.port, username=self.target.user_n, pkey=key_private)

            # The authenticity of host 'todo' can't be established.
            # ED25519 key fingerprint is SHA256:kO5qGJ92luOdRTm1Ye4pycNnXbNV4sl8gSoB9dAp9Uc.
            # This key is not known by any other names.

            std_outs = []
            std_err_list = []

            cmd_with_sudo_s = f"sudo -S {cmd}"
            logging.debug(f'cmd_with_sudo_s={cmd_with_sudo_s}')
            logging.debug(f'cmd={cmd}')
            stdin, stdout, stderr = ssh.exec_command(cmd_with_sudo_s)

            stdout_str = stdout.read().decode()
            stderr_str = stderr.read().decode()

            if stdout_str:
                std_outs = stdout_str.split("\n")
            if stderr_str:
                std_err_list = stderr_str.split("\n")

            for std_out_str in std_outs:
                logging.debug(f'''"{std_out_str} ''')

            if len(std_outs) > 0 and len(std_err_list) > 0:
                # std_outs 가 std_err_list 모두 있는 경우는 성공했지만 warning 을 띄우는 경우이다. 이 경우는 std_err_list 는 [] 로 초기화 처리했다
                for std_err_str in std_err_list:
                    logging.debug(f'''{"[ REMOTE ERROR ]"} {std_err_str} ''')
                std_err_list = []
                if LTA:
                    logging.debug(f'''std_outs={std_outs} ''')
                    logging.debug(f'''std_err_list={std_err_list} ''')

                return std_outs, std_err_list
            else:
                for std_err_str in std_err_list:
                    logging.debug(f'''{"[ REMOTE ERROR ]"} {std_err_str} {'%%%FOO%%%' if LTA else ''}''')
                if LTA:
                    logging.debug(f'''std_outs={std_outs} {'%%%FOO%%%' if LTA else ''}''')
                    logging.debug(f'''std_err_list={std_err_list} {'%%%FOO%%%' if LTA else ''}''')
                return std_outs, std_err_list

        except:
            ensure_debug_loged_verbose(traceback)
            # Check for specific SSH connection errors
            # TODO 아래는 wsl 국한되는 내용이다. 범용적인  target 의 내용을 상단에 추가하고 wsl 인 경우는 아래처럼 가이드를 해야한다.
            logging.error("SSH 연결에 실패했습니다. 다음 사항을 확인해 주십시오:")
            logging.error(r"1. WSL IP 주소 확인: WSL 터미널에서 'ip addr show eth0 | grep -oP '(?<=inet\s)\d+(\.\d+){3}'' 명령을 실행하여 현재 IP 주소를 확인하고, 코드에서 사용되는 IP와 일치하는지 확인하십시오.")
            logging.error("2. WSL 내 SSH 서버 실행 확인: WSL 터미널에서 'sudo service ssh status' 명령을 실행해 주십시오. 실행 중이 아니라면 'sudo service ssh start' 명령으로 시작할 수 있습니다.")
            logging.error("3. 방화벽 설정 확인: Windows 방화벽 또는 다른 네트워크 방화벽이 22번 포트의 인바운드 연결을 차단하고 있을 수 있습니다. Windows Defender 방화벽 설정에서 22번 포트에 대한 인바운드 규칙이 허용되어 있는지 확인해 주십시오.")
            logging.error(f"연결 시도 정보: IP={self.target.ip}, Port={self.target.port}, User={self.target.user_n}")

    def get_f_local_ssh_public_key(self):
        pass

    def set_target(self):
        func_n = get_caller_n()
        if LTA:
            target = PkTarget(
                identifier=PkDeviceIdentifiers.jetson_xavier,
                user_n=None,
                f_local_ssh_public_key=None,
                f_local_ssh_private_key=None,
                nick_name="pk jetson xavier",
                distro_name="Ubuntu 24.04 LTS",
                hostname=None,
                ip=None,
                pw=None,
                port=None,
            )
            self.target = target
            return
        else:
            key_name = 'target_identifier'
            options = [PkDeviceIdentifiers.jetson_xavier, PkDeviceIdentifiers.jetson_nano, PkDeviceIdentifiers.arduino_nano_classic, PkDeviceIdentifiers.arduino_nano_esp32]
            selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=options)
            target_identifier = selected

            key_name = 'target_user_n'
            selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n)
            target_user_n = selected

            # pk_* ensure_env_var_completed_advanced
            key_name = 'target_f_local_ssh_public_key'
            selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n)
            target_f_local_ssh_public_key = selected

            key_name = 'target_f_local_ssh_private_key'
            selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n)
            target_f_local_ssh_private_key = selected

            key_name = 'target_nick_name'
            selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n)
            target_nick_name = selected

            key_name = 'target_distro_name'
            options = ["windows", "linux", "macos", "android"] + self.get_wsl_distro_names_installed()
            selected = ensure_env_var_completed_advanced(key_name=key_name, func_n=func_n, options=options)
            target_distro_name = selected

            target = PkTarget(
                identifier=target_identifier,
                user_n=target_user_n,
                f_local_ssh_public_key=target_f_local_ssh_public_key,
                f_local_ssh_private_key=target_f_local_ssh_private_key,
                nick_name=target_nick_name,
                distro_name=target_distro_name,
            )
            self.target = target

    @ensure_seconds_measured
    def ensure_target_flashed(self):
        try:
            from objects.device_identifiers import PkDeviceIdentifiers
            import logging

            if not self._setup_successful:
                logging.error("Target setup was not successful. Cannot proceed with flashing.")
                return False

            # self.ensure_target_info_printed()
            self.ensure_target_effective_info_printed()
            self.ensure_wsl_effective_info_printed()

            # ensure_spoken(rf"{get_easy_speakable_text(self.target.identifier.value)} 플래시 작업을 시작합니다")
            if self.target.identifier == PkDeviceIdentifiers.jetson_xavier:

                # windows 과 wsl 간 usb 브릿지 생성
                if not self.ensure_usb_bridge_between_windows_and_wsl_established():
                    logging.warning("usbipd-win 종속성이 해결되지 않아 플래시 프로세스를 중단합니다.")
                    return False

                # sdkmanager가 의존하는 패키지 INSTALLATION
                # sudo apt update
                # sudo apt --fix-broken install -y
                # sudo apt --fix-broken install
                # sudo apt install -y binutils
                # sudo apt install -y build-essential
                # sudo apt install -y libxml2-utils simg2img abootimg liblz4-tool binutils

                # windows sdkmanager-cli 다운로드 (sdkmanager_2.2.1-12028_amd64.deb)
                # nvidia developer website.
                # nvidia developer login.
                # download sdkmanager_2.2.1-12028_amd64.deb by clicking button

                # wsl distro sdkmanager-cli 설치 (sdkmanager_2.2.1-12028_amd64.deb)
                # sudo dpkg -i sdkmanager_


                # wsl
                # mkdir -p ~/Downloads
                # copy "C:\Users\Autonomousa2z\Downloads\sdkmanager_2.2.1-12028_amd64.deb" \\wsl.localhost\Ubuntu-20.04\home\a2z\Downloads
                # cp /mnt/c/Users/user/Downloads/sdkmanager_2.2.1-12028_amd64.deb ~/Downloads/
                # cd ~/Downloads


                self.ensure_sdkmanager_executed()
                # sdkmanager    #  sdkmanager --archived-versions 이거 아님. # 안될때 sudo sdkmanager 로그인 했다가 종료하고 sdkmanager 로 다시 접속
                # self.ensure_command_to_wsl_distro_like_human(cmd="sdkmanager", window_title_seg=windows_title_seg)


                # start "5: cd ~/flash/no_flash/Linux_for_Tegra" cmd.exe /k "wsl sudo find ~/flash -type f -name 'flash.sh'"

                # WSL 에서 실행중인데 cmd  를 관리자 권한으로 실행하고 WSL 을 실행해서 sdkmanger 실행했는데 여전히 You do not have permission to access the download folder. 나와
                # download 폴더를 변경 create and select pk_download   -> ~/Downloads/pk_nvidia ->   flash/evm_flash

                # jetpack installation via sdkmanager as gui

                # nvidia developer login
                # 로그인웹이 자동으로 안열리는 경우, 재부팅부터 해보자, QR code 로 시도
                # smart phone 에서 QR 촬영을 해서 smart phone web 열리면 로그인
                # 다른거 치라는데 패스워드 치면 됨.
                # 로그인 되면서 device type select 창이 나옴.
                # Jetson AGX Xavier
                # OK
                # Later

                # show all versions
                # 4.6.6
                # [fail] ensure only os without nvidia sdk component
                # ensure both os and nvidia sdk component
                # continue
                # ensure download now. install later. disable # 이거 체크하면 flash 진행하지 않음
                # ensure I accpet the terms and conditions of the license agreements. able
                # continue
                # manual flash try, # 안해도 될 듯 download now. install later. able 처리해서 발생한 문제
                # wait for OEM Configuration setting pop up
                # Runtime # OEM Configuration # 자꾸 안되서 Runtime 안하고 pre-config 로 해봄 pre-config는 default 임
                # Flash
                # finish

                # [fail] ensure ubuntu OEM : in evm
                # evm
                # EVM terminal x
                # accept blah lisence
                # display on
                # agree
                # english
                # english(US)
                # english(US)
                # seoul
                # nvidia
                # nvidia
                # nvidia
                # nvidia
                # nvidia
                # MAXN
                # log in automatically
                # Install # if this process fail, retry flash

                # set evm network wired connection 1 as 192.168.2.124 22 192.168.1.1 8.8.8.8 manualy in evm
                # sudo apt update in evm
                # skip check
                # pkill sdkmanger-gui
                # sdkmanger
                # ensure only nvidia sdk component without os(jetpack)
                # Ethernet
                # 192.168.2.124
                # nvidia
                # nvidia
                # install

                # ensure log in automatically

                # ensure MAXN

                # ensure no passwd

                # ensure stack size 10240 #MEMORY LEAK 예방 #10240로 합의
                # sudo vi /etc/security/limits.conf
                # #End of file
                # nvidia hard stack 10240
                # nvidia soft stack 10240
                # ubuntu hard stack 10240
                # ubuntu soft stack 10240
                # root hard stack 10240
                # root soft stack 10240
                # :wq
                # cat /etc/security/limits.conf

                # ensure ntp available
                # sudo vi /etc/systemd/timesyncd.conf
                # [Time]
                # NTP=192.168.10.10 #server ip(control PC)
                # FallbackNTP=ntp.ubuntu.com
                # RootDistanceMaxSec=15 #5→15
                # PollIntervalMinSec=32
                # PollIntervalMaxSec=2048
                # # timedatectl set-ntp no #자동 시간동기화 해제
                # # date
                # # timedatectl set-time "2024-10-28 13:26:00" #수동 시간 SETTING

                # ensure auto reboot

                # make flash image # started at 15:18
                # recovery mode again
                # sudo find /home -type f -name "flash.sh"
                # evm_flash_jetpack_4_6_6_ready.img 는 ip124,  ntp, stack, ensure 함.
                # evm_flash_jetpack_4_6_6_with_side_a.img
                # evm_flash_jetpack_4_6_6_with_side_b.img
                # sudo ./flash.sh -r -k APP -G evm_flash_jetpack_4_6_6_ready.img jetson-xavier mmcblk0p1
                # sudo ./flash.sh -r -k APP -G evm_flash_jetpack_4_6_6_with_side_a.img jetson-xavier mmcblk0p1
                # sudo ./flash.sh -r -k APP -G evm_flash_jetpack_4_6_6_with_side_b.img jetson-xavier mmcblk0p1
                # sudo find /home -type f -name "evm_flash_jetpack_4_6_6*"
                # ended at mkr.

                pass
            # elif self.is_target_flash_image_exists() == 1:
            # sudo ./flash.sh -r -k APP -G EVM_flash_241125.img jetson-xavier mmcblk0p1
            # pass

            # elif 'no' == self.target.identifier:
            #     with_flash_image = self.is_target_flash_image_exists()
            #     if self.is_target_flash_image_exists():
            #         ensure_command_to_remote_os(cmd='sdkmanager',
            #                          wsl)  # execute sdkmanager    # todo sdkmanager cli 로 업그레이드 시도
            #
            #         ensure_remote_os_connection(wsl)  # test_ip
            #
            #         ensure_target_jetpack(wsl)
            #
            #         ensure_remote_os_connection(wsl)  # test_ip
            #
            #         ensure_os_locked()
            #         ensure_screen_black_never()
            #         ensure_maxn()
            #         reboot_vpc()
            #
            #     if not self.is_target_flash_image_exists():
            #         ensure_remote_os_connection(wsl)
            #
            #     ensure_target_aifw_running(selfwsl)  # todo
            # elif 'xc' == self.target.identifier:
            #     while 1:
            #         # todo : reference : XC도 4.6.6 고정되고 나면 플래시 이미지로만 관리
            #         if self.is_target_flash_image_exists():
            #             cmd_to_wsl_os_like_human_deprecated(cmd=rf"echo {wsl_pw} | sudo -S ./flash.sh -r jetson-xavier mmcblk0p1",
            #                                                 distro_name=wsl.selected,
            #                                                 wsl_window_title_seg=wsl_window_title_seg)
            #
            #             # target_device_data 추가설정
            #             #  ntp
            #             #  stacksize
            #
            #             gen_target_flash_image()
            #
            #         elif not self.is_target_flash_image_exists():
            #             # cd
            #             # cmd = "cd ~/Downloads/flash/xc_flash/Linux_for_Tegra/"
            #             # cmd_to_wsl_os_like_human_deprecated(cmd=cmd, distro_name=target_device_data_os_n, wsl_window_title_seg=wsl_window_title_seg, exit_mode=exit_mode)
            #
            #             # ensure system.img* and system.img.raw
            #             ensure_location_about_system_img_and_system_img_raw(wsl)
            #
            #             # flash
            #             cmd = rf"echo {wsl_pw} | sudo -S ./flash.sh -r jetson-xavier mmcblk0p1"
            #             cmd_to_wsl_os_like_human_deprecated(cmd=cmd, distro_name=wsl.selected,
            #                                                 wsl_window_title_seg=wsl_window_title_seg)
            #
            #             # sudo mv /home/task_orchestrator_cli/Downloads/flash/xc_flash/Linux_for_Tegra/system.img* /home/task_orchestrator_cli/Downloads/flash/xc_flash/Linux_for_Tegra/rootfs/bin/
            #
            #             # cmd = rf'sudo find -type f -name "system.img*"'
            #             # cmd_to_wsl_like_human(cmd=cmd, distro_name=distro_name, wsl_window_title_seg=wsl_window_title_seg)
            #             #
            #             # cmd = rf'df -h'
            #             # cmd_to_wsl_like_human(cmd=cmd, distro_name=distro_name, wsl_window_title_seg=wsl_window_title_seg)
            #             #
            #             # cmd = rf'explorer \\wsl$'
            #             # ensure_command_executed(cmd=cmd)
            #
            #             time_s = time.localtime(time_s)
            #             check_manual_task_iteractively(
            #                 f'''The flash has Started at {time_s.tm_hour:02}:{time_s.tm_min:02}. Has the flash ended?''')
            #
            #             elapsed_seconds = time.time() - time_s
            #             elapsed_minutes = elapsed_seconds / 60
            #
            #             logging.debug(rf'''FLASH : This function took {elapsed_minutes} minutes  {'%%%FOO%%%' if LTA else ''}''')
            #             # todo : elapsed_minutes 이걸 f에 매번 기록, 공정시간 자동통계
            #             # 해당공정이 통계시간보다 느리거나 빠르게 종료되었다는 것을 출력 하도록
            #
            #         check_manual_task_iteractively(question=rf'''DID YOU EXIT WSL FLASH PROGRAM AT LOCAL?  %%%FOO%%%''')
            #         check_manual_task_iteractively(question=rf'''DID YOU EXIT WSL ATTACH PROGRAM AT LOCAL?  %%%FOO%%%''')
            #         # todo : 플래시이미지 재생성 후 해당 내용 네트워크 설정 자동화 후 추후삭제예정
            #         check_manual_task_iteractively(question=rf'''DID YOU SET WIRED CONNECTION 3 AS {target_device_wired_connection_3_new} ?  %%%FOO%%%''')
            #         ensure_target_side_mode(target_device_data=self, wsl)
            #         if not ensure_target_accessable(self, wsl):
            #             # history : ensure_target_accessable() 수행 -> target_device 접속안됨 -> Wired Connection 활성화 실패->gui 통해서 2.76 으로 ssh 접속 시도->fail->flash 재수행->success
            #             # flash 재수행해야 하는 경우로 판단
            #             continue
            #
            # else:
            #     logging.debug(f'''unknown target_device_data.identifier ({self.target_device_identifier}) {'%%%FOO%%%' if LTA else ''}''',
            #                   )
            #     raise

            return True
        except:
            ensure_debug_loged_verbose(traceback)
        finally:
            ensure_spoken(wait=True)

    def ensure_self_info_printed(self):
        """Prints all fields of the PkTargetManager (self) in pretty JSON format."""
        import logging
        import json

        self_dict = {
            "identifier": self.identifier.value if self.identifier else None,
            "nick_name": self.nick_name,
            "state": self.state.name if self.state else None,
            "ip": getattr(self, 'ip', None),
            "hostname": getattr(self, 'hostname', None),
            "port": getattr(self, 'port', None),
            "user_n": getattr(self, 'user_n', None),
            "f_local_ssh_public_key": str(getattr(self, 'f_local_ssh_public_key', None)),
            "f_local_ssh_private_key": str(getattr(self, 'f_local_ssh_private_key', None)),
            # Password ('pw') is intentionally omitted for security.
        }

        pretty_json = json.dumps(self_dict, indent=4, ensure_ascii=False)
        logging.debug(f"PkTargetManager (self) info:\n{pretty_json}")
        return pretty_json

    def ensure_target_recovery_mode_entered(self):
        import logging
        import re
        from objects.device_identifiers import PkDeviceIdentifiers
        if self.target.identifier == PkDeviceIdentifiers.jetson_xavier:
            guide_title = "리커버리 모드 진입"
            question = f'{guide_title}시도'
            ensure_spoken(get_easy_speakable_text(question))
            while True:
                if is_os_windows():
                    cmd = "usbipd.exe list"  # 수동가이드 : start "1: usbipd.exe list" wsl watch -n 0.3 usbipd.exe list 대응 파이썬 코드

                    souts, _ = ensure_command_executed(cmd=cmd, encoding='utf-8')
                    bus_id = None
                    device_signature = "APX"

                    # 정규표현식을 사용하여 BUSID, VID:PID, DEVICE, STATE를 정확히 파싱
                    line_pattern = re.compile(r"^\s*([0-9\-]+)\s+([0-9a-fA-F]{4}:[0-9a-fA-F]{4})\s+(.*?)\s{2,}(.*)$")

                    logging.debug("--- 'usbipd list' 출력 파싱 시작 ---")
                    if not souts:
                        logging.warning("'usbipd list' 명령어의 출력이 없습니다.")

                    for line in souts:
                        if not line.strip():
                            continue
                        logging.debug(f"파싱 대상 라인: \"{line}\"")
                        match = line_pattern.match(line)
                        if match:
                            parsed_bus_id = match.group(1)
                            parsed_vid_pid = match.group(2)
                            parsed_device = match.group(3).strip()
                            parsed_state = match.group(4).strip()

                            logging.debug(f"  -> 파싱 결과: BUSID={parsed_bus_id}, VID:PID={parsed_vid_pid}, DEVICE='{parsed_device}', STATE='{parsed_state}'")

                            if device_signature in parsed_device:
                                bus_id = parsed_bus_id
                                logging.info(f"타겟 장치 '{device_signature}' 발견. BUSID: {bus_id}")
                                break  # 첫 번째 일치하는 장치를 찾으면 중단
                        else:
                            # 파싱에 실패한 라인도 로그를 남겨 디버깅을 용이하게 함
                            logging.debug(f"  -> 라인이 예상 형식과 일치하지 않아 파싱에 실패했습니다.")

                    if bus_id is None:
                        error_message = "Could not find a device with the required signature (APX) from 'usbipd list' output."
                        logging.warning(error_message)

                        guide_message = textwrap.dedent("""
                                    [가이드] 타겟 장치(APX)를 찾을 수 없습니다.
                                    플래시를 계속하려면, Jetson 장치를 복구 모드(Recovery Mode)로 설정하고 PC와 USB로 연결해야 합니다.
                                    연결 상태를 확인하고 다시 시도해주세요.
                                """)
                        logging.warning(get_text_yellow(guide_message))
                        ensure_spoken(get_easy_speakable_text("타겟 장치를 찾을 수 없습니다. 화면의 가이드를 확인해주세요."))

                        return False
                    logging.debug(rf'''bus_id={bus_id}  {'%%%FOO%%%' if LTA else ''}''')

                    # wsl --shutdown 을 실행해야합니다 진행할까요?
                    # ensure_command_executed(cmd="wsl --shutdown", encoding='cp949')
                    ensure_command_executed(cmd=f"wsl --terminate -d {self.wsl.distro_name}", encoding='cp949') # wsl --terminate  # 바인딩 하지 않을 wsl distro 해제


                    souts = ensure_command_executed(cmd=rf"wsl -d {self.wsl.distro_name} -- exit", encoding='cp949')
                    if check_signiture_in_loop(time_limit=10, working_list=souts, signiture="제공된 이름의 배포가 없습니다", signiture_found_ment=rf"'{cmd}' 할수없었습니다"):
                        return False

                    souts = ensure_command_executed(cmd="wsl -l -v", encoding='utf-16-le')
                    ensure_command_executed(cmd=rf"usbipd unbind -b {bus_id}", encoding='cp949')

                    ensure_command_executed(cmd=rf"usbipd bind -b {bus_id}", encoding='cp949')  # 수동가이드 : start "3: usbipd bind -b $BUSID" cls && usbipd bind -b $BUSID
                    # ensure_command_executed_like_human(cmd=rf"usbipd attach --wsl --busid {bus_id} --auto-attach")
                    ensure_command_executed(cmd=rf'start "" usbipd attach --wsl --busid {bus_id} --auto-attach')  # 수동가이드 : start "4: usbipd attach --wsl --busid $BUSID --auto-attach" cls && usbipd attach --wsl --busid $BUSID --auto-attach

                    # usb/ip attached to wsl
                    # 수동가이드 : start "2: lsusb" wsl watch -n 0.3 lsusb
                    # signiture="제공된 이름의 배포가 없습니다" or 'xxxx'
                    souts = ensure_command_executed(cmd=rf"wsl -d {self.wsl.distro_name} lsusb", encoding='cp949')  # 수동가이드 : watch -n 1 lsusb
                    if check_signiture_in_loop(time_limit=10, working_list=souts, signiture="제공된 이름의 배포가 없습니다", signiture_found_ment="wsl 에 attach 할수없었습니다"):
                        return False
                    if check_signiture_in_loop(time_limit=10, working_list=souts, signiture="NVidia Corp.", signiture_found_ment="wsl 에 attach 되었습니다"):
                        return False


                    # jetpack update" via sdkmanger #원격방식 가능#usb방식 가능?


                # pk_* : 가이드
                guide = textwrap.dedent(rf'''
                    # {guide_title} 수동가이드
                    
                    # Force Recovery Mode of Jetson Xavier Series way 1 (success)
                    n. Power on the carrier board # power button
                    n. hold the RECOVERY button  # cw button # # EVM 의 가운데 버튼
                    n. Press the RESET button    # ccw button
                    n. USB C to A 케이블을 연결 PC 의 뒷편(A), Xaver WHITE LED 인디케이터 옆 USB 포트(C)  
                    
                    # Force Recovery Mode of Jetson Xavier Series way 2
                    n. remove all plugs 
                    n. remove auto power selector pin
                    n. reconnect power cable
                    n. reconnect usb c(right port # not left port)
                    n. hold the RESET button.    # ccw button
                    n. press power button.
                    n. release power button.
                    n. reinstall auto power mode selector pin
                    
                ''')
                logging.debug(get_text_cyan(guide))
                ok = ensure_value_completed(key_hint=rf"{question}=", options=[PkTexts.YES, PkTexts.NO, PkTexts.FAILED])
                if ok != PkTexts.YES:
                    ensure_spoken(get_easy_speakable_text(f'{guide_title}를 반드시 수행해야 다음으로 진행할 수 있습니다'))
                    continue
                if ok != PkTexts.FAILED:
                    guide_title = f'{guide_title} 트러블슈팅'
                    guide = textwrap.dedent(rf'''
                                            # {guide_title} 수동가이드
                                            n. 플래시 케이블 연결안함
                                            n. 네트워크 케이블 remove 후 재시도
                                        ''')
                    logging.debug(get_text_yellow(guide))
                    ok = ensure_value_completed(key_hint=rf"{question}=", options=[PkTexts.YES])
                    if ok != PkTexts.YES:
                        ensure_spoken(get_easy_speakable_text(f'{guide_title}를 반드시 수행해야 다음으로 진행할 수 있습니다'))
                        continue
                continue

    def ensure_target_info_printed(self):
        logging.debug(f'self.target.to_json()={self.target.to_json()}')
        return

    def ensure_target_effective_info_printed(self):
        """
        Print only non-None fields of target in pretty JSON format.
        """
        import logging
        import json

        # target 객체 → dict
        target_dict = self.target.to_dict()

        # None 값 제거
        effective_dict = {k: v for k, v in target_dict.items() if v is not None}

        # JSON 문자열 변환
        pretty_json = json.dumps(effective_dict, indent=4, ensure_ascii=False)

        logging.debug(pretty_json)
        return pretty_json

    def get_f_wsl_sshd_config_path(self, distro_name: str) -> Optional[Path]:
        """
        지정된 WSL 배포판의 sshd_config 파일에 대한 Windows 호스트 접근 경로를 반환합니다.

        Args:
            distro_name: 대상 WSL 배포판의 이름입니다.

        Returns:
            Windows에서 접근 가능한 sshd_config 파일의 Path 객체.
            distro_name이 제공되지 않으면 None을 반환합니다.
        """
        import logging
        from pathlib import Path

        from objects.task_orchestrator_cli_files import F_WSL_SSHD_CONFIG

        if not distro_name:
            logging.error("distro_name이 제공되지 않았습니다.")
            return None

        # Windows에서 WSL 파일 시스템에 접근하기 위한 UNC 경로
        # \wsl.localhost\Ubuntu\etc\ssh\sshd_config 형식
        wsl_path = Path(f"//wsl.localhost/{distro_name}{F_WSL_SSHD_CONFIG}")

        logging.debug(f"생성된 WSL sshd_config 경로: {wsl_path}")

        return wsl_path

    def ensure_usbipd_installed(self):
        from functions import ensure_command_executed
        guide_title = "usbipd-win 설치"
        question = f"'{guide_title}' 가이드를 모두 완료하고 uspipd가 준비되었습니까?"
        ensure_spoken(get_easy_speakable_text(f"{guide_title}를 시작합니다. 웹페이지를 확인해주세요."))

        # Open the download page once at the beginning
        ensure_command_executed("explorer https://github.com/dorssel/usbipd-win/releases")
        while True:
            guide = textwrap.dedent(f'''
                        # {guide_title} 수동 가이드 (usbipd-win_5.2.0_x64.msi 파일사용 가정)
                        n. 방금 열린 웹페이지/Assets/usbipd-win_5.2.0_x64.msi 클릭
                        n. 다운로드된 usbipd-win_5.2.0_x64.msi 클릭 후 설치창의 절차진행
                        n. cmd.exe 또는 PowerShell 터미널에서  `usbipd --version`  5.2.0-45+Branch.master.Sha.e37737bfa2c8bafbe33674fc32eda3857dab6893.e37737bfa2c8bafbe33674fc32eda3857dab6893 이런 해시 형태의 버전이 나오면 정상설치완료
                    ''')
            logging.info(get_text_cyan(guide))

            ok = ensure_value_completed(key_hint=rf"{question} (y/n): ", options=[PkTexts.YES, PkTexts.NO])

            if ok == PkTexts.YES:
                logging.info("사용자가 설치 완료를 확인했습니다. uspipd 상태를 다시 확인합니다...")
                if self.get_uspipd_version():
                    logging.info("usbipd가 성공적으로 확인되었습니다.")
                    ensure_spoken(get_easy_speakable_text("usbipd가 성공적으로 확인되었습니다."), wait=True)
                    return True
                else:
                    logging.error("오류: 사용자가 완료를 확인했지만, 여전히 uspipd를 사용할 수 없습니다.")
                    troubleshooting_guide = textwrap.dedent(f'''
                                # {guide_title} 트러블슈팅
                                n. PC를 재부팅한 후 `usbipd` 명령어 시도.
                                n. PowerShell 세션을 닫고 `usbipd` 명령어 시도.
                                n. PowerShell(관리자)에서 `usbipd` 명령어 시도.
                                n. target이 PC에 올바르게 연결되어 있는지 확인해주세요.(wsl 의 경우는 상관없어요) 
                            ''')
                    logging.warning(get_text_yellow(troubleshooting_guide))
                    ensure_spoken(get_easy_speakable_text("설치 확인에 실패했습니다. 트러블슈팅 가이드를 확인하고 재시도해주세요."), wait=True)
                    continue
            else:  # PkTexts.NO or other
                ensure_spoken(get_easy_speakable_text(f'{guide_title}를 반드시 수행해야 다음으로 진행할 수 있습니다.'))
                # Loop will continue

    def ensure_wsl_effective_info_printed(self):
        """
        Print only non-None fields of wsl in pretty JSON format.
        """
        import logging
        import json

        if not hasattr(self, 'wsl') or self.wsl is None:
            logging.warning("self.wsl is not initialized. Cannot print effective info.")
            return None

        # wsl 객체 → dict
        wsl_dict = self.wsl.to_dict()

        # None 값 제거
        effective_dict = {k: v for k, v in wsl_dict.items() if v is not None}

        # JSON 문자열 변환
        pretty_json = json.dumps(effective_dict, indent=4, ensure_ascii=False)

        logging.debug(f"WSL effective info:\n{pretty_json}")
        return pretty_json

    def is_usbipd_enabled(self):
        import subprocess
        import logging
        try:
            command = ["usbipd", "list"]
            logging.debug(f"Executing command: {' '.join(command)}")

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                encoding='utf-8',
                errors='ignore'
            )

            if result.returncode == 0:
                logging.info("usbipd-win is enabled and accessible.")
                return True
            else:
                logging.warning(f"'usbipd wsl list' command failed with return code {result.returncode}.")
                if result.stderr:
                    logging.debug(f"usbipd stderr: {result.stderr.strip()}")

                # Automatically check the service status for better diagnostics
                try:
                    sc_command = ["sc", "query", "usbipd"]
                    sc_result = subprocess.run(sc_command, capture_output=True, text=True, check=False, encoding='utf-8', errors='ignore')
                    service_status = sc_result.stdout.strip()
                    logging.debug(f"Checking service status for 'usbipd':\n{service_status}")

                    if "STOPPED" in service_status:
                        logging.error("The 'usbipd' service is stopped. Please start it by running 'sc start usbipd' in a terminal with administrator privileges.")
                    elif "RUNNING" in service_status:
                        logging.warning("The 'usbipd' service is running, but the command failed. This might be a permissions issue or a problem with the WSL integration.")
                    else:
                        logging.warning("Could not determine the state of the 'usbipd' service, but the command failed.")

                except FileNotFoundError:
                    logging.error("'sc.exe' not found. Cannot automatically check the service status.")
                except Exception as sc_e:
                    logging.error(f"An unexpected error occurred while checking the usbipd service status: {sc_e}")
                return False

        except FileNotFoundError:
            logging.error(
                "The 'usbipd' command was not found. "
                "Please ensure usbipd-win is installed and its location is included in the system's PATH environment variable."
            )
            return False
        except Exception as e:
            logging.error(f"An unexpected error occurred while checking usbipd-win status: {e}")
            return False

    def get_uspipd_version(self):
        """
        Checks for usbipd-win version on Windows by running 'usbipd --version'.
        Returns the version string if found, otherwise None.
        """
        import subprocess
        import logging
        from sources.functions.is_os_windows import is_os_windows

        if not is_os_windows():
            logging.debug("get_uspipd_version is only supported on Windows.")
            return None

        try:
            # Execute the command to get the version
            result = subprocess.run(
                ["usbipd", "--version"],
                capture_output=True,
                text=True,
                check=True,  # Raises CalledProcessError for non-zero exit codes
                encoding='utf-8',
                errors='ignore'
            )
            # The output is typically just the version string
            version = result.stdout.strip()
            if version:
                logging.debug(f"Found usbipd-win version: {version}")
                return version
            else:
                logging.warning("'usbipd --version' command ran but returned empty output.")
                return None

        except FileNotFoundError:
            # This means the 'usbipd' command was not found in the system's PATH
            logging.warning("'usbipd' command not found. usbipd-win may not be installed or not in PATH.")
            return None
        except subprocess.CalledProcessError as e:
            # This means the command executed but returned an error
            logging.error(f"The 'usbipd --version' command failed: {e.stderr}")
            return None
        except Exception as e:
            # Catch any other unexpected errors
            logging.error(f"An unexpected error occurred while checking usbipd version: {e}")
            return None

    def ensure_sdkmanager_executed(self):
        if not self.ensure_sdkmanager_installed():
            return False

        # sdkmanager --cli --help
        # list products
        # list targets
        # list components

    def ensure_sdkmanager_installed(self):
        self.ensure_wsl_distro_pkg_rar_installed()

    def ensure_wsl_distro_pkg_rar_installed(self):
        import logging

        try:
            logging.debug("Starting ensure_wsl_distro_pkg_rar_installed...")
            wsl_distro_config = self.get_wsl_distro_config()

            # Ensure dependencies
            packages_to_install = ["rar"]
            # return ensure_wsl_packages_installed(wsl_distro_config.distro_name, packages_to_install)
            return self.ensure_wsl_packages_installed(wsl_distro_config['distro_name'], packages_to_install)

        except Exception as e:
            ensure_debug_loged_verbose(traceback)
            return False

    @ensure_seconds_measured
    @ensure_function_return_ttl_cached(ttl_seconds=60 * 1 * 1, maxsize=10)  # task_orchestrator_cli_option
    def ensure_wsl_packages_installed(self, distro_name, packages):
        import logging

        from functions.ensure_command_executed import ensure_command_executed

        """Checks if a list of packages are installed in a WSL distribution and installs them if not."""
        for package in packages:
            logging.debug(f"Checking if '{package}' is installed in WSL distro '{distro_name}'...")
            # Using 'dpkg -s' is more reliable for checking installation status of Debian packages.
            check_cmd = f"wsl -d {distro_name} -- dpkg -s {package}"
            outs, errs = ensure_command_executed(check_cmd)

            # 'dpkg -s' outputs to stdout and has a zero exit code if the package is installed.
            # If not installed, it outputs to stderr and has a non-zero exit code.
            if not errs:
                logging.info(f"Package '{package}' is already installed in '{distro_name}'.")
                continue

            # Package is not installed or check failed, proceed with installation.
            logging.warning(f"Package '{package}' not found or check failed in '{distro_name}'. Attempting to install...")

            # Update package list first
            update_cmd = f"wsl -d {distro_name} -- sudo apt-get update"
            logging.debug(f"Running package list update in '{distro_name}'...")
            update_outs, update_errs = ensure_command_executed(update_cmd)
            if update_errs:
                # This might not be a fatal error, so just log a warning.
                logging.warning(f"Error updating package lists in '{distro_name}': {update_errs}")

            # Install the package
            install_cmd = f"wsl -d {distro_name} -- sudo apt-get install -y {package}"
            logging.debug(f"Running installation for '{package}' in '{distro_name}'...")
            install_outs, install_errs = ensure_command_executed(install_cmd)
            if install_errs:
                logging.error(f"Failed to install '{package}' in '{distro_name}': {install_errs}")
                raise RuntimeError(f"Failed to install '{package}' in WSL distro '{distro_name}'.")

            # Verify installation
            logging.debug(f"Verifying installation of '{package}' in '{distro_name}'...")
            verify_outs, verify_errs = ensure_command_executed(check_cmd)
            if verify_errs:
                logging.error(f"Verification failed for '{package}' in '{distro_name}' after installation attempt: {verify_errs}")
                raise RuntimeError(f"Failed to verify '{package}' installation in WSL distro '{distro_name}'.")

            logging.info(f"Successfully installed and verified '{package}' in '{distro_name}'.")

        return True

    @ensure_seconds_measured
    @ensure_function_return_ttl_cached(ttl_seconds=60 * 60 * 1, maxsize=10)  # task_orchestrator_cli_option
    def get_wsl_distro_name_installed_legacy(self):
        from functions.ensure_value_completed_advanced import ensure_value_completed_advanced

        wsl_distro_names_installed = self.get_wsl_distro_names_installed()

        if len(wsl_distro_names_installed) == 1:
            return wsl_distro_names_installed[0]

        else:
            key_name = "wsl_distro_name"
            from functions.get_caller_n import get_caller_n
            func_n = get_caller_n()
            selected = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=wsl_distro_names_installed)
            wsl_distro_name = selected

            return wsl_distro_name

    def get_wsl_distro_name_installable(self, cmd):
        from sources.functions.ensure_command_executed import ensure_command_executed
        wsl_distro_name = []
        std_outs = ensure_command_executed(cmd=cmd, encoding='utf-16')
        for line_str in std_outs:
            line_str = line_str.strip()
            if line_str.startswith("NAME"):
                continue
            if line_str.startswith("*"):
                line_str = line_str.replace("* ", "")
                line_str = line_str.strip()
            parts = line_str.split(' ')
            name = parts[0]
            line_str = line_str.strip()
            wsl_distro_name.append(name)
        return wsl_distro_name

    def get_wsl_distro_pw_legacy(self, distro_name):
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()  # Get function name
        env_var_name = get_env_var_id("PASSWORD", func_n)
        prompt_message = f"Please enter the password for WSL distro '{distro_name}': "

        wsl_pw = ensure_env_var_completed(env_var_name, prompt_message)

        return wsl_pw

    def get_wsl_distro_ip_legacy(self, distro_name):
        import logging
        from sources.functions.is_os_wsl_linux import is_os_wsl_linux
        from sources.functions.is_os_windows import is_os_windows
        from sources.functions.ensure_command_executed import ensure_command_executed
        from sources.functions.ensure_env_var_completed import ensure_env_var_completed
        from sources.functions.get_env_var_name_id import get_env_var_id  # New import
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()  # Get function name

        std_outs = None
        if is_os_windows():
            std_outs = ensure_command_executed(rf'wsl -d {distro_name} hostname -I')
        else:
            if is_os_wsl_linux():
                std_outs = ensure_command_executed(rf'hostname -I')
            else:
                pass

        wsl_ip = None
        if std_outs and len(std_outs) > 0:
            logging.debug(f"DEBUG: In get_wsl_ip, type(std_outs)={type(std_outs)}, std_outs={std_outs}")
            logging.debug(f"DEBUG: In get_wsl_ip, type(std_outs[0])={type(std_outs[0])}, std_outs[0]={std_outs[0]}")
            wsl_ip = std_outs[0][0].split(" ")[0]

        if not wsl_ip:
            env_var_name = get_env_var_id("IP", func_n)  # Use helper function
            prompt_message = f"Please enter the IP address for WSL distro '{distro_name}': "
            wsl_ip = ensure_env_var_completed(env_var_name, prompt_message)

        return wsl_ip

    def get_wsl_distro_user_name_legacy_via_whoami(self, distro_name):
        import logging

        from sources.functions.ensure_command_executed import ensure_command_executed
        from sources.functions.ensure_env_var_completed import ensure_env_var_completed  # New import
        from sources.functions.get_env_var_name_id import get_env_var_id  # New import
        from sources.functions.get_list_without_none_and_duplicates import get_list_without_none_and_duplicates
        from sources.functions.is_os_windows import is_os_windows
        from sources.objects.pk_local_test_activate import LTA

        std_outs = None
        if is_os_windows():
            std_outs = ensure_command_executed(f'wsl -d {distro_name} whoami')
        else:
            std_outs = ensure_command_executed(rf'whoami', encoding='utf-8')

        user_n = None
        if std_outs:
            user_n_list = get_list_without_none_and_duplicates(std_outs)
            if len(user_n_list) == 1:
                user_n = user_n_list[0]
            else:
                logging.debug(f"현재 wsl에 로그인된 사용자가 한명이 아닙니다 user_n_list=[{user_n_list}]")

                # Removed raise to allow fallback

        # If username is not found, use ensure_env_var_completed as fallback
        if not user_n:
            from functions.get_caller_n import get_caller_n
            func_n = get_caller_n()  # Get function name
            env_var_name = get_env_var_id("USERNAME", func_n)  # Use helper function
            prompt_message = f"Please enter the username for WSL distro '{distro_name}': "
            user_n = ensure_env_var_completed(env_var_name, prompt_message)

        if user_n:
            logging.debug(rf'''user_n"{user_n}"  {'%%%FOO%%%' if LTA else ''}''')
        return user_n
