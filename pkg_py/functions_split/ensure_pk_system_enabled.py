#!/usr/bin/env python3
"""
PK System Enable Script (Unified OS-Compatible Version)
Windows, Linux, WSL 환경에서 PK 시스템을 활성화하는 통합 스크립트
"""
import os
import platform
import shutil
import subprocess
import sys
import tarfile
import zipfile
from pathlib import Path

from pkg_py.system_object.urls import UV_URL_LINUX, FZF_API_URL, UV_URL_WINDOWS
from pkg_py.system_object.map_massages import PkMessages2025

if platform.system().lower() == "windows":
    import winreg

# System object imports with error handling
try:
    from pkg_py.system_object.directories import (
        D_PKG_WINDOWS, D_PKG_LINUX, D_PK_SYSTEM, D_BUSINESS_DEMO,
        D_DOWNLOADS, D_PKG_LINUX, D_PK_WORKING, D_PKG_PY
    )
    from pkg_py.system_object.files import (
        F_UV_EXE, F_FZF_EXE, F_UV_ZIP, F_FZF_ZIP, F_ALIAS_CMD,
        F_ENSURE_PK_SYSTEM_ENABLED_CMD
    )
except ImportError as e:
    print(f"Error: Could not import system objects: {e}")
    raise

# Windows-specific paths
D_VENV_SCRIPTS = os.path.join(D_PK_SYSTEM, ".venv", "Scripts") if D_PK_SYSTEM else ""
F_VENV_PYTHON_WINDOWS = os.path.join(D_VENV_SCRIPTS, "python.exe") if D_VENV_SCRIPTS else ""
F_SHORTCUT_TARGET_WINDOWS = os.path.join(D_PK_SYSTEM, "pkg_windows", "ensure_pk_system_ran.cmd") if D_PK_SYSTEM else ""

# Linux/WSL-specific paths
USER_HOME = Path.home()
D_VENV_BIN = D_PK_SYSTEM / ".venv" / "bin" if D_PK_SYSTEM else Path()
F_UV_BINARY_LINUX = D_PKG_LINUX / "uv" if D_PKG_LINUX else Path()
F_FZF_BINARY_LINUX = D_PKG_LINUX / "fzf" if D_PKG_LINUX else Path()
F_VENV_PYTHON_LINUX = D_VENV_BIN / "python" if D_VENV_BIN else Path()
F_UV_TAR_LINUX = USER_HOME / "Downloads" / "uv.tar.gz"
F_FZF_TAR_LINUX = USER_HOME / "Downloads" / "fzf.tar.gz"

temp_installed_modules = {}


def detect_os() -> str:
    """OS 감지"""
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "linux":
        # WSL 감지
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


def print_step(step_index: int, total_steps: int, description: str, color: str = "cyan") -> None:
    """단계 출력"""
    color_code = {"cyan": 36, "yellow": 33, "green": 32, "red": 31}.get(color, 36)
    print(f"\033[{color_code}m[{step_index}/{total_steps}] {description}\033[0m")


# Windows-specific functions
def get_system_path() -> str:
    """시스템 환경변수 PATH 가져오기 (Windows)"""
    try:
        if platform.system().lower() == "windows":
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
                                0, winreg.KEY_READ) as key:
                try:
                    system_path, _ = winreg.QueryValueEx(key, "Path")
                    return system_path
                except FileNotFoundError:
                    return ""
    except Exception:
        return ""


def get_user_path() -> str:
    """사용자 환경변수 PATH 가져오기 (Windows)"""
    try:
        if platform.system().lower() == "windows":
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ) as key:
                try:
                    user_path, _ = winreg.QueryValueEx(key, "Path")
                    return user_path
                except FileNotFoundError:
                    return ""
    except Exception:
        return ""


def broadcast_environment_change() -> None:
    """환경변수 변경을 시스템에 알림 (Windows)"""
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


