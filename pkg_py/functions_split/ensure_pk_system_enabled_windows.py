import os
import platform
import subprocess
import tempfile
import time
import uuid
import zipfile


from pkg_py.functions_split.ensure_pnxs_moved_to_trash_bin import ensure_pnxs_moved_to_trash_bin
from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP
from pkg_py.system_object.directories import *
from pkg_py.system_object.files import *
from pkg_py.system_object.urls import FZF_API_URL

if platform.system().lower() == "windows":
    import winreg

print = None
PkMessages2025FallBack = type('PkMessages2025', (), {
    'VENV_PYTHON_TEST': '가상환경 Python 테스트',
    'VENV_PYTHON_NOT_FOUND': '가상환경 Python을 찾을 수 없음',
    'VENV_PYTHON_VERSION': '가상환경 Python 버전',
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
    'VENV_SETUP': '가상환경 Python으로 패키지 설치',
    'VENV_PYTHON_FOUND': '가상환경 Python 사용',
    'PACKAGE_INSTALLING': '설치 중',
    'PACKAGE_INSTALL_SUCCESS': '설치 완료',
    'PACKAGE_INSTALL_FAILED': '설치 실패',
    'PACKAGE_INSTALL_ERROR': '설치 오류',
    'VENV_PACKAGE_INSTALL_COMPLETE': '가상환경 패키지 설치 완료',
    'FZF_INSTALLATION': 'FZF 설치',
    'OPERATION_SUCCESS': '동기화 완료',
    'OPERATION_FAILED': '동기화 실패',
    'VENV_TEST_FAILED': '테스트 실패'
})()
# Lazy import to avoid circular dependency
try:
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.map_massages import PkMessages2025

    print = ensure_printed
except ImportError:
    import builtins

    print = builtins.print
    PkMessages2025 = PkMessages2025FallBack


