import logging

try:
    from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
except ImportError as e:
    import platform

    logging.debug(f"모듈을 찾을 수 없음: {e}")
    logging.debug("Windows 환경에서 안전한 색상 코드 사용합니다")
    if platform.system().lower() == "windows":
        try:
            import colorama

            colorama.init(autoreset=True, convert=True)
            TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP = {
                'GREEN': '\033[32m', 'RED': '\033[31m', 'YELLOW': '\033[33m',
                'BLUE': '\033[34m', 'MAGENTA': '\033[35m', 'CYAN': '\033[36m',
                'RESET': '\033[0m'
            }
        except (ImportError, Exception):
            # colorama 실패 시 색상 없이
            TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP = {
                'GREEN': '', 'RED': '', 'YELLOW': '', 'BLUE': '',
                'MAGENTA': '', 'CYAN': '', 'RESET': ''
            }
    else:
        # Linux/Mac에서는 기본 ANSI 색상 코드
        TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP = {
            'GREEN': '\033[32m', 'RED': '\033[31m', 'YELLOW': '\033[33m',
            'BLUE': '\033[34m', 'MAGENTA': '\033[35m', 'CYAN': '\033[36m',
            'RESET': '\033[0m'
        }
try:
    from sources.objects.task_orchestrator_cli_directories import *
    from sources.objects.task_orchestrator_cli_files import *
    from sources.objects.task_orchestrator_cli_urls import URL_FZF_API, URL_CHATGPT_PK_WORKING
except ImportError as e:
    import os

    logging.debug(f"모듈을 찾을 수 없음: {e}")
    logging.debug("기본 경로를 사용합니다.")

    # 기본 경로 설정 (USERPROFILE 동적 사용)

    userprofile = os.environ.get('USERPROFILE', os.path.expanduser('~'))

    D_TASK_ORCHESTRATOR_CLI = Path(userprofile) / "Downloads" / "task_orchestrator_cli"
    D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES = Path(userprofile) / "Downloads" / "task_orchestrator_cli" / "system_resources"
    D_TASK_ORCHESTRATOR_CLI_RESOURCES = Path(userprofile) / "Downloads" / "task_orchestrator_cli" / "resources"
    D_TASK_ORCHESTRATOR_CLI_SENSITIVE = Path(userprofile) / "Downloads" / "task_orchestrator_cli" / "task_orchestrator_cli_sensitive"
    D_PK_WORKING = Path(userprofile) / "Downloads" / "pk_working"
    D_PK_MEMO = Path(userprofile) / "Downloads" / "pk_memo"
    D_BUSINESS_DEMO = Path(userprofile) / "Downloads" / "business_demo"
    D_DOWNLOADS = Path(userprofile) / "Downloads"

    # 기본 파일 경로
    F_UV = None
    F_FZF = None
    F_UV_ZIP = None
    F_FZF_ZIP = None
    F_VSCODE = None
    F_CURSOR = None
    F_CLAUDE = None
    F_PYCHARM = None

    # 기본 URL
    URL_FZF_API = "https://api.github.com/repos/junegunn/fzf/releases/latest"
    URL_CHATGPT_PK_WORKING = "https://chat.openai.com"

if platform.system().lower() == "windows":
    import winreg

print = None
PkTextsFallBack = type('PkTexts', (), {
    'VENV_PYTHON_TEST': 'virtual environment Python 테스트',
    'VENV_PYTHON_NOT_FOUND': 'virtual environment Python을 찾을 수 없음',
    'VENV_PYTHON_VERSION': 'virtual environment Python 버전',
    'VENV_MODULE_TEST': '모듈 사용 가능',
    'VENV_TEST_SUCCESS': '테스트 성공',
    'UV_INSTALLATION': 'UV 설치',
    'PERMISSION_ERROR': '권한 오류',
    'BACKUP_CREATED': '백업 생성됨',
    'BACKUP_FAILED': '백업 실패',
    'FILE_NOT_FOUND': '파일을 찾을 수 없음',
    'DIRECTORY_CREATED': '디렉토리 생성됨',
    'DIRECTORY_CREATION_FAILED': '디렉토리 생성 실패',
    'FILE_COPY_SUCCESS': '파일 복사 성공',
    'FILE_COPY_FAILED': '파일 복사 실패',
    'ALTERNATIVE_INSTALLATION': '대안 설치',
    'TEMP_CLEANUP_FAILED': '임시 파일 정리 실패',
    'INSTALLATION_SUCCESS': '설치 완료',
    'INSTALLATION_FAILED': '설치 실패',
    'PATH_SETUP': 'Windows PATH 설정',
    'ALIAS_SETUP': 'Windows 별칭 설정',
    'REGISTRY_SETUP_SUCCESS': '레지스트리 설정 완료',
    'REGISTRY_SETUP_FAILED': '레지스트리 설정 실패',
    'WINDOWS_REGISTRY_SETUP_SUCCESS': 'Windows 레지스트리 설정 완료',
    'WINDOWS_REGISTRY_SETUP_FAILED': 'Windows 레지스트리 설정 실패',
    'PACKAGE_SYNC': 'uv 패키지 동기화',
    'VENV_SETUP': 'virtual environment Python으로 패키지 설치',
    'VENV_PYTHON_FOUND': 'virtual environment Python 사용',
    'PACKAGE_INSTALLING': '설치 중',
    'PACKAGE_INSTALL_SUCCESS': '설치 완료',
    'PACKAGE_INSTALL_FAILED': '설치 실패',
    'PACKAGE_INSTALL_ERROR': '설치 오류',
    'VENV_PACKAGE_INSTALL_COMPLETE': 'virtual environment 패키지 설치 완료',
    'FZF_INSTALLATION': 'FZF 설치',
    'OPERATION_SUCCESS': '동기화 완료',
    'OPERATION_FAILED': '동기화 실패',
    'VENV_TEST_FAILED': '테스트 실패'
})()
# Lazy import to avoid circular dependency
try:
    import logging
    from sources.objects.pk_map_texts import PkTexts

    print = logging.debug