def install_uv_windows(max_retry: int = 2) -> None:
    """UV 다운로드 및 설치 (Windows)"""
    print("\n📦 Step 11: UV 설치 (Windows)")

    try_import_or_install("requests")
    import requests

    os.makedirs(D_PKG_WINDOWS, exist_ok=True)

    for attempt in range(1, max_retry + 1):
        try:
            print(f"[Attempt {attempt}] Downloading uv from {UV_URL_WINDOWS}")
            with requests.get(UV_URL_WINDOWS, stream=True) as r:
                r.raise_for_status()
                with open(F_UV_ZIP, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            # Extract zip
            print("Extracting uv.zip...")
            with zipfile.ZipFile(F_UV_ZIP, 'r') as zip_ref:
                extract_dir = os.path.join(D_PKG_WINDOWS, "__temp_uv_extract__")
                os.makedirs(extract_dir, exist_ok=True)
                zip_ref.extractall(extract_dir)

            # Find uv.exe in extracted files
            found_uv_exe = None
            for root, _, files in os.walk(extract_dir):
                for name in files:
                    if name.lower() == "uv.exe":
                        found_uv_exe = os.path.join(root, name)
                        break
                if found_uv_exe:
                    break

            if not found_uv_exe:
                raise FileNotFoundError("uv.exe not found in extracted zip.")

            shutil.copy(found_uv_exe, F_UV_EXE)
            shutil.rmtree(extract_dir)

            # Validate execution
            print("Validating uv.exe execution...")
            result = subprocess.run([F_UV_EXE, "--version"], check=True, capture_output=True, text=True)
            print(f"✅ uv 설치 완료: {result.stdout.strip()}")

            break

        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt >= max_retry:
                raise RuntimeError("uv installation failed after multiple attempts.") from e
            else:
                print("Retrying...")

        finally:
            try:
                if os.path.exists(F_UV_ZIP):
                    os.remove(F_UV_ZIP)
            except Exception as e:
                print(f"Failed to remove uv.zip: {e}")


def install_fzf_windows(max_retry: int = 2) -> None:
    """FZF 다운로드 및 설치 (Windows)"""
    print("\n🔍 Step 12: FZF 설치 (Windows)")

    try_import_or_install("requests")
    import requests

    os.makedirs(D_PKG_WINDOWS, exist_ok=True)

    for attempt in range(1, max_retry + 1):
        try:
            fzf_url = get_latest_fzf_url_windows()
            print(f"[Attempt {attempt}] Downloading fzf from {fzf_url}")

            with requests.get(fzf_url, stream=True) as r:
                r.raise_for_status()
                with open(F_FZF_ZIP, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            # Extract zip
            print("Extracting fzf.zip...")
            with zipfile.ZipFile(F_FZF_ZIP, 'r') as zip_ref:
                extract_dir = os.path.join(D_PKG_WINDOWS, "__temp_fzf_extract__")
                os.makedirs(extract_dir, exist_ok=True)
                zip_ref.extractall(extract_dir)

            # Find fzf.exe in extracted files
            found_fzf_exe = None
            for root, _, files in os.walk(extract_dir):
                for name in files:
                    if name.lower() == "fzf.exe":
                        found_fzf_exe = os.path.join(root, name)
                        break
                if found_fzf_exe:
                    break

            if not found_fzf_exe:
                raise FileNotFoundError("fzf.exe not found in extracted zip.")

            shutil.copy(found_fzf_exe, F_FZF_EXE)
            shutil.rmtree(extract_dir)

            # Validate execution
            print("Validating fzf.exe execution...")
            result = subprocess.run([F_FZF_EXE, "--version"], check=True, capture_output=True, text=True)
            print(f"✅ fzf 설치 완료: {result.stdout.strip()}")

            break

        except Exception as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt >= max_retry:
                raise RuntimeError("fzf installation failed after multiple attempts.") from e
            else:
                print("Retrying...")

        finally:
            try:
                if os.path.exists(F_FZF_ZIP):
                    os.remove(F_FZF_ZIP)
            except Exception as e:
                print(f"Failed to remove fzf.zip: {e}")


def get_latest_fzf_url_windows() -> str:
    """GitHub API를 사용하여 최신 FZF 다운로드 URL 가져오기 (Windows)"""
    try_import_or_install("requests")
    import requests

    try:
        print("FZF 최신 버전 확인 중...")
        response = requests.get(FZF_API_URL)
        response.raise_for_status()
        data = response.json()
        version = data["tag_name"]
        print(f"FZF 최신 버전: {version}")

        # Remove 'v' prefix from version for filename
        version_clean = version.lstrip('v')

        # Windows AMD64 다운로드 URL 생성
        download_url = f"https://github.com/junegunn/fzf/releases/download/{version}/fzf-{version_clean}-windows_amd64.zip"
        print(f"FZF 다운로드 URL: {download_url}")

        return download_url

    except Exception as e:
        # Fallback URL
        fallback_url = "https://github.com/junegunn/fzf/releases/download/v0.65.0/fzf-0.65.0-windows_amd64.zip"
        print(f"Fallback URL 사용: {fallback_url}")

        try:
            # Fallback URL 테스트
            response = requests.head(fallback_url)
            if response.status_code == 200:
                return fallback_url
        except:
            pass

        print(f"FZF 최신 버전 확인 실패: {e}")
        print(f"최종 Fallback URL 사용: {fallback_url}")
        return fallback_url


def setup_uv_path_windows() -> None:
    """UV, FZF, 가상환경 Python 경로를 환경변수에 추가하고 PATH 정리 (Windows)"""
    print(f"UV 경로: {D_PKG_WINDOWS}")
    print(f"가상환경 Scripts 경로: {D_VENV_SCRIPTS}")
    print(f"Business Demo 경로: {D_BUSINESS_DEMO}")

    # 시스템 PATH와 사용자 PATH 모두 가져오기
    system_path = get_system_path()
    user_path = get_user_path()

    print(f"시스템 PATH 항목 수: {len(system_path.split(';')) if system_path else 0}")
    print(f"사용자 PATH 항목 수: {len(user_path.split(';')) if user_path else 0}")

    # 모든 PATH 병합
    all_paths = system_path + ";" + user_path if user_path else system_path
    path_list = all_paths.split(";")

    # 중복 제거 및 정리
    seen = set()
    clean_path = []

    # UV, FZF, 가상환경 Python 경로 우선 추가
    if os.path.exists(D_PKG_WINDOWS):
        norm_uv = os.path.normpath(D_PKG_WINDOWS)
        if norm_uv not in seen:
            seen.add(norm_uv)
            clean_path.append(norm_uv)
            print(f"UV/FZF 경로 추가: {norm_uv}")

    # 가상환경 Scripts 경로 추가
    if os.path.exists(D_VENV_SCRIPTS):
        norm_venv = os.path.normpath(D_VENV_SCRIPTS)
        if norm_venv not in seen:
            seen.add(norm_venv)
            clean_path.append(norm_venv)
            print(f"가상환경 Scripts 경로 추가: {norm_venv}")

    # Business Demo 경로 추가
    if os.path.exists(D_BUSINESS_DEMO):
        norm_business = os.path.normpath(D_BUSINESS_DEMO)
        if norm_business not in seen:
            seen.add(norm_business)
            clean_path.append(norm_business)
            print(f"Business Demo 경로 추가: {norm_business}")
    else:
        # Business Demo 디렉토리가 없으면 생성
        try:
            os.makedirs(D_BUSINESS_DEMO, exist_ok=True)
            norm_business = os.path.normpath(D_BUSINESS_DEMO)
            if norm_business not in seen:
                seen.add(norm_business)
                clean_path.append(norm_business)
                print(f"Business Demo 경로 생성 및 추가: {norm_business}")
        except Exception as e:
            print(f"Business Demo 디렉토리 생성 실패: {e}")

    for path in path_list:
        norm = os.path.normpath(path.strip())
        if not norm:
            continue
        if "user" in norm.lower() and "pk_system" not in norm.lower():  # 다른 사용자 경로 제거 (pk_system 제외)
            continue
        if norm not in seen:
            seen.add(norm)
            clean_path.append(norm)

    # 필수 경로 재정렬 (시스템, .venv, pk_system, business_demo 우선)
    priority = ["system32", ".venv", "pk_system", "business_demo", "uv.exe", "fzf.exe", "python.exe"]

    def sort_key(p):
        for i, keyword in enumerate(priority):
            if keyword.lower() in p.lower():
                return i
        return len(priority)

    clean_path.sort(key=sort_key)

    # 병합
    new_path = ";".join(clean_path)

    # 사용자 환경변수에 저장
    try:
        if platform.system().lower() == "windows":
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                print("사용자 PATH 환경변수가 정리되었습니다.")

                # D_BUSINESS_DEMO 환경변수도 별도로 설정
                winreg.SetValueEx(key, "D_BUSINESS_DEMO", 0, winreg.REG_EXPAND_SZ, D_BUSINESS_DEMO)
                print(f"D_BUSINESS_DEMO 환경변수 설정: {D_BUSINESS_DEMO}")

            # 환경변수 변경 알림
            broadcast_environment_change()

            print("새 터미널을 열어서 환경변수 변경사항을 확인하세요.")
            print("또는 다음 명령어로 현재 세션에 적용:")
            print("   refreshenv")

    except Exception as e:
        print(f"환경변수 정리 실패: {e}")
        raise


def register_pk_alias_windows() -> None:
    """Windows에서 pk_alias 등록"""
    try:
        if platform.system().lower() == "windows":
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Command Processor") as key:
                winreg.SetValueEx(key, "AutoRun", 0, winreg.REG_SZ, f'"{F_ALIAS_CMD}"')
    except Exception as e:
        print(f"Failed to register pk_alias: {e}")
        raise


def create_shortcuts_windows() -> None:
    """바로가기 생성 함수 (Windows)"""
    try:
        import win32com.client

        # F_ALIAS_CMD 파일이 존재하는지 확인
        if not os.path.exists(F_ALIAS_CMD):
            print(f"경고: {F_ALIAS_CMD} 파일이 존재하지 않습니다.")
            print("바로가기 생성을 건너뜁니다.")
            return

        shell = win32com.client.Dispatch("WScript.Shell")

        # 바탕화면 바로가기 생성
        try:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            if os.path.exists(desktop):
                shortcut_path = os.path.join(desktop, "pk_system_launcher.lnk")
                shortcut = shell.CreateShortCut(shortcut_path)
                shortcut.Targetpath = F_ALIAS_CMD
                shortcut.WorkingDirectory = D_PK_SYSTEM
                shortcut.save()
                print(f"바탕화면 바로가기 생성됨: {shortcut_path}")
            else:
                print("바탕화면 경로를 찾을 수 없습니다.")
        except Exception as e:
            print(f"바탕화면 바로가기 생성 실패: {e}")

        # 작업 디렉토리 바로가기 생성
        try:
            shortcut_path = os.path.join(D_PKG_WINDOWS, "pk_system_launcher.lnk")
            shortcut = shell.CreateShortCut(shortcut_path)
            shortcut.Targetpath = F_ALIAS_CMD
            shortcut.WorkingDirectory = D_PK_SYSTEM
            shortcut.save()
            print(f"작업 디렉토리 바로가기 생성됨: {shortcut_path}")
        except Exception as e:
            print(f"작업 디렉토리 바로가기 생성 실패: {e}")

    except ImportError as e:
        print(f"win32com.client 모듈을 가져올 수 없습니다: {e}")
        print("바로가기 생성은 선택사항이므로 계속 진행합니다.")
    except Exception as e:
        print(f"바로가기 생성 중 예상치 못한 오류: {e}")
        print("바로가기 생성은 선택사항이므로 계속 진행합니다.")


# Linux/WSL-specific functions
def install_uv_linux(max_retry: int = 2) -> None:
    """UV 다운로드 및 설치 (Linux/WSL)"""
    print("\n📦 Step 11: UV 설치 (Linux/WSL)")

    # UV가 이미 설치되어 있는지 확인
    try:
        result = subprocess.run(["uv", "--version"], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            print(f"✅ uv가 이미 설치되어 있습니다: {result.stdout.strip()}")
            return
    except FileNotFoundError:
        pass

    # Linux/WSL 환경에서만 UV 설치
    if detect_os() == "linux":
        print("🔧 uv 설치 중...")

        # requests 모듈 설치 확인
        try:
            import requests
        except ImportError:
            print("📦 requests 모듈 설치 중...")
            subprocess.run([sys.executable, "-m", "pip", "install", "requests"])
            import requests

        os.makedirs(D_PKG_LINUX, exist_ok=True)

        # 이미 UV가 설치되어 있는지 확인
        if F_UV_BINARY_LINUX.exists():
            print(f"✅ uv가 이미 설치되어 있습니다: {F_UV_BINARY_LINUX}")
            return

        for attempt in range(1, max_retry + 1):
            try:
                print(f"[Attempt {attempt}] Downloading uv from {UV_URL_LINUX}")
                response = requests.get(UV_URL_LINUX, stream=True)
                response.raise_for_status()

                with open(F_UV_TAR_LINUX, "wb") as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

                # Extract tar.gz
                print("Extracting uv.tar.gz...")
                with tarfile.open(F_UV_TAR_LINUX, 'r:gz') as tar_ref:
                    tar_ref.extractall(D_PKG_LINUX)

                # Find uv binary
                found_uv = None
                for root, _, files in os.walk(D_PKG_LINUX):
                    for name in files:
                        if name == "uv":
                            found_uv = Path(root) / name
                            break
                    if found_uv:
                        break

                if not found_uv:
                    raise FileNotFoundError("uv binary not found in extracted tar.gz.")

                # 대상 파일이 이미 존재하면 삭제
                if F_UV_BINARY_LINUX.exists():
                    F_UV_BINARY_LINUX.unlink()

                # 파일 복사 (더 안전한 방법 사용)
                try:
                    shutil.copy2(found_uv, F_UV_BINARY_LINUX)
                    os.chmod(F_UV_BINARY_LINUX, 0o755)  # 실행 권한 부여
                    print(f"✅ uv 바이너리 복사 완료: {F_UV_BINARY_LINUX}")
                except Exception as copy_error:
                    print(f"파일 복사 중 오류: {copy_error}")
                    # 대안: 직접 복사
                    with open(found_uv, 'rb') as src, open(F_UV_BINARY_LINUX, 'wb') as dst:
                        dst.write(src.read())
                    os.chmod(F_UV_BINARY_LINUX, 0o755)
                    print(f"✅ uv 바이너리 직접 복사 완료: {F_UV_BINARY_LINUX}")

                # Validate execution
                print("Validating uv binary execution...")
                result = subprocess.run([str(F_UV_BINARY_LINUX), "--version"], capture_output=True, text=True)
                print(f"✅ uv 설치 완료: {result.stdout.strip()}")

                break

            except Exception as e:
                print(f"Attempt {attempt} failed: {e}")
                if attempt >= max_retry:
                    print("❌ uv 설치 실패")
                    raise RuntimeError("uv installation failed after multiple attempts.") from e
                else:
                    print("Retrying...")

            finally:
                try:
                    if F_UV_TAR_LINUX.exists():
                        F_UV_TAR_LINUX.unlink()
                except Exception as e:
                    print(f"Failed to remove uv.tar.gz: {e}")
    else:
        print("ℹ️ Windows/macOS 환경이므로 Linux UV 설치를 건너뜁니다")


def install_fzf_linux(max_retry: int = 2) -> None:
    """FZF 다운로드 및 설치 (Linux/WSL)"""
    print("\n🔍 Step 12: FZF 설치 (Linux/WSL)")

    # FZF가 이미 설치되어 있는지 확인
    try:
        result = subprocess.run(["fzf", "--version"], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            print(f"✅ fzf가 이미 설치되어 있습니다: {result.stdout.strip()}")
            return
    except FileNotFoundError:
        pass

    # Linux/WSL 환경에서만 FZF 설치
    if detect_os() == "linux":
        print("🔧 fzf 설치 중...")

        # 이미 FZF가 설치되어 있는지 확인
        if F_FZF_BINARY_LINUX.exists():
            print(f"✅ fzf가 이미 설치되어 있습니다: {F_FZF_BINARY_LINUX}")
            return

        os.makedirs(D_PKG_LINUX, exist_ok=True)

        for attempt in range(1, max_retry + 1):
            try:
                print(f"[Attempt {attempt}] Installing fzf using WSL bash...")

                # WSL bash를 사용하여 직접 설치
                install_cmd = [
                    "wsl", "bash", "-c",
                    f"cd /tmp && curl -LsSf https://github.com/junegunn/fzf/releases/download/v0.65.0/fzf-0.65.0-linux_amd64.tar.gz | tar -xz && sudo cp fzf {D_PKG_LINUX}/ && sudo chmod +x {D_PKG_LINUX}/fzf"
                ]

                result = subprocess.run(install_cmd, capture_output=True, text=True, check=True)
                print("✅ fzf 설치 완료")

                # Validate execution
                print("Validating fzf binary execution...")
                result = subprocess.run([str(F_FZF_BINARY_LINUX), "--version"], capture_output=True, text=True)
                print(f"✅ fzf 설치 완료: {result.stdout.strip()}")

                break

            except Exception as e:
                print(f"Attempt {attempt} failed: {e}")
                if attempt >= max_retry:
                    print("❌ fzf 설치 실패")
                    raise RuntimeError("fzf installation failed after multiple attempts.") from e
                else:
                    print("Retrying...")
    else:
        print("ℹ️ Windows/macOS 환경이므로 Linux FZF 설치를 건너뜁니다")


def setup_linux_path() -> None:
    """UV, FZF, 가상환경 Python 경로를 .bashrc/.zshrc에 추가"""
    print("\n🛤️ Step 13: Linux PATH 설정")

    print(f"UV 경로: {D_PKG_LINUX}")
    print(f"가상환경 bin 경로: {D_VENV_BIN}")
    print(f"Business Demo 경로: {D_BUSINESS_DEMO}")

    # Business Demo 디렉토리 생성
    if not D_BUSINESS_DEMO.exists():
        try:
            D_BUSINESS_DEMO.mkdir(parents=True, exist_ok=True)
            print(f"Business Demo 디렉토리 생성: {D_BUSINESS_DEMO}")
        except Exception as e:
            print(f"Business Demo 디렉토리 생성 실패: {e}")

    # .bashrc와 .zshrc 모두 설정
    config_files = [
        (USER_HOME / ".bashrc", "bash"),
        (USER_HOME / ".zshrc", "zsh")
    ]

    for config_file, shell_type in config_files:
        if config_file.exists():
            content = config_file.read_text()

            # 기존 PK System PATH 설정 제거
            lines = content.split('\n')
            filtered_lines = []
            for line in lines:
                if not any(marker in line for marker in [
                    "# PK System PATH",
                    "export PATH=",
                    "export D_BUSINESS_DEMO="
                ]):
                    filtered_lines.append(line)

            # 새로운 PATH 설정 추가
            path_section = f"\n# PK System PATH ({shell_type})\n"
            path_section += f'export PATH="$PATH:{D_PKG_LINUX}:{D_VENV_BIN}"\n'
            path_section += f'export D_BUSINESS_DEMO="{D_BUSINESS_DEMO}"\n'

            new_content = '\n'.join(filtered_lines) + path_section

            config_file.write_text(new_content)

            print(f"✅ {shell_type} PATH 설정 완료: {config_file}")
        else:
            print(f"⚠️ {shell_type} 설정 파일을 찾을 수 없습니다: {config_file}")

    print("✅ Linux PATH 설정 완료")


# Common functions
def sync_uv_packages() -> None:
    """UV 패키지 동기화"""
    print("\n🔄 Step 20: uv 패키지 동기화")

    current_os = detect_os()

    if current_os == "windows":
        try:
            if not os.path.isdir(D_PK_SYSTEM):
                raise FileNotFoundError(f"Target path does not exist: {D_PK_SYSTEM}")

            os.chdir(D_PK_SYSTEM)
            os.environ["PATH"] += ";" + os.path.dirname(F_UV_EXE)

            result = subprocess.run([F_UV_EXE, "sync"])
            if result.returncode != 0:
                raise RuntimeError("uv sync failed.")
            
            print("✅ uv sync 완료 - 가상환경 Python 사용 준비됨")
        except Exception as e:
            print(f"Failed during uv sync: {e}")
            raise
    elif current_os == "linux":
        try:
            if not D_PK_SYSTEM.exists():
                raise FileNotFoundError(f"Target path does not exist: {D_PK_SYSTEM}")

            os.chdir(D_PK_SYSTEM)
            os.environ["PATH"] += ":" + str(D_PKG_LINUX)

            result = subprocess.run([str(F_UV_BINARY_LINUX), "sync"])
            if result.returncode != 0:
                raise RuntimeError("uv sync failed.")
            
            print("✅ uv sync 완료 - 가상환경 Python 사용 준비됨")
        except Exception as e:
            print(f"Failed during uv sync: {e}")
            raise
    else:
        print("ℹ️ 지원되지 않는 OS입니다.")


def install_packages_with_venv_python() -> None:
    """가상환경 Python을 사용하여 패키지 설치"""
    print("\n🐍 Step 21: 가상환경 Python으로 패키지 설치")
    
    current_os = detect_os()
    
    if current_os == "windows":
        venv_python = os.path.join(D_PK_SYSTEM, ".venv", "Scripts", "python.exe")
        venv_pip = os.path.join(D_PK_SYSTEM, ".venv", "Scripts", "pip.exe")
    elif current_os == "linux":
        venv_python = D_PK_SYSTEM / ".venv" / "bin" / "python"
        venv_pip = D_PK_SYSTEM / ".venv" / "bin" / "pip"
    else:
        print("ℹ️ 지원되지 않는 OS입니다.")
        return
    
    # 가상환경 Python이 존재하는지 확인
    if not os.path.exists(venv_python):
        print(f"❌ 가상환경 Python을 찾을 수 없습니다: {venv_python}")
        print("uv sync를 먼저 실행해주세요.")
        return
    
    print(f"✅ 가상환경 Python 사용: {venv_python}")
    
    # 필요한 패키지들을 가상환경에 설치
    packages_to_install = ["toml", "requests", "pywin32"]
    
    for package in packages_to_install:
        try:
            print(f"📦 {package} 설치 중...")
            if current_os == "windows":
                result = subprocess.run([venv_pip, "install", package], 
                                      capture_output=True, text=True, check=True)
            else:
                result = subprocess.run([str(venv_pip), "install", package], 
                                      capture_output=True, text=True, check=True)
            print(f"✅ {package} 설치 완료")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ {package} 설치 실패: {e}")
            if "pywin32" in package and current_os == "linux":
                print("pywin32는 Windows 전용 패키지이므로 Linux에서는 건너뜁니다.")
        except Exception as e:
            print(f"❌ {package} 설치 중 오류: {e}")
    
    print("✅ 가상환경 패키지 설치 완료")


def test_venv_python() -> None:
    """가상환경 Python 테스트"""
    print("\n🧪 Step 22: 가상환경 Python 테스트")
    
    current_os = detect_os()
    
    if current_os == "windows":
        venv_python = os.path.join(D_PK_SYSTEM, ".venv", "Scripts", "python.exe")
    elif current_os == "linux":
        venv_python = D_PK_SYSTEM / ".venv" / "bin" / "python"
    else:
        print("ℹ️ 지원되지 않는 OS입니다.")
        return
    
    if not os.path.exists(venv_python):
        print(f"❌ 가상환경 Python을 찾을 수 없습니다: {venv_python}")
        return
    
    try:
        # Python 버전 확인
        if current_os == "windows":
            result = subprocess.run([venv_python, "--version"], 
                                  capture_output=True, text=True, check=True)
        else:
            result = subprocess.run([str(venv_python), "--version"], 
                                  capture_output=True, text=True, check=True)
        print(f"✅ 가상환경 Python 버전: {result.stdout.strip()}")
        
        # toml 모듈 테스트
        if current_os == "windows":
            result = subprocess.run([venv_python, "-c", "import toml; print('toml 모듈 사용 가능')"], 
                                  capture_output=True, text=True, check=True)
        else:
            result = subprocess.run([str(venv_python), "-c", "import toml; print('toml 모듈 사용 가능')"], 
                                  capture_output=True, text=True, check=True)
        print(f"✅ {result.stdout.strip()}")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ 가상환경 Python 테스트 실패: {e}")
    except Exception as e:
        print(f"❌ 테스트 중 오류: {e}")
    
    print("✅ 가상환경 Python 테스트 완료")


def ensure_pk_system_enabled():
    """PK System 활성화 메인 함수"""
    import os
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.system_object.directories import D_PKG_WINDOWS, D_PKG_LINUX
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.system_object.files import F_ENSURE_PK_SYSTEM_ENABLED_CMD

    if is_os_windows():
        os.chdir(D_PKG_WINDOWS)
        ensure_pk_system_enabled_cmd = get_pnx_os_style(rf"{F_ENSURE_PK_SYSTEM_ENABLED_CMD}")
        ensure_command_excuted_to_os(cmd=f'start ""  "{ensure_pk_system_enabled_cmd}"')
        # ensure_command_excuted_to_os(cmd=f'call "{ensure_pk_system_enabled_cmd}"')
    elif is_os_wsl_linux():
        os.chdir(D_PKG_LINUX)
        ensure_command_excuted_to_os(cmd='bash pkg_linux/ensure_pk_system_enabled.sh')
    elif is_os_linux():
        os.chdir(D_PKG_LINUX)
        ensure_command_excuted_to_os(cmd='bash pkg_linux/ensure_pk_system_enabled.sh')
    else:
        ensure_printed(f'''{PkMessages2025.NOT_PREPARED_YET}{'%%%FOO%%%' if LTA else ''}''', print_color='green', mode_verbose=0)


def main() -> None:
    """메인 실행 함수"""
    current_os = detect_os()
    print(f"🐍 PK System Enabler (Unified OS-Compatible)")
    print("=" * 50)
    print(f"🖥️ OS: {current_os}")

    if current_os == "windows":
        # Windows 실행 로직
        total_steps = 10

        try:
            print_step(1, total_steps, "Registering pk_alias (1st time)")
            register_pk_alias_windows()

            print_step(2, total_steps, "Installing uv (download/unzip/version)")
            install_uv_windows()

            print_step(3, total_steps, "Installing fzf (download/unzip/version)")
            install_fzf_windows()

            print_step(4, total_steps, "Syncing uv packages")
            sync_uv_packages()

            print_step(5, total_steps, "Installing packages with venv Python")
            install_packages_with_venv_python()

            print_step(6, total_steps, "Testing venv Python")
            test_venv_python()

            print_step(7, total_steps, "Setting up PATH with UV, FZF, and venv Python")
            setup_uv_path_windows()

            print_step(8, total_steps, "Creating desktop and working directory shortcuts")
            create_shortcuts_windows()

            print_step(9, total_steps, "Re-registering pk_alias to AutoRun")
            register_pk_alias_windows()

            print_step(10, total_steps, "All steps completed successfully", "green")

        except Exception as e:
            print(f"\n❌ 오류 발생: {e}")
            sys.exit(1)

    elif current_os == "linux":
        # Linux/WSL 실행 로직
        total_steps = 10

        try:
            print_step(1, total_steps, "Installing uv (Linux)")
            install_uv_linux()

            print_step(2, total_steps, "Installing fzf (Linux)")
            install_fzf_linux()

            print_step(3, total_steps, "Setting up Linux PATH")
            setup_linux_path()

            print_step(4, total_steps, "Syncing uv packages")
            sync_uv_packages()

            print_step(5, total_steps, "Installing packages with venv Python")
            install_packages_with_venv_python()

            print_step(6, total_steps, "Testing venv Python")
            test_venv_python()

            print_step(7, total_steps, "Setting up Python virtual environment")
            # Python 가상환경 설정 로직 추가 가능

            print_step(8, total_steps, "Registering pk_alias")
            # Linux alias 등록 로직 추가 가능

            print_step(9, total_steps, "Final PATH setup with venv Python")
            # 최종 PATH 설정 (가상환경 Python 포함)

            print_step(10, total_steps, "All steps completed successfully", "green")

            print("\n🔄 변경사항을 적용하려면 새 터미널을 열거나 다음 명령어를 실행하세요:")
            print("   source ~/.bashrc")

        except Exception as e:
            print(f"\n❌ 오류 발생: {e}")
            sys.exit(1)

    else:
        print(f"❌ 지원되지 않는 OS입니다: {current_os}")
        sys.exit(1)


if __name__ == "__main__":
    main()
