#!/usr/bin/env python3
import logging

try:
    from sources.functions.ensure_embeded_script_created import ensure_embeded_script_created
    from functions.ensure_guided_not_prepared_yet import ensure_not_prepared_yet_guided
    from sources.functions.ensure_pnxs_move_to_recycle_bin import ensure_pnxs_move_to_recycle_bin
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.objects.pk_etc import PK_UNDERLINE
    from sources.objects.pk_map_texts import PkTexts
    from sources.objects.task_orchestrator_cli_directories import *
    from sources.objects.task_orchestrator_cli_files import *
    from abc import ABC, abstractmethod
    import traceback

    class PlatformManager(ABC):
        """플랫폼별 관리자 추상 클래스"""

        def __init__(self):
            self.utils = PkSystemManager()

        @abstractmethod
        def install_uv(self, max_retry: int = 2) -> bool:
            """UV 설치"""
            pass

        @abstractmethod
        def install_fzf(self, max_retry: int = 2) -> bool:
            """FZF 설치"""
            pass

        @abstractmethod
        def setup_path(self) -> bool:
            """PATH 설정"""
            pass

        @abstractmethod
        def setup_aliases(self) -> bool:
            """별칭 설정"""
            pass

        @abstractmethod
        def sync_uv_packages(self) -> bool:
            """UV 패키지 동기화"""
            pass

        @abstractmethod
        def install_packages_with_venv_python(self) -> bool:
            """virtual environment Python으로 패키지 설치"""
            pass

        @abstractmethod
        def test_venv_python(self) -> bool:
            """virtual environment Python 테스트"""
            pass


    class PkSystemManager:
        """공통 유틸리티 함수들"""

        @staticmethod
        def detect_os() -> str:
            """OS 감지"""
            system = platform.system().lower()
            if system == "windows":
                return "windows"
            elif system == "linux":
                try:
                    with open("/proc/version", "r") as f:
                        if "microsoft" in f.read().lower():
                            return "linux"  # WSL
                except:
                    pass
                return "linux"
            elif system == "darwin":
                return "macos"
            else:
                return "unknown"

        @staticmethod
        def try_import_or_install(pkg_name: str, import_name: str = None) -> None:
            import subprocess
            import sys

            """모듈을 import하거나 설치"""
            import_name = import_name or pkg_name
            try:
                __import__(import_name)
            except ImportError:
                logging.debug(f"'{pkg_name}' {PkTexts.MODULE_NOT_FOUND}, attempting to install...")
                try:
                    subprocess.run([sys.executable, "-m", "pip", "install", pkg_name], check=True)
                except Exception as e:
                    logging.debug(f"{PkTexts.INSTALL_FAILED} '{pkg_name}': {e}")
                    raise

        @staticmethod
        def print_step(step_index: int, total_steps: int, description: str, color: str = "cyan") -> None:
            import platform

            from sources.functions.ensure_task_orchestrator_cli_colorama_initialized_once import ensure_task_orchestrator_cli_colorama_initialized_once

            """단계 출력"""
            # Windows 환경에서 ANSI 색상 코드 문제 방지
            if platform.system().lower() == "windows":
                try:
                    ensure_task_orchestrator_cli_colorama_initialized_once()
                    # Windows에서 색상 출력 시도
                    color_code = {"cyan": 36, "yellow": 33, "green": 32, "red": 31, "blue": 34}.get(color, 36)
                    logging.debug(f"\033[{color_code}m[{step_index}/{total_steps}] {description}\033[0m")
                except (ImportError, Exception):
                    # colorama 실패 시 색상 없이 출력
                    logging.debug(f"[{step_index}/{total_steps}] {description}")
            else:
                # Linux/Mac에서는 기본 ANSI 색상 코드 사용
                try:
                    color_code = {"cyan": 36, "yellow": 33, "green": 32, "red": 31, "blue": 34}.get(color, 36)
                    logging.debug(f"\033[{color_code}m[{step_index}/{total_steps}] {description}\033[0m")
                except Exception:
                    # ANSI 색상 코드 실패 시 색상 없이 출력
                    logging.debug(f"[{step_index}/{total_steps}] {description}")

        @staticmethod
        def download_file(url: str, file_path: Path, max_retry: int = 2) -> bool:
            """파일 다운로드 (공통)"""
            PkSystemManager.try_import_or_install("requests")
            import requests

            for attempt in range(1, max_retry + 1):
                try:
                    logging.debug(f"[Attempt {attempt}] Downloading from {url}")
                    with requests.get(url, stream=True) as r:
                        r.raise_for_status()
                        with open(file_path, "wb") as f:
                            for chunk in r.iter_content(chunk_size=8192):
                                f.write(chunk)
                    return True
                except Exception as e:
                    logging.debug(f"Attempt {attempt} failed: {e}")
                    if attempt >= max_retry:
                        return False
            return False

        @classmethod
        def save_to_doskey(name: str, command: str) -> bool:
            import subprocess

            """Windows에서 doskey로 alias 저장"""
            try:
                doskey_cmd = f'doskey {name}={command}'
                result = subprocess.run(doskey_cmd, shell=True, capture_output=True, text=True)
                return result.returncode == 0
            except Exception as e:
                logging.debug(f"Doskey 저장 실패: {e}")
                return False

        @classmethod
        def ensure_task_orchestrator_cli_root_directory(self):
            import os
            import sys
            from sources.functions.ensure_pwd_moved_to_d_task_orchestrator_cli import ensure_pwd_moved_to_d_task_orchestrator_cli

            if ensure_pwd_moved_to_d_task_orchestrator_cli():
                return True
            else:
                logging.debug(f"task_orchestrator_cli 루트 디렉토리를 찾을 수 없습니다.")
                logging.debug(f"️이 스크립트는 task_orchestrator_cli 루트 디렉토리에서 실행되어야 합니다.")
                logging.debug(f"️다음 중 하나의 방법으로 실행하세요:")
                logging.debug(f"1. task_orchestrator_cli 디렉토리로 이동 후 실행")
                logging.debug(f"2. Downloads/task_orchestrator_cli 디렉토리에서 실행")
                logging.debug(f"3. task_orchestrator_cli 루트 디렉토리에서 실행")

            try:
                response = input("계속 진행하시겠습니까? (y/N): ").strip().lower()
                if response in ['y', 'yes']:
                    logging.debug("️ 경고: 예상치 못한 오류가 발생할 수 있습니다.")
                    return True
                else:
                    logging.debug("스크립트를 중단합니다.")
                    sys.exit(1)
            except KeyboardInterrupt:
                logging.debug("사용자에 의해 중단되었습니다.")
                sys.exit(1)

        @classmethod
        def ensure_task_orchestrator_cli_installation_info_guided(self):
            import os
            import platform
            import sys

            logging.debug(PK_UNDERLINE)
            logging.debug(rf"{__file__} is started")
            logging.debug("task_orchestrator_cli installation Script started")
            logging.debug(f"Platform: {platform.system()}")
            logging.debug(f"Python version: {sys.version}")
            logging.debug(f"Current working directory: {os.getcwd()}")

        @classmethod
        def setup_pk_environment_with_aliases(self):
            import os

            """task_orchestrator_cli 환경변수 설정 및 내장 alias 로드"""
            try:
                # Path 객체로 환경변수 설정 (directories.py에서 가져온 경로들)
                from sources.objects.task_orchestrator_cli_directories import (
                    D_TASK_ORCHESTRATOR_CLI, D_TASK_ORCHESTRATOR_CLI_RESOURCES, D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES, D_TASK_ORCHESTRATOR_CLI_SENSITIVE,
                    D_PK_WORKING, D_PK_MEMO, D_BUSINESS_DEMO, D_DOWNLOADS, D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES
                )
                # Path 객체로 변환
                d_task_orchestrator_cli = Path(D_TASK_ORCHESTRATOR_CLI)
                d_resources = Path(D_TASK_ORCHESTRATOR_CLI_RESOURCES)
                d_system_resources = D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES
                d_task_orchestrator_cli_sensitive = D_TASK_ORCHESTRATOR_CLI_SENSITIVE
                d_pk_working = D_PK_WORKING
                d_pk_memo = Path(D_PK_MEMO)
                d_business_demo = Path(D_BUSINESS_DEMO)
                d_downloads = Path(D_DOWNLOADS)
                d_system_resources = D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES

                # d_userprofile = Path.home()
                # d_downloads = Path(rf"{d_userprofile}\Downloads")
                # d_task_orchestrator_cli = Path(rf"{d_downloads}\task_orchestrator_cli")
                # d_resources = Path(rf"{d_downloads}\task_orchestrator_cli\resources")
                # d_system_resources = Path(rf"{d_downloads}\task_orchestrator_cli\system_resources")
                # d_task_orchestrator_cli_sensitive = Path(rf"{d_downloads}\task_orchestrator_cli\task_orchestrator_cli_sensitive")
                # d_pk_working = Path(rf"{d_downloads}\pk_working")
                # d_pk_memo = Path(rf"{d_downloads}\pk_memo")
                # d_business_demo = Path(rf"{d_downloads}\business_demo")
                # d_system_resources = Path(rf"{d_downloads}\task_orchestrator_cli\system_resources")

                # OS별 virtual environment 경로 추가
                d_venv_windows = d_task_orchestrator_cli / ".venv_windows"
                d_venv_linux = d_task_orchestrator_cli / ".venv_linux"

                # 환경변수 설정 (Path 객체를 문자열로 변환)
                os.environ['D_TASK_ORCHESTRATOR_CLI'] = str(d_task_orchestrator_cli)
                os.environ['D_TASK_ORCHESTRATOR_CLI_RESOURCES'] = str(d_resources)
                os.environ['D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES'] = str(d_system_resources)
                os.environ['D_task_orchestrator_cli_sensitive'] = str(d_task_orchestrator_cli_sensitive)
                os.environ['D_PK_WORKING'] = str(d_pk_working)
                os.environ['D_PK_MEMO'] = str(d_pk_memo)
                os.environ['D_BUSINESS_DEMO'] = str(d_business_demo)
                os.environ['D_DOWNLOADS'] = str(d_downloads)
                os.environ['D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES'] = str(d_system_resources)

                # OS별 virtual environment 환경변수 설정
                os.environ['D_VENV_WINDOWS'] = str(d_venv_windows)
                os.environ['D_VENV_LINUX'] = str(d_venv_linux)

                # PYTHONPATH 설정
                current_pythonpath = os.environ.get('PYTHONPATH', '')
                if str(d_task_orchestrator_cli) not in current_pythonpath:
                    new_pythonpath = f"{d_task_orchestrator_cli};{current_pythonpath}" if current_pythonpath else str(d_task_orchestrator_cli)
                    os.environ['PYTHONPATH'] = new_pythonpath

                logging.debug("task_orchestrator_cli 환경변수 설정 완료 (OS별 virtual environment 포함)")
                return True

            except Exception as e:
                logging.debug(f"환경변수 설정 실패: {e}")
                return False

        @classmethod
        def ensure_task_orchestrator_cli_enabled(self):
            import sys
            import textwrap

            import os
            from sources.functions.ensure_windows_minimized import ensure_windows_minimized
            from sources.functions.is_os_linux import is_os_linux
            from sources.functions.is_os_windows import is_os_windows
            from sources.functions.is_os_wsl_linux import is_os_wsl_linux
            from sources.functions.ensure_task_orchestrator_cli_enabled_windows import WindowsManager
            from sources.functions.ensure_task_orchestrator_cli_enabled_linux import LinuxManager
            from sources.functions.ensure_command_executed import ensure_command_executed
            from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES





            self.ensure_task_orchestrator_cli_installation_info_guided()
            self.ensure_task_orchestrator_cli_root_directory()
            current_os = PkSystemManager.detect_os()
            current_os = current_os.strip()
            logging.debug(PK_UNDERLINE)
            logging.debug(f"task_orchestrator_cli Enabler (Refactored Version)")
            logging.debug(current_os)
            os.chdir(D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES)
            if is_os_windows():
                logging.debug(f"{current_os} is supported for task_orchestrator_cli")
                manager = WindowsManager()
                total_steps = 7
            elif is_os_wsl_linux() or is_os_linux():
                logging.debug(f"{current_os} is supported for task_orchestrator_cli")
                manager = LinuxManager()
                ensure_command_executed(cmd='bash system_resources/ensure_task_orchestrator_cli_enabled.sh')
                total_steps = 6
            else:
                logging.debug(f"{current_os} is not supported for task_orchestrator_cli")
                ensure_not_prepared_yet_guided()
                sys.exit(1)

            # Step 1: UV 설치
            PkSystemManager.print_step(1, total_steps, "Installing uv")
            if not manager.install_uv():
                logging.debug(f"UV 설치 실패 설치를 중단합니다.")
                sys.exit(1)

            # Step 2: FZF 설치
            PkSystemManager.print_step(2, total_steps, "Installing fzf")
            if not manager.install_fzf():
                logging.debug(f"FZF 설치 실패 설치를 중단합니다.")
                sys.exit(1)

            # Step 3: PATH 설정
            PkSystemManager.print_step(3, total_steps, "Setting up PATH")
            if not manager.setup_path():
                logging.debug(f"PATH 설정 실패 설치를 중단합니다.")
                sys.exit(1)

            # Step 4: 별칭 설정
            PkSystemManager.print_step(4, total_steps, "Setting up aliases")
            if not manager.setup_aliases():
                logging.debug(f"별칭 설정 실패 설치를 중단합니다.")
                sys.exit(1)

            # Step 5: UV 패키지 동기화 (OS별 virtual environment 자동 설정)
            PkSystemManager.print_step(5, total_steps, "Syncing uv packages with OS-specific venv")
            logging.debug(f"OS별 virtual environment 설정:")
            if is_os_windows():
                logging.debug(f"Windows: .venv_windows 디렉토리 사용")
                logging.debug(f"uv sync --active 명령어로 의존성 설치")
            elif is_os_wsl_linux() or is_os_linux():
                logging.debug(f"Linux/WSL: .venv_linux 디렉토리 사용")
                logging.debug(f"uv sync --active 명령어로 의존성 설치")

            if not manager.sync_uv_packages():
                logging.debug(f"UV 패키지 동기화 실패 설치를 중단합니다.")
                sys.exit(1)

            # Step 6: virtual environment 패키지 설치 및 테스트
            PkSystemManager.print_step(6, total_steps, "Installing and testing venv packages")
            if not manager.install_packages_with_venv_python():
                logging.debug(f"virtual environment 패키지 설치 실패 설치를 중단합니다.")
                sys.exit(1)

            if not manager.test_venv_python():
                logging.debug(f"virtual environment Python 테스트 실패 설치를 중단합니다.")
                sys.exit(1)

            # Step 7: task_orchestrator_cli shortcut guide (선택적)
            try:
                PkSystemManager.print_step(7, total_steps, "task_orchestrator_cli shortcut guided")

                # 필요한 파일/함수들이 있는 경우에만 실행
                if 'F_TASK_ORCHESTRATOR_CLI_LAUNCHER_LNK' in globals():
                    ensure_pnxs_move_to_recycle_bin(
                        pnxs=[F_TASK_ORCHESTRATOR_CLI_LAUNCHER_LNK, str(F_TASK_ORCHESTRATOR_CLI_LAUNCHER_LNK).removesuffix(".lnk")])

                # PYTHONPATH 설정
                ensure_command_executed(rf"setx PYTHONPATH %USERPROFILE%\Downloads\task_orchestrator_cli")

                # 배치 파일 생성 (필요한 변수들이 있는 경우에만)
                if all(var in globals() for var in ['F_ENSURE_TASK_ORCHESTRATOR_CLI_LNK_RAN_BAT', 'F_TASK_ORCHESTRATOR_CLI_RESOURCESTHON', 'D_TASK_ORCHESTRATOR_CLI_RESOURCES']):
                    # get_nx 함수가 있는지 확인
                    try:
                        from sources.functions.get_nx import get_nx
                        title_name = get_nx(F_ENSURE_TASK_ORCHESTRATOR_CLI_LNK_RAN_BAT)
                    except ImportError:
                        title_name = "task_orchestrator_cli Launcher"

                    batch_content = textwrap.dedent(f'''
                       @echo off
                       title {title_name}
                       chcp 65001 >NUL
                       {F_VENV_PYTHON_EXE} {F_PK_ENSURE_TASK_ORCHESTRATOR_CLI_STARTED_PY}
                   ''').lstrip()
                    ensure_embeded_script_created(script_file=F_ENSURE_TASK_ORCHESTRATOR_CLI_LNK_RAN_BAT,
                                                  script_content=batch_content)

                # 윈도우 관리 (선택적)
                ensure_windows_minimized()

                if 'F_ENSURE_TASK_ORCHESTRATOR_CLI_LNK_PINNED_PS1' in globals():
                    # PowerShell 스크립트를 새 창에서 실행하고 유지
                    try:
                        ps_cmd = f'start "" powershell -NoExit -ExecutionPolicy Bypass -File "{F_ENSURE_TASK_ORCHESTRATOR_CLI_LNK_PINNED_PS1}"'
                        ensure_command_executed(ps_cmd)
                        logging.debug(f"PowerShell 스크립트 실행됨: {F_ENSURE_TASK_ORCHESTRATOR_CLI_LNK_PINNED_PS1}")
                    except Exception as e:
                        logging.debug(f"⚠️ PowerShell 스크립트 실행 실패: {e}")
                        logging.debug(f"⚠️ 수동으로 실행하세요: powershell -ExecutionPolicy Bypass -File {F_ENSURE_TASK_ORCHESTRATOR_CLI_LNK_PINNED_PS1}")

                # get_nx 함수 안전하게 호출
                try:
                    from sources.functions.get_nx import get_nx
                    window_title = get_nx(__file__)
                except ImportError:
                    window_title = "task_orchestrator_cli"

                ensure_window_to_front(window_title)

            except Exception as e:
                logging.debug(f"Step 7 (shortcut guide) 건너뜀: {e}")
                logging.debug("기본 기능만 계속 진행합니다.")

            logging.debug("task_orchestrator_cli installed successfully!")

            if is_os_wsl_linux() or is_os_linux():
                logging.debug("변경사항을 적용하려면 새 터미널을 열거나 다음 명령어를 실행하세요:")
                logging.debug("source ~/.bashrc")



except ImportError as e:
    logging.debug(f"일부 모듈을 찾을 수 없음: {e}")
    logging.debug("기본 기능만 사용 가능합니다.")


def ensure_task_orchestrator_cli_enabled():
    from sources.functions.ensure_pwd_moved_to_d_task_orchestrator_cli import ensure_pwd_moved_to_d_task_orchestrator_cli
    import logging

    if not ensure_pwd_moved_to_d_task_orchestrator_cli():
        logging.debug("task_orchestrator_cli 루트 디렉토리로 이동 할 수 없었었습니다")
    else:
        logging.debug("task_orchestrator_cli 루트 디렉토리로 이동되었습니다")
        PkSystemManager.ensure_task_orchestrator_cli_enabled()


if __name__ == "__main__":
    # install.cmd 는 여기를 타지 않음.
    try:
        PkSystemManager.ensure_task_orchestrator_cli_enabled()
    except Exception as e:
        logging.debug(f"=== Error occurred: {e} ===")
        import traceback
        import sys
        import time

        traceback.print_exc()
        time.sleep(100)