except ImportError:
    import builtins

    print = builtins.print
    PkTexts = PkTextsFallBack


class WindowsManager():
    """Windows 플랫폼 관리자"""

    def __init__(self):
        from sources.functions.ensure_pnxs_move_to_recycle_bin import ensure_pnxs_move_to_recycle_bin
        import platform
        from pathlib import Path

        if platform.system().lower() == "windows":
            import winreg
            self.winreg = winreg

        self.d_userprofile = Path.home()

        # 경로 설정 (import 실패 시 대비)
        try:
            self.d_task_orchestrator_cli = Path(D_TASK_ORCHESTRATOR_CLI)
            self.d_business_demo = Path(D_BUSINESS_DEMO)
            self.d_resources = Path(D_TASK_ORCHESTRATOR_CLI_RESOURCES)
            self.d_system_resources = D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES
            self.d_task_orchestrator_cli_sensitive = D_TASK_ORCHESTRATOR_CLI_SENSITIVE
            self.d_pk_working = D_PK_WORKING
            self.d_pk_memo = Path(D_PK_MEMO)
            self.d_downloads = Path(D_DOWNLOADS)
            self.d_system_resources = D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES
        except NameError:
            # 기본 경로 사용
            self.d_task_orchestrator_cli = Path.home() / "Downloads" / "task_orchestrator_cli"
            self.d_business_demo = Path.home() / "Downloads" / "business_demo"
            self.d_resources = self.d_task_orchestrator_cli / "resources"
            self.d_system_resources = self.d_task_orchestrator_cli / "system_resources"
            self.d_task_orchestrator_cli_sensitive = self.d_task_orchestrator_cli / "task_orchestrator_cli_sensitive"
            self.d_pk_working = Path.home() / "Downloads" / "pk_working"
            self.d_pk_memo = Path.home() / "Downloads" / "pk_memo"
            self.d_downloads = Path.home() / "Downloads"
            self.d_system_resources = self.d_task_orchestrator_cli / "system_resources"

        # 현재 사용자 경로로 동적 설정 (하드코딩된 경로 대신)
        if not self.d_task_orchestrator_cli.exists():
            # 기본 경로가 존재하지 않으면 현재 사용자 경로 사용
            self.d_task_orchestrator_cli = Path.home() / "Downloads" / "task_orchestrator_cli"
            self.d_resources = self.d_task_orchestrator_cli / "resources"
            self.d_system_resources = self.d_task_orchestrator_cli / "system_resources"
            self.d_task_orchestrator_cli_sensitive = self.d_task_orchestrator_cli / "task_orchestrator_cli_sensitive"
            self.d_system_resources = self.d_task_orchestrator_cli / "system_resources"

        self.d_pk_recycle_bin = self.d_task_orchestrator_cli_sensitive
        # Windows 전용 virtual environment 경로 사용
        self.d_venv_scripts = self.d_task_orchestrator_cli / ".venv_windows" / "Scripts"

        self.f_venv_python_windows = self.d_venv_scripts / "python.exe"
        self.f_uv_exe = Path(F_UV_EXE) if F_UV_EXE else self.d_system_resources / "uv.exe"
        self.f_fzf_exe = F_FZF if F_FZF else self.d_system_resources / "fzf.exe"
        self.f_uv_zip = F_UV_ZIP if F_UV_ZIP else self.d_downloads / "uv.zip"
        self.f_fzf_zip = Path(F_FZF_ZIP) if F_FZF_ZIP else self.d_downloads / "fzf.zip"

        self.f_ensure_pk_alias_enabled_cmd = F_ENSURE_PK_ALIAS_ENABLED_BAT
        self.f_ensure_task_orchestrator_cli_lnk_executed_bat = D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES / "ensure_task_orchestrator_cli_lnk_executed.bat"

        ensure_pnxs_move_to_recycle_bin(pnxs=[
            self.f_ensure_pk_alias_enabled_cmd,
            # self.f_ensure_task_orchestrator_cli_lnk_executed_bat, # 추후 lnk 재생성할거면
        ])

    def install_uv(self, max_retry: int = 2) -> bool:
        import subprocess
        import tempfile
        import time
        import uuid
        import zipfile
        from pathlib import Path

        """UV 설치 (Windows)"""
        import shutil
        try:
            logging.debug(f"UV 설치 (Windows)")
            # 디렉토리 생성 권한 확인
            if not self._check_windows_permissions():
                logging.debug(f"️ 권한 오류: {self.d_system_resources}")
                return False

            # 기존 파일 백업
            if self.f_uv_exe.exists():
                try:
                    backup_path = self.f_uv_exe.with_suffix('.exe.backup')
                    self.f_uv_exe.rename(backup_path)
                    logging.debug(f"[성공] 백업 생성됨: {backup_path}")
                except PermissionError:
                    logging.debug(f"⚠️ 파일이 사용 중입니다. 강제 삭제 시도...")
                    try:
                        # 파일이 사용 중일 때 강제 삭제
                        import time
                        time.sleep(1)  # 잠시 대기
                        self.f_uv_exe.unlink()
                        logging.debug(f"[성공] 기존 파일 삭제됨")
                    except Exception as e2:
                        logging.debug(f"[오류] 강제 삭제 실패: {e2}")
                        # 대안 위치에 설치
                        alternative_path = Path.home() / "uv.exe"
                        self.f_uv_exe = alternative_path
                        logging.debug(f"⚠️ 대안 위치 사용: {alternative_path}")
                except FileExistsError:
                    logging.debug(f"⚠️ 백업 파일이 이미 존재합니다. 기존 백업 파일 제거 후 재시도...")
                    try:
                        # 기존 백업 파일 제거
                        backup_path = self.f_uv_exe.with_suffix('.exe.backup')
                        if backup_path.exists():
                            backup_path.unlink()
                            logging.debug(f"[성공] 기존 백업 파일 제거됨")

                        # 다시 백업 시도
                        backup_path = self.f_uv_exe.with_suffix('.exe.backup')
                        self.f_uv_exe.rename(backup_path)
                        logging.debug(f"[성공] 백업 생성됨: {backup_path}")
                    except Exception as e2:
                        logging.debug(f"⚠️ 백업 재시도 실패: {e2}")
                        # 백업 없이 기존 파일 삭제
                        try:
                            self.f_uv_exe.unlink()
                            logging.debug(f"[성공] 기존 파일 삭제됨")
                        except Exception as e3:
                            logging.debug(f"[오류] 파일 삭제 실패: {e3}")
                            # 대안 위치에 설치
                            alternative_path = Path.home() / "uv.exe"
                            self.f_uv_exe = alternative_path
                            logging.debug(f"⚠️ 대안 위치 사용: {alternative_path}")
                except Exception as e:
                    logging.debug(f"⚠️ 백업 실패: {e}")
                    try:
                        self.f_uv_exe.unlink()
                        logging.debug(f"[성공] 기존 파일 삭제됨")
                    except Exception as e2:
                        logging.debug(f"[오류] 파일 삭제 실패: {e2}")
                        # 대안 위치에 설치
                        alternative_path = Path.home() / "uv.exe"
                        self.f_uv_exe = alternative_path
                        logging.debug(f"⚠️ 대안 위치 사용: {alternative_path}")

            # UV 다운로드 및 설치
            for attempt in range(max_retry):
                try:
                    logging.debug(            f" [Attempt {attempt + 1}] Downloading from https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip")

                    # 임시 디렉토리 생성
                    temp_dir = Path(tempfile.gettempdir()) / f"uv_install_{uuid.uuid4().hex[:8]}"
                    temp_dir.mkdir(exist_ok=True)

                    # UV 다운로드
                    uv_zip_path = temp_dir / "uv.zip"
                    import requests
                    response = requests.get(
                        "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip",
                        timeout=30)
                    response.raise_for_status()

                    with open(uv_zip_path, 'wb') as f:
                        f.write(response.content)

                    # 압축 해제
                    logging.debug("Extracting uv.zip...")
                    with zipfile.ZipFile(uv_zip_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)

                    # UV 실행 파일 복사
                    uv_exe_src = temp_dir / "uv.exe"
                    if uv_exe_src.exists():
                        try:
                            shutil.copy2(uv_exe_src, self.f_uv_exe)
                            logging.debug(f"파일 복사 성공: {self.f_uv_exe}")
                        except PermissionError:
                            # 대안 위치에 설치
                            alternative_path = Path.home() / "uv.exe"
                            shutil.copy2(uv_exe_src, alternative_path)
                            self.f_uv_exe = alternative_path
                            logging.debug(f"대안 설치: {alternative_path}")
                        except Exception as e:
                            logging.debug(f"파일 복사 실패: {e}")
                            return False
                    else:
                        logging.debug(f"uv.exe in extracted files")
                        return False

                    # 임시 디렉토리 정리
                    try:
                        shutil.rmtree(temp_dir)
                    except Exception as e:
                        logging.debug(f"️ 임시 파일 정리 실패: {e}")

                    # 설치 확인
                    result = subprocess.run([str(self.f_uv_exe), "--version"], capture_output=True, text=True)
                    if result.returncode == 0:
                        logging.debug(f"설치 완료: {result.stdout.strip()}")
                        return True
                    else:
                        logging.debug(f"설치 실패: {result.stderr}")

                except Exception as e:
                    logging.debug(f"설치 실패: {e}")
                    if attempt < max_retry - 1:
                        time.sleep(2)
                        continue
                    else:
                        return False

            return False

        except Exception as e:
            logging.debug(f"설치 실패: {e}")
            return False

    def _check_windows_permissions(self) -> bool:

        # TBD : 이부분 로직적으로 불필요하면 제거하고, ensure_task_orchestrator_cli_enabled_admin.cmd 파일로직도 불필요 판단 시 , 제거
        """Windows 권한 확인 및 안내"""
        from sources.objects.pk_map_colors import TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP
        try:
            # 테스트 파일 생성 시도
            test_file = self.d_system_resources / "test_permission.tmp"
            test_file.write_text("test")
            test_file.unlink()
            return True
        except PermissionError:
            logging.debug(f"️ 권한 문제 발견: {TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['YELLOW']}상태=권한문제 {TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}")
            logging.debug("해결 방법:")
            logging.debug("1. 관리자 권한으로 실행:")
            logging.debug(rf"      {self.d_system_resources}\ensure_task_orchestrator_cli_enabled_admin.cmd")
            logging.debug("2. 또는 PowerShell을 관리자 권한으로 실행 후:")
            logging.debug(f"cd {self.d_task_orchestrator_cli}")
            logging.debug(rf"      python sources\wrappers\functions\ensure_task_orchestrator_cli_enabled.py")
            logging.debug("3. 또는 명령 프롬프트를 관리자 권한으로 실행 후:")
            logging.debug(f"cd {self.d_task_orchestrator_cli}")
            logging.debug(rf"      python sources\wrappers\functions\ensure_task_orchestrator_cli_enabled.py")
            logging.debug("4. 대안 위치 사용 (자동으로 시도됨):")
            from sources.objects.task_orchestrator_cli_directories import D_DOWNLOADS
            logging.debug(rf"      {D_DOWNLOADS}")
            return False
        except Exception as e:
            logging.debug(f"️ 권한 확인 오류: {TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RED']}오류={e} {TASK_ORCHESTRATOR_CLI_ANSI_COLOR_MAP['RESET']}")
            return False

    def install_fzf(self, max_retry: int = 2) -> bool:
        import subprocess
        import tempfile
        import time
        import uuid
        import zipfile
        from pathlib import Path

        """FZF 설치 (Windows)"""
        try:
            logging.debug(f"FZF 설치 (Windows)")

            # 권한 확인
            if not self._check_windows_permissions():
                logging.debug(f"️ 권한 오류: {self.d_system_resources}")
                return False

            # 최신 FZF URL 가져오기
            fzf_url = self._get_latest_fzf_url_windows()
            logging.debug("FZF 최신 버전 확인 중...")
            logging.debug(f"FZF 최신 버전: {fzf_url.split('/')[-1].replace('fzf-', '').replace('-windows_amd64.zip', '')}")
            logging.debug(f"FZF 다운로드 URL: {fzf_url}")

            # 기존 파일 백업
            if self.f_fzf_exe.exists():
                try:
                    backup_path = self.f_fzf_exe.with_suffix('.exe.backup')
                    self.f_fzf_exe.rename(backup_path)
                    logging.debug(f"백업 생성됨: {self.f_fzf_exe}")
                except Exception as e:
                    logging.debug(f"️ 백업 실패: {self.f_fzf_exe}")
                    try:
                        self.f_fzf_exe.unlink()
                    except Exception as e2:
                        logging.debug(f"️ 백업 실패: {e2}")

            # FZF 다운로드 및 설치
            for attempt in range(max_retry):
                try:
                    logging.debug(f"[Attempt {attempt + 1}] Downloading fzf from {fzf_url}")
                    logging.debug(f"[Attempt {attempt + 1}] Downloading from {fzf_url}")

                    # 임시 디렉토리 생성
                    temp_dir = Path(tempfile.gettempdir()) / f"fzf_install_{uuid.uuid4().hex[:8]}"
                    temp_dir.mkdir(exist_ok=True)

                    # FZF 다운로드
                    fzf_zip_path = temp_dir / "fzf.zip"
                    import requests
                    response = requests.get(fzf_url, timeout=30)
                    response.raise_for_status()

                    with open(fzf_zip_path, 'wb') as f:
                        f.write(response.content)

                    # 압축 해제
                    logging.debug("Extracting fzf.zip...")
                    with zipfile.ZipFile(fzf_zip_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)

                    # FZF 실행 파일 복사
                    fzf_exe_src = temp_dir / "fzf.exe"
                    if fzf_exe_src.exists():
                        try:
                            import shutil
                            shutil.copy2(fzf_exe_src, self.f_fzf_exe)
                            logging.debug(f"파일 복사 성공: {self.f_fzf_exe}")
                        except PermissionError:
                            # 대안 위치에 설치
                            alternative_path = Path.home() / "fzf.exe"
                            shutil.copy2(fzf_exe_src, alternative_path)
                            self.f_fzf_exe = alternative_path
                            logging.debug(f"대안 설치: {alternative_path}")
                        except Exception as e:
                            logging.debug(f"파일 복사 실패: {e}")
                            return False
                    else:
                        logging.debug(f"fzf.exe in extracted files")
                        return False

                    # 임시 디렉토리 정리
                    try:
                        shutil.rmtree(temp_dir)
                    except Exception as e:
                        logging.debug(f"️ 임시 파일 정리 실패: {e}")

                    # 설치 확인
                    result = subprocess.run([str(self.f_fzf_exe), "--version"], capture_output=True, text=True)
                    if result.returncode == 0:
                        logging.debug(f"설치 완료: {result.stdout.strip()}")
                        return True
                    else:
                        logging.debug(f"설치 실패: {result.stderr}")

                except Exception as e:
                    logging.debug(f"설치 실패: {e}")
                    if attempt < max_retry - 1:
                        time.sleep(2)
                        continue
                    else:
                        return False

            return False

        except Exception as e:
            logging.debug(f"설치 실패: {e}")
            return False

    def _get_latest_fzf_url_windows(self) -> str:

        """GitHub API를 사용하여 최신 FZF 다운로드 URL 가져오기 (Windows)"""
        try:
            logging.debug("FZF 최신 버전 확인 중...")
            import requests
            response = requests.get(URL_FZF_API)
            response.raise_for_status()
            data = response.json()
            version = data["tag_name"]
            logging.debug(f"FZF 최신 버전: {version}")

            version_clean = version.lstrip('v')
            download_url = f"https://github.com/junegunn/fzf/releases/download/{version}/fzf-{version_clean}-windows_amd64.zip"
            logging.debug(f"FZF 다운로드 URL: {download_url}")

            return download_url

        except Exception as e:
            fallback_url = "https://github.com/junegunn/fzf/releases/download/v0.65.0/fzf-0.65.0-windows_amd64.zip"
            logging.debug(f"Fallback URL 사용: {fallback_url}")
            return fallback_url

    def setup_path(self) -> bool:
        """Windows PATH 설정"""
        try:

            logging.debug(f"{PkTexts.PATH_SETUP}")

            # 새로운 PATH 구성
            new_path = self._build_windows_path()

            # PYTHONPATH 환경변수 설정
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
                winreg.SetValueEx(key, "PYTHONPATH", 0, winreg.REG_EXPAND_SZ, str(self.d_task_orchestrator_cli))
                winreg.CloseKey(key)
                logging.debug(f"PYTHONPATH 설정 완료: {self.d_task_orchestrator_cli}")
            except Exception as e:
                logging.debug(f"PYTHONPATH 설정 실패: {e}")

            # 시스템 PATH 업데이트
            try:

                # 사용자 PATH 업데이트
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
                winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)
                winreg.CloseKey(key)

                # 환경변수 변경 알림
                self._broadcast_environment_change()

                logging.debug(f"{PkTexts.OPERATION_SUCCESS}")
                return True

            except Exception as e:
                logging.debug(f"{PkTexts.OPERATION_FAILED} {e}")
                return False

        except Exception as e:
            logging.debug(f"{PkTexts.OPERATION_FAILED} {e}")
            return False

    def _build_windows_path(self) -> str:
        import os

        """Windows PATH 구성"""
        system_path = self._get_system_path()
        user_path = self._get_user_path()

        all_paths = system_path + ";" + user_path if user_path else system_path
        path_list = all_paths.split(";")

        # 중복 제거 및 정리
        seen = set()
        clean_path = []

        # 우선순위 경로 추가 (OS별 virtual environment 포함)
        priority_paths = [
            (self.d_system_resources, "UV/FZF 경로"),
            (self.d_venv_scripts, "Windows virtual environment Scripts 경로"),
            (self.d_resources, "PK_PY 경로"),
            (self.d_business_demo, "Business Demo 경로"),
            (self.d_task_orchestrator_cli / ".venv_windows" / "Scripts", "Windows virtual environment Scripts 경로"),
            (self.d_task_orchestrator_cli / ".venv_linux" / "bin", "Linux virtual environment bin 경로")
        ]

        for path, description in priority_paths:
            if path.exists():
                norm_path = str(path.resolve())
                if norm_path not in seen:
                    seen.add(norm_path)
                    clean_path.append(norm_path)
                    logging.debug(f"{description} 추가: {norm_path}")

        # 나머지 경로 추가
        for path in path_list:
            norm = os.path.normpath(path.strip())
            if not norm or norm in seen:
                continue
            if "user" in norm.lower() and "task_orchestrator_cli" not in norm.lower():
                continue
            seen.add(norm)
            clean_path.append(norm)

        return ";".join(clean_path)

    def _get_system_path(self) -> str:
        """시스템 환경변수 PATH 가져오기"""
        try:
            with self.winreg.OpenKey(self.winreg.HKEY_LOCAL_MACHINE,
                                     r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
                                     0, self.winreg.KEY_READ) as key:
                try:
                    system_path, _ = self.winreg.QueryValueEx(key, "Path")
                    return system_path
                except FileNotFoundError:
                    return ""
        except Exception:
            return ""

    def _get_user_path(self) -> str:
        """사용자 환경변수 PATH 가져오기"""
        try:
            with self.winreg.OpenKey(self.winreg.HKEY_CURRENT_USER, "Environment", 0, self.winreg.KEY_READ) as key:
                try:
                    user_path, _ = self.winreg.QueryValueEx(key, "Path")
                    return user_path
                except FileNotFoundError:
                    return ""
        except Exception:
            return ""

    def _broadcast_environment_change(self) -> None:
        """환경변수 변경을 시스템에 알림"""
        try:
            import ctypes
            HWND_BROADCAST = 0xFFFF
            WM_SETTINGCHANGE = 0x001A
            SMTO_ABORTIFHUNG = 0x0002
            result = ctypes.windll.user32.SendMessageTimeoutW(
                HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment",
                SMTO_ABORTIFHUNG, 5000, ctypes.byref(ctypes.c_ulong())
            )
            if result:
                logging.debug("환경변수 변경 알림이 전송되었습니다.")
            else:
                logging.debug("환경변수 변경 알림 전송 실패")
        except Exception as e:
            logging.debug(f"환경변수 변경 알림 실패: {e}")

    def setup_aliases(self) -> bool:
        """Windows 별칭 설정"""
        try:
            logging.debug(f"{PkTexts.ALIAS_SETUP}")
            self.create_f_pk_alias_bat()
            self.execute_f_pk_alias_bat()
            self.regist_autorun()
            logging.debug(f"{PkTexts.OPERATION_SUCCESS}")
            return True

        except Exception as e:
            logging.debug(f"{PkTexts.OPERATION_FAILED} {e}")
            return False

    def create_f_pk_alias_bat(self):
        """배치 파일 생성 및 실행"""
        try:
            import textwrap
            f_pk_alias_bat = F_ENSURE_PK_ALIAS_ENABLED_BAT
            batch_content = textwrap.dedent(f'''
                @echo off
                chcp 65001 >NUL

                doskey 1=cd "{D_DOWNLOADS}"
                doskey 2=cd "{D_TASK_ORCHESTRATOR_CLI}"
                doskey 3=cd "{D_PK_MEMO}"
                doskey 4=cd "{D_PK_WORKING}"
                doskey 5=cd "{D_BUSINESS_DEMO}"
                doskey 6=cd "{D_TASK_ORCHESTRATOR_CLI_RESOURCES}"
                doskey 7=cd "{D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES}"
                doskey 9=cd "{D_DESKTOP}"
                doskey 0=cd "{D_PK_RECYCLE_BIN}"
                
                doskey pk=python "{F_PK_ENSURE_TASK_ORCHESTRATOR_CLI_STARTED_PY}"
                doskey pk--fix=python "{F_PK_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_PY}"

                doskey venv="{F_VENV_ACTIVATE_BAT}"
                doskey code="{F_VSCODE_LNK}" $*
                doskey cursor="{F_CURSOR_LNK}" $*
                doskey claude="{F_CLAUDE_LNK}" $*
                doskey pycharm=start "" "{F_PYCHARM64_EXE}" $*
                doskey ps=powershell
                doskey psa=powershell -Command "Start-Process powershell -Verb RunAs"
                doskey cmda=start "" "{F_ENSURE_CMD_EXE_RAN_AS_ADMIN}"
                doskey gpt=start {URL_CHATGPT_PK_WORKING}
            
                doskey reboot=shutdown /r /t 0
                doskey poweroff=shutdown /s /t 0
                doskey shutdown=shutdown /s /t 0
                doskey logout=logoff
            
                doskey wsld=wsl --distribution Ubuntu
                doskey wsl24=wsl --distribution Ubuntu-24.04
                doskey wsl20=wsl --distribution Ubuntu-20.04
                doskey wsl18=wsl --distribution Ubuntu-18.04
            
                doskey ls=dir /b
                doskey cat=type $*
                doskey which=where $*
                doskey pwd=cd $*
                doskey history=doskey /history
        
                doskey x=exit
                doskey .=explorer.exe .
            ''').lstrip()
            # TODO : 삭제 명령 python 처리도 괜찮음 doskey rm=  ensure_pnxs_moved_to_recycle_bin
            #                 doskey ff=dir /s /b | fzf | clip
            #                 doskey fd=dir /s /b /ad | fzf | clip
            #                 doskey fe=explorer.exe <fzf | clip
            #                 doskey fcd=cd (fzf | clip)
            #                 doskey fc=fzf | clip     # python ensure_fc_enaabled.py
            #                 doskey rm=          # python ensure_pnx_moved_to_recycle_bin .py
            f_pk_alias_bat.parent.mkdir(parents=True, exist_ok=True)
            with open(f_pk_alias_bat, 'w', encoding='utf-8') as f:
                f.write(batch_content)
            if f_pk_alias_bat.exists():
                logging.debug(f'''{f_pk_alias_bat} 생성완료 {'%%%FOO%%%' if LTA else ''}''')
                return f_pk_alias_bat
            else:
                logging.debug(f'''{f_pk_alias_bat} 생성실패 {'%%%FOO%%%' if LTA else ''}''')
                raise

        except Exception as e:
            logging.debug(f"파일 생성/실행 실패: {e}")
            raise

    #         def setup_pk_environment():
    #             """task_orchestrator_cli 환경변수 설정 및 내장 alias 로드"""
    #             try:

    # # d_userprofile = Path.home()
    # # d_downloads = Path(rf"{d_userprofile}\Downloads")
    # # d_task_orchestrator_cli = Path(rf"{d_downloads}\task_orchestrator_cli")
    # # d_resources = Path(rf"{d_downloads}\task_orchestrator_cli\resources")
    # # d_system_resources = Path(rf"{d_downloads}\task_orchestrator_cli\system_resources")
    # # d_task_orchestrator_cli_sensitive = Path(rf"{d_downloads}\task_orchestrator_cli\task_orchestrator_cli_sensitive")
    # # d_pk_working = Path(rf"{d_downloads}\pk_working")
    # # d_pk_memo = Path(rf"{d_downloads}\pk_memo")
    # # d_business_demo = Path(rf"{d_downloads}\business_demo")
    # # d_system_resources = Path(rf"{d_downloads}\task_orchestrator_cli\system_resources")

    # # 환경변수 설정 (Path 객체를 문자열로 변환)
    # os.environ['D_TASK_ORCHESTRATOR_CLI'] = str(d_task_orchestrator_cli)
    # os.environ['D_TASK_ORCHESTRATOR_CLI_RESOURCES'] = str(d_resources)
    # os.environ['D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES'] = str(d_system_resources)
    # os.environ['D_task_orchestrator_cli_sensitive'] = str(d_task_orchestrator_cli_sensitive)
    # os.environ['D_PK_WORKING'] = str(d_pk_working)
    # os.environ['D_PK_MEMO'] = str(d_pk_memo)
    # os.environ['D_BUSINESS_DEMO'] = str(d_business_demo)
    # os.environ['D_DOWNLOADS'] = str(d_downloads)
    # os.environ['D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES'] = str(d_system_resources)

    #                 # 환경변수 설정 (Path 객체를 문자열로 변환)
    #                 os.environ['D_TASK_ORCHESTRATOR_CLI'] = str(task_orchestrator_cli)
    #                 os.environ['D_TASK_ORCHESTRATOR_CLI_RESOURCES'] = str(resources)
    #                 os.environ['D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES'] = str(system_resources)
    #                 os.environ['D_task_orchestrator_cli_sensitive'] = str(task_orchestrator_cli_sensitive)
    #                 os.environ['D_PK_WORKING'] = str(pk_working)
    #                 os.environ['D_PK_MEMO'] = str(pk_memo)
    #                 os.environ['D_BUSINESS_DEMO'] = str(business_demo)
    #                 os.environ['D_DOWNLOADS'] = str(downloads)
    #                 os.environ['D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES'] = str(system_resources)
    #
    #                 # alias 로드 및 등록
    #                 aliases = load_default_aliases()
    #                 success_count = 0
    #
    #                 for name, command in aliases.items():
    #                     if save_to_doskey(name, command):
    #                         success_count += 1
    #
    #                 # logging.debug(f"task_orchestrator_cli 환경변수 설정 완료, {{success_count}}개 alias 등록")
    #                 return True
    #
    #             except Exception as e:
    #                 logging.debug(f"환경변수 설정 실패: {{e}}")
    #                 return False

    def _ensure_file_lnk_created_windows(self) -> None:
        """바로가기 생성"""
        try:
            import win32com.client

            if not self.f_ensure_pk_alias_enabled_cmd.exists():
                logging.debug(f"️ {self.f_ensure_pk_alias_enabled_cmd} 파일이 존재하지 않습니다.")
                return

            shell = win32com.client.Dispatch("WScript.Shell")

            # 바탕화면 바로가기 생성
            try:
                desktop = Path.home() / "Desktop"
                if desktop.exists():
                    shortcut_path = desktop / "task_orchestrator_cli_launcher.lnk"
                    shortcut = shell.CreateShortCut(str(shortcut_path))
                    # ensure_task_orchestrator_cli_enabled.cmd 파일을 직접 사용
                    target_path = self.d_system_resources / "ensure_task_orchestrator_cli_enabled.cmd"
                    shortcut.Targetpath = str(target_path)
                    shortcut.WorkingDirectory = str(self.d_task_orchestrator_cli)
                    shortcut.save()
                    logging.debug(f"바탕화면 바로가기 생성됨: {shortcut_path}")
                    logging.debug(f"- 대상: {target_path}")
                    logging.debug(f"- 작업 디렉토리: {self.d_task_orchestrator_cli}")
            except Exception as e:
                logging.debug(f"️ 바탕화면 바로가기 생성 실패: {e}")

            # 작업 디렉토리 바로가기 생성
            try:
                shortcut_path = self.d_system_resources / "task_orchestrator_cli_launcher.lnk"
                shortcut = shell.CreateShortCut(str(shortcut_path))
                # ensure_task_orchestrator_cli_enabled.cmd 파일을 직접 사용
                target_path = self.d_system_resources / "ensure_task_orchestrator_cli_enabled.cmd"
                shortcut.Targetpath = str(target_path)
                shortcut.WorkingDirectory = str(self.d_task_orchestrator_cli)
                shortcut.save()
                logging.debug(f"작업 디렉토리 바로가기 생성됨: {shortcut_path}")
                logging.debug(f"- 대상: {target_path}")
                logging.debug(f"- 작업 디렉토리: {self.d_task_orchestrator_cli}")
            except Exception as e:
                logging.debug(f"️ 작업 디렉토리 바로가기 생성 실패: {e}")

        except ImportError as e:
            logging.debug(f"win32com.client 모듈을 가져올 수 없습니다: {e}")
        except Exception as e:
            logging.debug(f"바로가기 생성 중 예상치 못한 오류: {e}")

    def sync_uv_packages(self) -> bool:
        import os
        import subprocess
        from pathlib import Path

        """UV 패키지 동기화 (Windows)"""
        try:
            logging.debug(f"{PkTexts.PACKAGE_SYNC} (Windows)")

            if not self.d_task_orchestrator_cli.is_dir():
                raise FileNotFoundError(f"Target path does not exist: {self.d_task_orchestrator_cli}")

            os.chdir(str(self.d_task_orchestrator_cli))
            os.environ["PATH"] += ";" + str(self.f_uv_exe.parent)

            # .venv_windows 디렉토리 확인 및 생성
            venv_windows_path = Path(".venv_windows")
            if not venv_windows_path.exists():
                logging.debug(f"⚠️ .venv_windows 디렉토리가 없습니다. 생성 중...")
                result = subprocess.run([str(self.f_uv_exe), "venv", str(venv_windows_path)],
                                        capture_output=True, text=True, encoding='utf-8')
                if result.returncode != 0:
                    logging.debug(f"[오류] .venv_windows 생성 실패: {result.stderr}")
                    return False
                logging.debug(f"[성공] .venv_windows 디렉토리 생성 완료")
            else:
                logging.debug(f"[성공] .venv_windows 디렉토리가 이미 존재합니다. 생성 건너뜀")

            # .venv_windows 디렉토리를 활성화하고 uv sync --active 실행
            logging.debug(f"⚠️ .venv_windows virtual environment 활성화 중...")

            # Windows에서 virtual environment 활성화
            activate_script = venv_windows_path / "Scripts" / "activate.bat"
            if activate_script.exists():
                # 인코딩 문제 해결을 위한 환경변수 설정
                env = os.environ.copy()
                env['PYTHONIOENCODING'] = 'utf-8'
                env['PYTHONLEGACYWINDOWSSTDIO'] = 'utf-8'

                # 첫 번째 시도: 기본 uv sync --active
                logging.debug(f"⚠️ 첫 번째 시도: uv sync --active 실행 중...")
                cmd = f'"{activate_script}" && uv sync --active'
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True,
                                        encoding='utf-8', env=env, errors='replace')

                if result.returncode == 0:
                    logging.debug(f"[성공] uv sync --active 완료")
                    return True

                # 첫 번째 시도 실패 시 오류 분석
                error_output = result.stderr or result.stdout or "알 수 없는 오류"
                logging.debug(f"⚠️ 첫 번째 시도 실패. 오류 분석 중...")
                logging.debug(f"⚠️ 오류 내용: {error_output}")

                # simpleaudio 빌드 실패 감지
                if "simpleaudio" in error_output.lower() or "microsoft visual c++" in error_output.lower():
                    logging.debug(f"⚠️ Windows 빌드 문제 감지됨. 대안 방법 시도 중...")

                    # 대안 1: 문제가 되는 패키지 제외하고 설치
                    logging.debug(f"⚠️ 대안 1: 문제 패키지 제외하고 설치 시도...")
                    cmd_exclude = f'"{activate_script}" && uv sync --active --exclude simpleaudio --exclude PyAudio'
                    result_exclude = subprocess.run(cmd_exclude, shell=True, capture_output=True, text=True,
                                                    encoding='utf-8', env=env, errors='replace')

                    if result_exclude.returncode == 0:
                        logging.debug(f"[성공] 문제 패키지 제외하고 설치 완료")

                        # 필수 패키지만 수동으로 설치
                        logging.debug(f"⚠️ 필수 오디오 패키지 대안 설치 중...")
                        cmd_install = f'"{activate_script}" && pip install playsound pyaudio-win32'
                        result_install = subprocess.run(cmd_install, shell=True, capture_output=True, text=True,
                                                        encoding='utf-8', env=env, errors='replace')

                        if result_install.returncode == 0:
                            logging.debug(f"[성공] 대안 오디오 패키지 설치 완료")
                            return True
                        else:
                            logging.debug(f"⚠️ 대안 패키지 설치 실패, 기본 설치로 진행")
                            return True
                    else:
                        logging.debug(f"⚠️ 대안 1 실패, 대안 2 시도...")

                # 대안 2: --no-build-isolation 옵션으로 시도
                logging.debug(f"⚠️ 대안 2: --no-build-isolation 옵션으로 시도...")
                cmd_no_build = f'"{activate_script}" && uv sync --active --no-build-isolation'
                result_no_build = subprocess.run(cmd_no_build, shell=True, capture_output=True, text=True,
                                                 encoding='utf-8', env=env, errors='replace')

                if result_no_build.returncode == 0:
                    logging.debug(f"[성공] --no-build-isolation 옵션으로 설치 완료")
                    return True

                # 대안 3: pip으로 직접 설치
                logging.debug(f"⚠️ 대안 3: pip으로 직접 설치 시도...")
                cmd_pip = f'"{activate_script}" && pip install -r pyproject.toml --no-deps'
                result_pip = subprocess.run(cmd_pip, shell=True, capture_output=True, text=True,
                                            encoding='utf-8', env=env, errors='replace')

                if result_pip.returncode == 0:
                    logging.debug(f"[성공] pip으로 직접 설치 완료")
                    return True

                # 모든 대안 실패
                logging.debug(f"[오류] 모든 설치 방법 실패")
                logging.debug(f"⚠️ 수동 해결 방법:")
                logging.debug(f"⚠️ 1. Microsoft Visual C++ Build Tools 설치")
                logging.debug(f"⚠️ 2. 또는 문제가 되는 패키지 제거 후 재시도")
                logging.debug(f"⚠️ 3. 또는 Linux/WSL 환경에서 설치")
                return False

            else:
                logging.debug(f"[오류] activate.bat을 찾을 수 없음: {activate_script}")
                return False

        except Exception as e:
            logging.debug(f"{PkTexts.OPERATION_FAILED} {e}")
            return False

    def install_packages_with_venv_python(self) -> bool:
        import subprocess

        """virtual environment Python으로 패키지 설치 (Windows)"""
        try:

            logging.debug(f"{PkTexts.VENV_SETUP} (Windows)")

            if not self.f_venv_python_windows.exists():
                logging.debug(f"{PkTexts.VENV_PYTHON_NOT_FOUND} {self.f_venv_python_windows}")
                return False

            logging.debug(f"{PkTexts.VENV_PYTHON_FOUND} {self.f_venv_python_windows}")

            # 필수 패키지 설치
            packages = ["toml", "requests", "pywin32"]
            for package in packages:
                logging.debug(f"{PkTexts.PACKAGE_INSTALLING} {package}...")
                try:
                    result = subprocess.run([str(self.f_venv_python_windows), "-m", "pip", "install", package],
                                            capture_output=True, text=True)

                    if result.returncode == 0:
                        logging.debug(f"{PkTexts.PACKAGE_INSTALL_SUCCESS} {package}")
                    else:
                        logging.debug(f"️ {PkTexts.PACKAGE_INSTALL_FAILED} {package}: {result.stderr}")

                except Exception as e:
                    logging.debug(f"{PkTexts.PACKAGE_INSTALL_ERROR} {package}: {e}")

            logging.debug(f"{PkTexts.VENV_PACKAGE_INSTALL_COMPLETE}")
            return True

        except Exception as e:
            logging.debug(f"{PkTexts.OPERATION_FAILED} {e}")
            return False

    def test_venv_python(self) -> bool:
        import subprocess

        """virtual environment Python 테스트 (Windows)"""
        try:

            logging.debug(f"{PkTexts.VENV_PYTHON_TEST} (Windows)")

            if not self.f_venv_python_windows.exists():
                logging.debug(f"{PkTexts.VENV_PYTHON_NOT_FOUND} {self.f_venv_python_windows}")
                return False

            # Python 버전 확인
            try:
                result = subprocess.run([str(self.f_venv_python_windows), "--version"],
                                        capture_output=True, text=True)
                if result.returncode == 0:
                    logging.debug(f"{PkTexts.VENV_PYTHON_VERSION} {result.stdout.strip()}")
                else:
                    logging.debug(f"{PkTexts.VENV_TEST_FAILED} {result.stderr}")
                    return False
            except Exception as e:
                logging.debug(f"{PkTexts.VENV_TEST_FAILED} {e}")
                return False

            # toml 모듈 테스트
            try:
                result = subprocess.run(
                    [str(self.f_venv_python_windows), "-c",
                     "import logging; import toml; logging.debug('toml module available')"],
                    capture_output=True, text=True)
                if result.returncode == 0:
                    logging.debug(f"{PkTexts.VENV_MODULE_TEST} toml")
                else:
                    logging.debug(f"{PkTexts.VENV_TEST_FAILED} toml module: {result.stderr}")
                    return False
            except Exception as e:
                logging.debug(f"{PkTexts.VENV_TEST_FAILED} {e}")
                return False

            logging.debug(f"{PkTexts.VENV_TEST_SUCCESS}")
            return True

        except Exception as e:
            logging.debug(f"{PkTexts.OPERATION_FAILED} {e}")
            return False

    def execute_f_pk_alias_bat(self):
        import subprocess

        f_pk_alias_bat = F_ENSURE_PK_ALIAS_ENABLED_BAT
        if f_pk_alias_bat.exists():
            result = subprocess.run(f'call "{f_pk_alias_bat}"', shell=True, capture_output=True, text=True,
                                    encoding='utf-8', errors='ignore')
            if result.returncode == 0:
                logging.debug("파일 실행 완료")
                if result.stdout:
                    logging.debug(f"출력: {result.stdout}")
                return f_pk_alias_bat
            else:
                logging.debug(f"️ 파일 실행 실패 (코드: {result.returncode})")
                if result.stderr:
                    logging.debug(f"오류: {result.stderr}")

    def regist_autorun(self):
        import subprocess
        f_pk_alias_bat = F_ENSURE_PK_ALIAS_ENABLED_BAT
        f_pk_alias_bat = f_pk_alias_bat
        # 레지스트리 AutoRun 설정
        try:
            # AutoRun 등록 (REG_EXPAND_SZ 로 환경변수 확장 허용 + call 사용)
            autorun_value = rf'call "{f_pk_alias_bat}"'
            subprocess.run([
                "reg", "add", r"HKCU\Software\Microsoft\Command Processor",
                "/v", "AutoRun", "/t", "REG_EXPAND_SZ", "/d", autorun_value, "/f"
            ], check=True, text=True, capture_output=True)
            logging.debug(f"AutoRun 등록:{autorun_value}")

            # 확인
            subprocess.run([
                "reg", "query", r"HKCU\Software\Microsoft\Command Processor", "/v", "AutoRun"
            ], check=True)
            logging.debug(f"AutoRun 설정완료")
        except Exception as e:
            logging.debug(f"️ 레지스트리 설정 실패 {e}")