class WindowsManager():
    """Windows 플랫폼 관리자"""

    def __init__(self):
        super().__init__()
        if platform.system().lower() == "windows":
            import winreg
            self.winreg = winreg

        self.d_userprofile = Path.home()
        self.d_pk_system = Path(D_PK_SYSTEM)
        self.d_business_demo = Path(D_BUSINESS_DEMO)
        self.d_pkg_py = Path(D_PKG_PY)
        self.d_pkg_windows = Path(D_PKG_WINDOWS)
        self.d_pkg_cache_private = Path(D_PKG_CACHE_PRIVATE)
        self.d_pk_working = Path(D_PK_WORKING)
        self.d_pk_memo = Path(D_PK_MEMO)
        self.d_business_demo = Path(D_BUSINESS_DEMO)
        self.d_downloads = Path(D_DOWNLOADS)
        self.d_pkg_linux = Path(D_PKG_LINUX)
        self.d_pk_recycle_bin = Path(D_PKG_CACHE_PRIVATE)
        self.d_venv_scripts = Path(D_VENV) / "Scripts"

        self.f_venv_python_windows = self.d_venv_scripts / "python.exe"
        self.f_uv_exe = Path(F_UV_EXE) if F_UV_EXE else self.d_pkg_windows / "uv.exe"
        self.f_fzf_exe = Path(F_FZF_EXE) if F_FZF_EXE else self.d_pkg_windows / "fzf.exe"
        self.f_uv_zip = Path(F_UV_ZIP) if F_UV_ZIP else self.d_downloads / "uv.zip"
        self.f_fzf_zip = Path(F_FZF_ZIP) if F_FZF_ZIP else self.d_downloads / "fzf.zip"

        self.f_ensure_pk_alias_enabled_cmd = Path(D_PKG_WINDOWS) / "ensure_pk_alias_enabled.cmd"
        self.f_ensure_pk_system_ran_cmd = self.d_pkg_windows / "ensure_pk_system_ran.cmd"

        ensure_pnxs_moved_to_trash_bin(pnxs=[self.f_ensure_pk_alias_enabled_cmd, self.f_ensure_pk_system_ran_cmd])

    def install_uv(self, max_retry: int = 2) -> bool:
        """UV 설치 (Windows)"""
        import shutil
        try:
            print(f" Step 11: UV 설치 (Windows)")
            # 디렉토리 생성 권한 확인
            if not self._check_windows_permissions():
                print(f"️ 권한 오류: {self.d_pkg_windows}")
                return False

            # 기존 파일 백업
            if self.f_uv_exe.exists():
                try:
                    backup_path = self.f_uv_exe.with_suffix('.exe.backup')
                    self.f_uv_exe.rename(backup_path)
                    print(f" 백업 생성됨: {self.f_uv_exe}")
                except Exception as e:
                    print(f"️ 백업 실패: {self.f_uv_exe}")
                    try:
                        self.f_uv_exe.unlink()
                    except Exception as e2:
                        print(f"️ 백업 실패: {e2}")

            # UV 다운로드 및 설치
            for attempt in range(max_retry):
                try:
                    print(f" [Attempt {attempt + 1}] Downloading from https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip")

                    # 임시 디렉토리 생성
                    temp_dir = Path(tempfile.gettempdir()) / f"uv_install_{uuid.uuid4().hex[:8]}"
                    temp_dir.mkdir(exist_ok=True)

                    # UV 다운로드
                    uv_zip_path = temp_dir / "uv.zip"
                    import requests
                    response = requests.get("https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip", timeout=30)
                    response.raise_for_status()

                    with open(uv_zip_path, 'wb') as f:
                        f.write(response.content)

                    # 압축 해제
                    print(" Extracting uv.zip...")
                    with zipfile.ZipFile(uv_zip_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)

                    # UV 실행 파일 복사
                    uv_exe_src = temp_dir / "uv.exe"
                    if uv_exe_src.exists():
                        try:
                            shutil.copy2(uv_exe_src, self.f_uv_exe)
                            print(f" 파일 복사 성공: {self.f_uv_exe}")
                        except PermissionError:
                            # 대안 위치에 설치
                            alternative_path = Path.home() / "uv.exe"
                            shutil.copy2(uv_exe_src, alternative_path)
                            self.f_uv_exe = alternative_path
                            print(f" 대안 설치: {alternative_path}")
                        except Exception as e:
                            print(f" 파일 복사 실패: {e}")
                            return False
                    else:
                        print(f" uv.exe in extracted files")
                        return False

                    # 임시 디렉토리 정리
                    try:
                        shutil.rmtree(temp_dir)
                    except Exception as e:
                        print(f"️ 임시 파일 정리 실패: {e}")

                    # 설치 확인
                    result = subprocess.run([str(self.f_uv_exe), "--version"], capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f" 설치 완료: {result.stdout.strip()}")
                        return True
                    else:
                        print(f" 설치 실패: {result.stderr}")

                except Exception as e:
                    print(f" 설치 실패: {e}")
                    if attempt < max_retry - 1:
                        time.sleep(2)
                        continue
                    else:
                        return False

            return False

        except Exception as e:
            print(f" 설치 실패: {e}")
            return False

    def _check_windows_permissions(self) -> bool:
        """Windows 권한 확인 및 안내"""
        try:
            # 테스트 파일 생성 시도
            test_file = self.d_pkg_windows / "test_permission.tmp"
            test_file.write_text("test")
            test_file.unlink()
            return True
        except PermissionError:
            print(f"️ 권한 문제 발견: {PK_ANSI_COLOR_MAP['YELLOW']}상태=권한문제 {PK_ANSI_COLOR_MAP['RESET']}")
            print(" 해결 방법:")
            print("   1. 관리자 권한으로 실행:")
            print(rf"      {self.d_pkg_windows}\ensure_pk_system_enabled_admin.cmd")
            print("   2. 또는 PowerShell을 관리자 권한으로 실행 후:")
            print(f"      cd {self.d_pk_system}")
            print(rf"      python pkg_py\functions_split\ensure_pk_system_enabled.py")
            print("   3. 또는 명령 프롬프트를 관리자 권한으로 실행 후:")
            print(f"      cd {self.d_pk_system}")
            print(rf"      python pkg_py\functions_split\ensure_pk_system_enabled.py")
            print("   4. 대안 위치 사용 (자동으로 시도됨):")
            from pkg_py.system_object.directories import D_DOWNLOADS
            print(rf"      {D_DOWNLOADS}")
            return False
        except Exception as e:
            print(f"️ 권한 확인 오류: {PK_ANSI_COLOR_MAP['RED']}오류={e} {PK_ANSI_COLOR_MAP['RESET']}")
            return False

    def install_fzf(self, max_retry: int = 2) -> bool:
        """FZF 설치 (Windows)"""
        try:
            print(f" FZF 설치 (Windows)")

            # 권한 확인
            if not self._check_windows_permissions():
                print(f"️ 권한 오류: {self.d_pkg_windows}")
                return False

            # 최신 FZF URL 가져오기
            fzf_url = self._get_latest_fzf_url_windows()
            print(" FZF 최신 버전 확인 중...")
            print(f"FZF 최신 버전: {fzf_url.split('/')[-1].replace('fzf-', '').replace('-windows_amd64.zip', '')}")
            print(f"FZF 다운로드 URL: {fzf_url}")

            # 기존 파일 백업
            if self.f_fzf_exe.exists():
                try:
                    backup_path = self.f_fzf_exe.with_suffix('.exe.backup')
                    self.f_fzf_exe.rename(backup_path)
                    print(f" 백업 생성됨: {self.f_fzf_exe}")
                except Exception as e:
                    print(f"️ 백업 실패: {self.f_fzf_exe}")
                    try:
                        self.f_fzf_exe.unlink()
                    except Exception as e2:
                        print(f"️ 백업 실패: {e2}")

            # FZF 다운로드 및 설치
            for attempt in range(max_retry):
                try:
                    print(f" [Attempt {attempt + 1}] Downloading fzf from {fzf_url}")
                    print(f" [Attempt {attempt + 1}] Downloading from {fzf_url}")

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
                    print(" Extracting fzf.zip...")
                    with zipfile.ZipFile(fzf_zip_path, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)

                    # FZF 실행 파일 복사
                    fzf_exe_src = temp_dir / "fzf.exe"
                    if fzf_exe_src.exists():
                        try:
                            import shutil
                            shutil.copy2(fzf_exe_src, self.f_fzf_exe)
                            print(f" 파일 복사 성공: {self.f_fzf_exe}")
                        except PermissionError:
                            # 대안 위치에 설치
                            alternative_path = Path.home() / "fzf.exe"
                            shutil.copy2(fzf_exe_src, alternative_path)
                            self.f_fzf_exe = alternative_path
                            print(f" 대안 설치: {alternative_path}")
                        except Exception as e:
                            print(f" 파일 복사 실패: {e}")
                            return False
                    else:
                        print(f" fzf.exe in extracted files")
                        return False

                    # 임시 디렉토리 정리
                    try:
                        shutil.rmtree(temp_dir)
                    except Exception as e:
                        print(f"️ 임시 파일 정리 실패: {e}")

                    # 설치 확인
                    result = subprocess.run([str(self.f_fzf_exe), "--version"], capture_output=True, text=True)
                    if result.returncode == 0:
                        print(f" 설치 완료: {result.stdout.strip()}")
                        return True
                    else:
                        print(f" 설치 실패: {result.stderr}")

                except Exception as e:
                    print(f" 설치 실패: {e}")
                    if attempt < max_retry - 1:
                        time.sleep(2)
                        continue
                    else:
                        return False

            return False

        except Exception as e:
            print(f" 설치 실패: {e}")
            return False

    def _get_latest_fzf_url_windows(self) -> str:
        """GitHub API를 사용하여 최신 FZF 다운로드 URL 가져오기 (Windows)"""
        try:
            print(" FZF 최신 버전 확인 중...")
            import requests
            response = requests.get(FZF_API_URL)
            response.raise_for_status()
            data = response.json()
            version = data["tag_name"]
            print(f"FZF 최신 버전: {version}")

            version_clean = version.lstrip('v')
            download_url = f"https://github.com/junegunn/fzf/releases/download/{version}/fzf-{version_clean}-windows_amd64.zip"
            print(f"FZF 다운로드 URL: {download_url}")

            return download_url

        except Exception as e:
            fallback_url = "https://github.com/junegunn/fzf/releases/download/v0.65.0/fzf-0.65.0-windows_amd64.zip"
            print(f"Fallback URL 사용: {fallback_url}")
            return fallback_url

    def setup_path(self) -> bool:
        """Windows PATH 설정"""
        try:

            print(f" {PkMessages2025.PATH_SETUP}")

            # 새로운 PATH 구성
            new_path = self._build_windows_path()

            # 시스템 PATH 업데이트
            try:
                import winreg

                # 사용자 PATH 업데이트
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
                winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)
                winreg.CloseKey(key)

                # 환경변수 변경 알림
                self._broadcast_environment_change()

                print(f" {PkMessages2025.OPERATION_SUCCESS}")
                return True

            except Exception as e:
                print(f" {PkMessages2025.OPERATION_FAILED} {e}")
                return False

        except Exception as e:
            print(f" {PkMessages2025.OPERATION_FAILED} {e}")
            return False

    def _build_windows_path(self) -> str:
        """Windows PATH 구성"""
        system_path = self._get_system_path()
        user_path = self._get_user_path()

        all_paths = system_path + ";" + user_path if user_path else system_path
        path_list = all_paths.split(";")

        # 중복 제거 및 정리
        seen = set()
        clean_path = []

        # 우선순위 경로 추가
        priority_paths = [
            (self.d_pkg_windows, "UV/FZF 경로"),
            (self.d_venv_scripts, "가상환경 Scripts 경로"),
            (self.d_pkg_py, "PK_PY 경로"),
            (self.d_business_demo, "Business Demo 경로")
        ]

        for path, description in priority_paths:
            if path.exists():
                norm_path = str(path.resolve())
                if norm_path not in seen:
                    seen.add(norm_path)
                    clean_path.append(norm_path)
                    print(f" {description} 추가: {norm_path}")

        # 나머지 경로 추가
        for path in path_list:
            norm = os.path.normpath(path.strip())
            if not norm or norm in seen:
                continue
            if "user" in norm.lower() and "pk_system" not in norm.lower():
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
                print("환경변수 변경 알림이 전송되었습니다.")
            else:
                print("환경변수 변경 알림 전송 실패")
        except Exception as e:
            print(f"환경변수 변경 알림 실패: {e}")

    def setup_aliases(self) -> bool:
        """Windows 별칭 설정"""
        try:
            print(f" {PkMessages2025.ALIAS_SETUP}")

            # 배치 파일 생성 및 실행
            self.create_and_run_batch_file()

            # 레지스트리 AutoRun 설정
            try:
                batch_file = self.d_pkg_cache_private / "ensure_pk_alias_enabled.bat"
                subprocess.run([
                    "reg", "add", "HKCU\\Software\\Microsoft\\Command Processor", "/v", "AutoRun", "/t", "REG_SZ", "/d", str(batch_file), "/f"
                ], capture_output=True, text=True)
                print(" AutoRun 설정 완료")
            except Exception as e:
                print(f"️ 레지스트리 설정 실패 {e}")

            print(f" {PkMessages2025.OPERATION_SUCCESS}")
            return True

        except Exception as e:
            print(f" {PkMessages2025.OPERATION_FAILED} {e}")
            return False

    def create_and_run_batch_file(self) -> None:
        """배치 파일 생성 및 실행"""
        try:
            import textwrap
            batch_content = textwrap.dedent(f'''\
                @echo off
                REM PK System AutoRun Script

                REM UTF-8 인코딩 설정
                chcp 65001 >nul

                doskey 1=cd "{self.d_downloads}"
                doskey 2=cd "{self.d_pk_system}"
                doskey 3=cd "{self.d_business_demo}"
                doskey 4=cd "{self.d_pk_memo}"
                doskey 5=cd "{self.d_pkg_py}"
                doskey 6=cd "{self.d_pkg_windows}"
                doskey 7=cd "{self.d_pk_working}"
                doskey pk=python "{self.d_pk_system}\\pkg_py\\pk_ensure_pk_system_started.py"
                doskey pkpk=python "{self.d_pk_system}\\pkg_py\\pk_ensure_pk_system_enabled.py"
                doskey gpt=start https://chat.openai.com
                doskey ls=dir /b
                doskey cat=type $*
                doskey which=where $*
                doskey pwd=cd $*
                doskey x=exit
                doskey .=explorer.exe .
            
                REM 주요 명령어 실행
                doskey pk=python "{self.d_pk_system}\\pkg_py\\pk_ensure_pk_system_started.py"
                doskey pkpk=python "{self.d_pk_system}\\pkg_py\\pk_ensure_pk_system_enabled.py"
                doskey pk--fix=python "{self.d_pk_system}\\pkg_py\\pk_ensure_pk_system_enabled.py"
                doskey pk--enable=python "{self.d_pk_system}\\pkg_py\\pk_ensure_pk_system_enabled.py"
            
                REM 가상환경, IDE
                doskey venv="{self.d_pk_system}\\.venv\\Scripts\\activate"
                doskey code=rf"{self.d_userprofile}\AppData\Local\Programs\Microsoft VS Code\Code.exe" $*
                doskey pycharm=start "" "C:\\Program Files\\JetBrains\\PyCharm Community Edition\\bin\\pycharm64.exe" $*
                
                REM PowerShell 및 관리자 권한
                doskey ps=powershell
                doskey psa=powershell -Command "Start-Process powershell -Verb RunAs"
                doskey cmda=start "" "{self.d_pkg_windows}\\ensure_cmd_exe_ran_as_admin.cmd"
            
                REM 시스템 명령
                doskey reboot=shutdown /r /t 0
                doskey poweroff=shutdown /s /t 0
                doskey shutdown=shutdown /s /t 0
                doskey logout=logoff
            
                REM WSL
                doskey wsld=wsl --distribution Ubuntu
                doskey wsl24=wsl --distribution Ubuntu-24.04
                doskey wsl20=wsl --distribution Ubuntu-20.04
                doskey wsl18=wsl --distribution Ubuntu-18.04
            
                REM linux 와 닮은 유틸리티
                doskey ls=dir /b
                doskey cat=type $*
                doskey which=where $*
                doskey pwd=cd $*
                doskey cls=clear
                doskey gpt=start https://chat.openai.com
                doskey history=doskey /history
            
                REM 탐색/편집 명령
                doskey find_f=dir /s /b
                doskey find_d=dir /s /b /ad
                doskey find_pnx=dir /s /b *.pnx
                doskey cp_pwd=copy
            
                REM 삭제 명령  
                doskey rm_f=del
                doskey rm_d=rmdir /s /q
            ''')
            # TODO : 삭제 명령 python 처리도 괜찮음 doskey rm=  ensure_pnxs_moved_to_recycle_bin
            # TODO : reboot == poweroff == shutdown

            f_pk_alias_bat = self.d_pkg_cache_private / "ensure_pk_alias_enabled.bat"
            f_pk_alias_bat.parent.mkdir(parents=True, exist_ok=True)

            with open(f_pk_alias_bat, 'w', encoding='utf-8') as f:
                f.write(batch_content)

            print(f" 배치 파일 생성 완료: {f_pk_alias_bat}")

            # 배치 파일 실행
            print(" 배치 파일 실행 중...")
            result = subprocess.run(str(f_pk_alias_bat), shell=True, capture_output=True, text=True, encoding='utf-8', errors='ignore')

            if result.returncode == 0:
                print(" 배치 파일 실행 완료")
                if result.stdout:
                    print(f"출력: {result.stdout}")
            else:
                print(f"️ 배치 파일 실행 실패 (코드: {result.returncode})")
                if result.stderr:
                    print(f"오류: {result.stderr}")

        except Exception as e:
            print(f"배치 파일 생성/실행 실패: {e}")
            raise

    # def get_pk_alias_script_content(self) -> str:
    #     import textwrap
    #     script = textwrap.dedent(f'''\
    #         #!/usr/bin/env python3
    #         # -*- coding: utf-8 -*-
    #         """
    #         PK System 환경변수 설정 및 내장 alias 로드 스크립트
    #         """
    #         import os
    #         import subprocess
    #         import sys
    #         from pathlib import Path
    #
    #         # UTF-8 인코딩 설정
    #         if sys.platform == "win32":
    #             import codecs
    #             sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    #             sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())
    #
    #         userprofile = Path.home()
    #         pk_system = Path(r"{get_pnx_os_style(Path(D_PK_SYSTEM))}")
    #         pkg_py = Path(r"{get_pnx_os_style(Path(D_PKG_PY))}")
    #         pkg_windows = Path(r"{get_pnx_os_style(Path(D_PKG_WINDOWS))}")
    #         pkg_cache_private = Path(r"{get_pnx_os_style(Path(D_PKG_CACHE_PRIVATE))}")
    #         pk_working = Path(r"{get_pnx_os_style(Path(D_PK_WORKING))}")
    #         pk_memo = Path(r"{get_pnx_os_style(Path(D_PK_MEMO))}")
    #         business_demo = Path(r"{get_pnx_os_style(Path(D_BUSINESS_DEMO))}")
    #         downloads = Path(r"{get_pnx_os_style(Path(D_DOWNLOADS))}")
    #         pkg_linux = Path(r"{get_pnx_os_style(Path(D_PKG_LINUX))}")
    #
    #         def load_default_aliases():
    #             # 37개의 기본 alias 정의
    #             aliases = {{
    #                 # 시스템 관련
    #                 'x': 'exit',
    #                 'wsld': 'wsl --distribution Ubuntu',
    #                 'wsl24': 'wsl --distribution Ubuntu-24.04',
    #                 'wsl20': 'wsl --distribution Ubuntu-20.04',
    #                 'wsl18': 'wsl --distribution Ubuntu-18.04',
    #                 'reboot': 'shutdown /r /t 0',
    #                 'poweroff': 'shutdown /s /t 0',
    #                 'logout': 'logoff',
    #
    #                 # 관리자 관련
    #                 'cmda': 'cmd /k',
    #                 'ps': 'powershell',
    #                 'psa': 'powershell -Command "Start-Process powershell -Verb RunAs"',
    #
    #                 # IDE 관련
    #                 'pycharm': 'start "" "C:\\\\Program Files\\\\JetBrains\\\\PyCharm Community Edition\\\\bin\\\\pycharm64.exe"',
    #                 'code': 'code .',
    #
    #                 # 디렉토리 이동
    #                 '0': f'cd "{{pk_system}}"',
    #                 '1': f'cd "{{pkg_py}}"',
    #                 '2': f'cd "{{pkg_windows}}"',
    #                 '3': f'cd "{{pk_working}}"',
    #                 '4': f'cd "{{pk_memo}}"',
    #                 '5': f'cd "{{business_demo}}"',
    #
    #                 # 편집 관련
    #                 'E100': 'notepad',
    #                 'E200': 'code .',
    #                 'E000': 'notepad .',
    #
    #                 # 유틸리티
    #                 '.': 'cls',
    #                 'gpt': 'start https://chat.openai.com',
    #                 'history': 'doskey /history',
    #                 'cat': 'type',
    #                 'which': 'where',
    #                 'pwd': 'cd',
    #                 'venv': f'"{{pk_system}}\\\\.venv\\\\Scripts\\\\activate"',
    #                 'pk': f'python "{{pk_system}}\\\\pkg_py\\\\pk_ensure_pk_system_enabled.py"',
    #                 'ls': 'dir',
    #                 'rm_f': 'del',
    #                 'rm_d': 'rmdir /s /q',
    #                 'find_f': 'dir /s /b',
    #                 'find_d': 'dir /s /b /ad',
    #                 'find_pnx': 'dir /s /b *.pnx',
    #                 'cp_pwd': 'copy'
    #             }}
    #             return aliases
    #
    #         def save_to_doskey(name, command):
    #             """Windows에서 doskey로 alias 저장"""
    #             try:
    #                 doskey_cmd = f'doskey {{name}}={{command}}'
    #                 result = subprocess.run(doskey_cmd, shell=True, capture_output=True, text=True)
    #                 return result.returncode == 0
    #             except Exception as e:
    #                 return False
    #
    #         def setup_pk_environment():
    #             """PK System 환경변수 설정 및 내장 alias 로드"""
    #             try:

                        # # d_userprofile = Path.home()
                        # # d_downloads = Path(rf"{d_userprofile}\Downloads")
                        # # d_pk_system = Path(rf"{d_downloads}\pk_system")
                        # # d_pkg_py = Path(rf"{d_downloads}\pk_system\pkg_py")
                        # # d_pkg_windows = Path(rf"{d_downloads}\pk_system\pkg_windows")
                        # # d_pkg_cache_private = Path(rf"{d_downloads}\pk_system\pkg_cache_private")
                        # # d_pk_working = Path(rf"{d_downloads}\pk_working")
                        # # d_pk_memo = Path(rf"{d_downloads}\pk_memo")
                        # # d_business_demo = Path(rf"{d_downloads}\business_demo")
                        # # d_pkg_linux = Path(rf"{d_downloads}\pk_system\pkg_linux")

                        # # 환경변수 설정 (Path 객체를 문자열로 변환)
                        # os.environ['D_PK_SYSTEM'] = str(d_pk_system)
                        # os.environ['D_PKG_PY'] = str(d_pkg_py)
                        # os.environ['D_PKG_WINDOWS'] = str(d_pkg_windows)
                        # os.environ['D_pkg_cache_private'] = str(d_pkg_cache_private)
                        # os.environ['D_PK_WORKING'] = str(d_pk_working)
                        # os.environ['D_PK_MEMO'] = str(d_pk_memo)
                        # os.environ['D_BUSINESS_DEMO'] = str(d_business_demo)
                        # os.environ['D_DOWNLOADS'] = str(d_downloads)
                        # os.environ['D_PKG_LINUX'] = str(d_pkg_linux)

    #                 # 환경변수 설정 (Path 객체를 문자열로 변환)
    #                 os.environ['D_PK_SYSTEM'] = str(pk_system)
    #                 os.environ['D_PKG_PY'] = str(pkg_py)
    #                 os.environ['D_PKG_WINDOWS'] = str(pkg_windows)
    #                 os.environ['D_pkg_cache_private'] = str(pkg_cache_private)
    #                 os.environ['D_PK_WORKING'] = str(pk_working)
    #                 os.environ['D_PK_MEMO'] = str(pk_memo)
    #                 os.environ['D_BUSINESS_DEMO'] = str(business_demo)
    #                 os.environ['D_DOWNLOADS'] = str(downloads)
    #                 os.environ['D_PKG_LINUX'] = str(pkg_linux)
    #
    #                 # alias 로드 및 등록
    #                 aliases = load_default_aliases()
    #                 success_count = 0
    #
    #                 for name, command in aliases.items():
    #                     if save_to_doskey(name, command):
    #                         success_count += 1
    #
    #                 # print(f"PK System 환경변수 설정 완료, {{success_count}}개 alias 등록")
    #                 return True
    #
    #             except Exception as e:
    #                 print(f"환경변수 설정 실패: {{e}}")
    #                 return False
    #
    #         if __name__ == "__main__":
    #             setup_pk_environment()
    #     ''')
    #     return script

    def _ensure_file_lnk_created_windows(self) -> None:
        """바로가기 생성"""
        try:
            import win32com.client

            if not self.f_ensure_pk_alias_enabled_cmd.exists():
                print(f"️ {self.f_ensure_pk_alias_enabled_cmd} 파일이 존재하지 않습니다.")
                return

            shell = win32com.client.Dispatch("WScript.Shell")

            # 바탕화면 바로가기 생성
            try:
                desktop = Path.home() / "Desktop"
                if desktop.exists():
                    shortcut_path = desktop / "pk_system_launcher.lnk"
                    shortcut = shell.CreateShortCut(str(shortcut_path))
                    shortcut.Targetpath = str(self.f_ensure_pk_alias_enabled_cmd)
                    shortcut.WorkingDirectory = str(self.d_pk_system)
                    shortcut.save()
                    print(f" 바탕화면 바로가기 생성됨: {shortcut_path}")
            except Exception as e:
                print(f"️ 바탕화면 바로가기 생성 실패: {e}")

            # 작업 디렉토리 바로가기 생성
            try:
                shortcut_path = self.d_pkg_windows / "pk_system_launcher.lnk"
                shortcut = shell.CreateShortCut(str(shortcut_path))
                shortcut.Targetpath = str(self.f_ensure_pk_alias_enabled_cmd)
                shortcut.WorkingDirectory = str(self.d_pk_system)
                shortcut.save()
                print(f" 작업 디렉토리 바로가기 생성됨: {shortcut_path}")
            except Exception as e:
                print(f"️ 작업 디렉토리 바로가기 생성 실패: {e}")

        except ImportError as e:
            print(f"win32com.client 모듈을 가져올 수 없습니다: {e}")
        except Exception as e:
            print(f"바로가기 생성 중 예상치 못한 오류: {e}")

    def sync_uv_packages(self) -> bool:
        """UV 패키지 동기화 (Windows)"""
        try:
            print(f" {PkMessages2025.PACKAGE_SYNC} (Windows)")

            if not self.d_pk_system.is_dir():
                raise FileNotFoundError(f"Target path does not exist: {self.d_pk_system}")

            os.chdir(str(self.d_pk_system))
            os.environ["PATH"] += ";" + str(self.f_uv_exe.parent)

            result = subprocess.run([str(self.f_uv_exe), "sync"])
            if result.returncode != 0:
                raise RuntimeError("uv sync failed.")

            print(f" {PkMessages2025.OPERATION_SUCCESS} - 가상환경 Python 사용 준비됨")
            return True

        except Exception as e:
            print(f" {PkMessages2025.OPERATION_FAILED} {e}")
            return False

    def install_packages_with_venv_python(self) -> bool:
        """가상환경 Python으로 패키지 설치 (Windows)"""
        try:

            print(f" {PkMessages2025.VENV_SETUP} (Windows)")

            if not self.f_venv_python_windows.exists():
                print(f" {PkMessages2025.VENV_PYTHON_NOT_FOUND} {self.f_venv_python_windows}")
                return False

            print(f" {PkMessages2025.VENV_PYTHON_FOUND} {self.f_venv_python_windows}")

            # 필수 패키지 설치
            packages = ["toml", "requests", "pywin32"]
            for package in packages:
                print(f" {PkMessages2025.PACKAGE_INSTALLING} {package}...")
                try:
                    result = subprocess.run([
                        str(self.f_venv_python_windows), "-m", "pip", "install", package
                    ], capture_output=True, text=True)

                    if result.returncode == 0:
                        print(f" {PkMessages2025.PACKAGE_INSTALL_SUCCESS} {package}")
                    else:
                        print(f"️ {PkMessages2025.PACKAGE_INSTALL_FAILED} {package}: {result.stderr}")

                except Exception as e:
                    print(f" {PkMessages2025.PACKAGE_INSTALL_ERROR} {package}: {e}")

            print(f" {PkMessages2025.VENV_PACKAGE_INSTALL_COMPLETE}")
            return True

        except Exception as e:
            print(f" {PkMessages2025.OPERATION_FAILED} {e}")
            return False

    def test_venv_python(self) -> bool:
        """가상환경 Python 테스트 (Windows)"""
        try:

            print(f" {PkMessages2025.VENV_PYTHON_TEST} (Windows)")

            if not self.f_venv_python_windows.exists():
                print(f" {PkMessages2025.VENV_PYTHON_NOT_FOUND} {self.f_venv_python_windows}")
                return False

            # Python 버전 확인
            try:
                result = subprocess.run([str(self.f_venv_python_windows), "--version"],
                                        capture_output=True, text=True)
                if result.returncode == 0:
                    print(f" {PkMessages2025.VENV_PYTHON_VERSION} {result.stdout.strip()}")
                else:
                    print(f" {PkMessages2025.VENV_TEST_FAILED} {result.stderr}")
                    return False
            except Exception as e:
                print(f" {PkMessages2025.VENV_TEST_FAILED} {e}")
                return False

            # toml 모듈 테스트
            try:
                result = subprocess.run([str(self.f_venv_python_windows), "-c", "import toml; print('toml module available')"],
                                        capture_output=True, text=True)
                if result.returncode == 0:
                    print(f" {PkMessages2025.VENV_MODULE_TEST} toml")
                else:
                    print(f" {PkMessages2025.VENV_TEST_FAILED} toml module: {result.stderr}")
                    return False
            except Exception as e:
                print(f" {PkMessages2025.VENV_TEST_FAILED} {e}")
                return False

            print(f" {PkMessages2025.VENV_TEST_SUCCESS}")
            return True

        except Exception as e:
            print(f" {PkMessages2025.OPERATION_FAILED} {e}")
            return False
