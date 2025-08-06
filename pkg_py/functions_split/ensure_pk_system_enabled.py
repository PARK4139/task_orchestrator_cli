#!/usr/bin/env python3
"""
PK System Enable Script (Refactored Version)
중복 제거 및 플랫폼별 마이그레이션된 버전
"""
import os
import platform
import subprocess
import sys
from abc import ABC, abstractmethod
from pathlib import Path

from pkg_py.functions_split.ensure_guided_not_prepared_yet import ensure_guided_not_prepared_yet
from pkg_py.system_object.map_massages import PkMessages2025

# System object imports with error handling
try:
    from pkg_py.system_object.directories import *
    from pkg_py.system_object.files import *
except ImportError as e:
    print(f"Error: Could not import system objects: {e}")
    raise



class CommonUtils:
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
        """모듈을 import하거나 설치"""
        import_name = import_name or pkg_name
        try:
            __import__(import_name)
        except ImportError:
            print(f"'{pkg_name}' {PkMessages2025.MODULE_NOT_FOUND}, attempting to install...")
            try:
                subprocess.run([sys.executable, "-m", "pip", "install", pkg_name], check=True)
            except Exception as e:
                print(f"{PkMessages2025.INSTALL_FAILED} '{pkg_name}': {e}")
                raise

    @staticmethod
    def print_step(step_index: int, total_steps: int, description: str, color: str = "cyan") -> None:
        """단계 출력"""
        color_code = {"cyan": 36, "yellow": 33, "green": 32, "red": 31}.get(color, 36)
        print(f"\033[{color_code}m[{step_index}/{total_steps}] {description}\033[0m")

    @staticmethod
    def download_file(url: str, file_path: Path, max_retry: int = 2) -> bool:
        """파일 다운로드 (공통)"""
        CommonUtils.try_import_or_install("requests")
        import requests

        for attempt in range(1, max_retry + 1):
            try:
                print(f"[Attempt {attempt}] Downloading from {url}")
                with requests.get(url, stream=True) as r:
                    r.raise_for_status()
                    with open(file_path, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            f.write(chunk)
                return True
            except Exception as e:
                print(f"Attempt {attempt} failed: {e}")
                if attempt >= max_retry:
                    return False
        return False




def get_environment_paths() -> dict:
    """환경변수 경로 반환"""
    return {
        'D_PK_SYSTEM': os.environ.get('D_PK_SYSTEM', ''),
        'D_PKG_WINDOWS': os.environ.get('D_PKG_WINDOWS', ''),
        'D_PKG_PY': os.environ.get('D_PKG_PY', ''),
        'D_PKG_CACHE_PRIVATE': os.environ.get('D_pkg_cache_private', ''),
        'D_PK_WORKING': os.environ.get('D_PK_WORKING', ''),
        'D_PK_MEMO': os.environ.get('D_PK_MEMO', ''),
        'D_BUSINESS_DEMO': os.environ.get('D_BUSINESS_DEMO', ''),
        'D_DOWNLOADS': os.environ.get('D_DOWNLOADS', ''),
        'D_PKG_LINUX': os.environ.get('D_PKG_LINUX', '')
    }



def save_to_doskey(name: str, command: str) -> bool:
    """Windows에서 doskey로 alias 저장"""
    try:
        doskey_cmd = f'doskey {name}={command}'
        result = subprocess.run(doskey_cmd, shell=True, capture_output=True, text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"Doskey 저장 실패: {e}")
        return False



def setup_pk_environment_with_aliases():
    """PK System 환경변수 설정 및 내장 alias 로드"""
    try:
        # Path 객체로 환경변수 설정 (directories.py에서 가져온 경로들)
        from pkg_py.system_object.directories import (
            D_PK_SYSTEM, D_PKG_PY, D_PKG_WINDOWS, D_PKG_CACHE_PRIVATE,
            D_PK_WORKING, D_PK_MEMO, D_BUSINESS_DEMO, D_DOWNLOADS, D_PKG_LINUX
        )
        # Path 객체로 변환
        d_pk_system = Path(D_PK_SYSTEM)
        d_pkg_py = Path(D_PKG_PY)
        d_pkg_windows = Path(D_PKG_WINDOWS)
        d_pkg_cache_private = Path(D_PKG_CACHE_PRIVATE)
        d_pk_working = Path(D_PK_WORKING)
        d_pk_memo = Path(D_PK_MEMO)
        d_business_demo = Path(D_BUSINESS_DEMO)
        d_downloads = Path(D_DOWNLOADS)
        d_pkg_linux = Path(D_PKG_LINUX)

        # d_userprofile = Path.home()
        # d_downloads = Path(rf"{d_userprofile}\Downloads")
        # d_pk_system = Path(rf"{d_downloads}\pk_system")
        # d_pkg_py = Path(rf"{d_downloads}\pk_system\pkg_py")
        # d_pkg_windows = Path(rf"{d_downloads}\pk_system\pkg_windows")
        # d_pkg_cache_private = Path(rf"{d_downloads}\pk_system\pkg_cache_private")
        # d_pk_working = Path(rf"{d_downloads}\pk_working")
        # d_pk_memo = Path(rf"{d_downloads}\pk_memo")
        # d_business_demo = Path(rf"{d_downloads}\business_demo")
        # d_pkg_linux = Path(rf"{d_downloads}\pk_system\pkg_linux")

        # 환경변수 설정 (Path 객체를 문자열로 변환)
        os.environ['D_PK_SYSTEM'] = str(d_pk_system)
        os.environ['D_PKG_PY'] = str(d_pkg_py)
        os.environ['D_PKG_WINDOWS'] = str(d_pkg_windows)
        os.environ['D_pkg_cache_private'] = str(d_pkg_cache_private)
        os.environ['D_PK_WORKING'] = str(d_pk_working)
        os.environ['D_PK_MEMO'] = str(d_pk_memo)
        os.environ['D_BUSINESS_DEMO'] = str(d_business_demo)
        os.environ['D_DOWNLOADS'] = str(d_downloads)
        os.environ['D_PKG_LINUX'] = str(d_pkg_linux)


        
        # print("PK System 환경변수 설정 완료")
        return True

    except Exception as e:
        print(f"환경변수 설정 실패: {e}")
        return False


class PlatformManager(ABC):
    """플랫폼별 관리자 추상 클래스"""

    def __init__(self):
        self.utils = CommonUtils()

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
        """가상환경 Python으로 패키지 설치"""
        pass

    @abstractmethod
    def test_venv_python(self) -> bool:
        """가상환경 Python 테스트"""
        pass


def ensure_pk_system_enabled():
    """PK System 활성화 메인 함수 (리팩토링된 버전)"""
    import os
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.system_object.directories import D_PKG_WINDOWS, D_PKG_LINUX
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

    current_os = CommonUtils.detect_os()
    print(f" PK System Enabler (Refactored Version)")
    print("=" * 50)
    print(f"️ OS: {current_os}")

    # 플랫폼별 관리자 생성
    if is_os_windows():
        from pkg_py.functions_split.ensure_pk_system_enabled_windows import WindowsManager
        manager = WindowsManager()
        os.chdir(str(Path(D_PKG_WINDOWS)))
        total_steps = 6
    elif is_os_wsl_linux() or is_os_linux():
        from pkg_py.functions_split.ensure_pk_system_enabled_linux import LinuxManager
        manager = LinuxManager()
        os.chdir(str(Path(D_PKG_LINUX)))
        ensure_command_excuted_to_os(cmd='bash pkg_linux/ensure_pk_system_enabled.sh')
        total_steps = 6
    else:
        ensure_guided_not_prepared_yet()
        print(f" 지원되지 않는 OS입니다: {current_os}")
        sys.exit(1)

    # Step 1: UV 설치
    CommonUtils.print_step(1, total_steps, "Installing uv")
    if not manager.install_uv():
        print(f"\n UV 설치 실패 - 설치를 중단합니다.")
        sys.exit(1)

    # Step 2: FZF 설치
    CommonUtils.print_step(2, total_steps, "Installing fzf")
    if not manager.install_fzf():
        print(f"\n FZF 설치 실패 - 설치를 중단합니다.")
        sys.exit(1)

    # Step 3: PATH 설정
    CommonUtils.print_step(3, total_steps, "Setting up PATH")
    if not manager.setup_path():
        print(f"\n PATH 설정 실패 - 설치를 중단합니다.")
        sys.exit(1)

    # Step 4: 별칭 설정
    CommonUtils.print_step(4, total_steps, "Setting up aliases")
    if not manager.setup_aliases():
        print(f"\n 별칭 설정 실패 - 설치를 중단합니다.")
        sys.exit(1)

    # Step 5: UV 패키지 동기화
    CommonUtils.print_step(5, total_steps, "Syncing uv packages")
    if not manager.sync_uv_packages():
        print(f"\n UV 패키지 동기화 실패 - 설치를 중단합니다.")
        sys.exit(1)

    # Step 6: 가상환경 패키지 설치 및 테스트
    CommonUtils.print_step(6, total_steps, "Installing and testing venv packages")
    if not manager.install_packages_with_venv_python():
        print(f"\n 가상환경 패키지 설치 실패 - 설치를 중단합니다.")
        sys.exit(1)

    if not manager.test_venv_python():
        print(f"\n 가상환경 Python 테스트 실패 - 설치를 중단합니다.")
        sys.exit(1)

    print("\n 모든 단계가 성공적으로 완료되었습니다!", "green")

    if is_os_wsl_linux() or is_os_linux():
        print("\n 변경사항을 적용하려면 새 터미널을 열거나 다음 명령어를 실행하세요:")
        print("   source ~/.bashrc")
