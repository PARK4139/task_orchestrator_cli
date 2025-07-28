import os
import subprocess
import sys
import traceback
import zipfile
import winreg
import json
from typing import Callable, List, Tuple

# ──────────────────────────────────────────────
# Constants
UV_URL = "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip"
FZF_API_URL = "https://api.github.com/repos/junegunn/fzf/releases/latest"
USER_PROFILE = os.environ["USERPROFILE"]
D_PK_SYSTEM = os.path.join(USER_PROFILE, "Downloads", "pk_system")
D_PKG_WINDOWS = os.path.join(D_PK_SYSTEM,   "pkg_windows")
D_VENV_SCRIPTS = os.path.join(D_PK_SYSTEM, ".venv", "Scripts")
F_UV_EXE = os.path.join(D_PKG_WINDOWS, "uv.exe")
F_FZF_EXE = os.path.join(D_PKG_WINDOWS, "fzf.exe")
F_VENV_PYTHON = os.path.join(D_VENV_SCRIPTS, "python.exe")
F_UV_ZIP = os.path.join(USER_PROFILE, "Downloads", "uv.zip")
F_FZF_ZIP = os.path.join(USER_PROFILE, "Downloads", "fzf.zip")
F_ALIAS_CMD = os.path.join(D_PK_SYSTEM, "pkg_windows", "ensure_alias_enabled.cmd")
F_SHORTCUT_TARGET = os.path.join(D_PK_SYSTEM, "pkg_windows", "ensure_pk_system_ran.cmd")

# ──────────────────────────────────────────────
temp_installed_modules = {}

def try_import_or_install(pkg_name: str, import_name: str = None) -> None:
    import_name = import_name or pkg_name
    try:
        globals()[import_name] = __import__(import_name)
        print(f"'{pkg_name}' module is already installed")
        temp_installed_modules[import_name] = False
    except ImportError:
        print(f"⚠️ '{pkg_name}' module not found, attempting to install...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", pkg_name], check=True)
            globals()[import_name] = __import__(import_name)
            temp_installed_modules[import_name] = True
        except Exception as e:
            print(f"❌ Failed to install '{pkg_name}': {e}")
            raise

# ──────────────────────────────────────────────
def print_step(step_index: int, total_steps: int, description: str, color: str = "cyan") -> None:
    color_code = {"cyan": 36, "yellow": 33, "green": 32, "red": 31}.get(color, 36)
    print(f"\033[{color_code}m[{step_index}/{total_steps}] {description}\033[0m")

# ──────────────────────────────────────────────
def get_system_path() -> str:
    """시스템 환경변수 PATH 가져오기"""
    try:
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
    """사용자 환경변수 PATH 가져오기"""
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ) as key:
            try:
                user_path, _ = winreg.QueryValueEx(key, "Path")
                return user_path
            except FileNotFoundError:
                return ""
    except Exception:
        return ""

def broadcast_environment_change() -> None:
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
            print("✅ 환경변수 변경 알림이 전송되었습니다.")
        else:
            print("⚠️ 환경변수 변경 알림 전송 실패")
    except Exception as e:
        print(f"⚠️ 환경변수 변경 알림 실패: {e}")

def verify_uv_in_path() -> bool:
    """UV가 PATH에 있는지 확인"""
    try:
        result = subprocess.run(['uv', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ UV 확인됨: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ UV 실행 실패: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ UV를 찾을 수 없습니다. PATH에 추가되지 않았을 수 있습니다.")
        return False
    except Exception as e:
        print(f"❌ UV 확인 중 오류: {e}")
        return False

def verify_fzf_in_path() -> bool:
    """FZF가 PATH에 있는지 확인"""
    try:
        result = subprocess.run(['fzf', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ FZF 확인됨: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ FZF 실행 실패: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ FZF를 찾을 수 없습니다. PATH에 추가되지 않았을 수 있습니다.")
        return False
    except Exception as e:
        print(f"❌ FZF 확인 중 오류: {e}")
        return False

def verify_venv_python_in_path() -> bool:
    """가상환경 Python이 PATH에 있는지 확인"""
    try:
        # 가상환경 Python으로 버전 확인
        result = subprocess.run([F_VENV_PYTHON, '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ 가상환경 Python 확인됨: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ 가상환경 Python 실행 실패: {result.stderr}")
            return False
    except FileNotFoundError:
        print("❌ 가상환경 Python을 찾을 수 없습니다. PATH에 추가되지 않았을 수 있습니다.")
        return False
    except Exception as e:
        print(f"❌ 가상환경 Python 확인 중 오류: {e}")
        return False

def get_latest_fzf_url() -> str:
    """GitHub API를 사용하여 최신 FZF 다운로드 URL 가져오기"""
    try_import_or_install("requests")
    import requests
    
    try:
        print("🔍 FZF 최신 버전 확인 중...")
        response = requests.get(FZF_API_URL, timeout=10)
        response.raise_for_status()
        
        release_data = response.json()
        version = release_data['tag_name']
        print(f"✅ FZF 최신 버전: {version}")
        
        # Windows amd64 zip 파일 찾기
        for asset in release_data['assets']:
            if 'windows_amd64.zip' in asset['name']:
                download_url = asset['browser_download_url']
                print(f"✅ FZF 다운로드 URL: {download_url}")
                return download_url
        
        # fallback: 직접 URL 구성
        fallback_url = f"https://github.com/junegunn/fzf/releases/download/{version}/fzf-{version}-windows_amd64.zip"
        print(f"⚠️ Fallback URL 사용: {fallback_url}")
        return fallback_url
        
    except Exception as e:
        print(f"❌ FZF 최신 버전 확인 실패: {e}")
        # 최종 fallback
        fallback_url = "https://github.com/junegunn/fzf/releases/latest/download/fzf-windows_amd64.zip"
        print(f"⚠️ 최종 Fallback URL 사용: {fallback_url}")
        return fallback_url

def install_fzf(max_retry: int = 2) -> None:
    """FZF 설치 (직접 다운로드)"""
    try_import_or_install("requests")
    import requests
    import shutil

    os.makedirs(D_PKG_WINDOWS, exist_ok=True)

    # 최신 FZF URL 가져오기
    fzf_url = get_latest_fzf_url()

    for attempt in range(1, max_retry + 1):
        try:
            print(f"🔁 [Attempt {attempt}] Downloading fzf from {fzf_url}")
            with requests.get(fzf_url, stream=True) as r:
                r.raise_for_status()
                with open(F_FZF_ZIP, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            # Extract zip
            print("📦 Extracting fzf.zip...")
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
            print("⚙️ Validating fzf.exe execution...")
            result = subprocess.run([F_FZF_EXE, "--version"], check=True, capture_output=True, text=True)
            print("✅ fzf version:", result.stdout.strip())

            break  # Success → break retry loop

        except Exception as e:
            print(f"❌ Attempt {attempt} failed: {e}")
            if attempt >= max_retry:
                raise RuntimeError("🚫 fzf installation failed after multiple attempts.") from e
            else:
                print("🔁 Retrying...")

        finally:
            try:
                if os.path.exists(F_FZF_ZIP):
                    os.remove(F_FZF_ZIP)
            except Exception as e:
                print(f"⚠️ Failed to remove fzf.zip: {e}")

def setup_uv_path() -> None:
    """UV, FZF, 가상환경 Python 경로를 환경변수에 추가하고 PATH 정리"""
    print(f" UV 경로: {D_PKG_WINDOWS}")
    print(f" 가상환경 Scripts 경로: {D_VENV_SCRIPTS}")
    
    # 시스템 PATH와 사용자 PATH 모두 가져오기
    system_path = get_system_path()
    user_path = get_user_path()
    
    print(f"📋 시스템 PATH 항목 수: {len(system_path.split(';')) if system_path else 0}")
    print(f"📋 사용자 PATH 항목 수: {len(user_path.split(';')) if user_path else 0}")
    
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
            print(f"✅ UV/FZF 경로 추가: {norm_uv}")
    
    # 가상환경 Scripts 경로 추가
    if os.path.exists(D_VENV_SCRIPTS):
        norm_venv = os.path.normpath(D_VENV_SCRIPTS)
        if norm_venv not in seen:
            seen.add(norm_venv)
            clean_path.append(norm_venv)
            print(f"✅ 가상환경 Scripts 경로 추가: {norm_venv}")
    
    for path in path_list:
        norm = os.path.normpath(path.strip())
        if not norm:
            continue
        if "user" in norm.lower() and "pk_system" not in norm.lower():  # 다른 사용자 경로 제거 (pk_system 제외)
            continue
        if norm not in seen:
            seen.add(norm)
            clean_path.append(norm)
    
    # 필수 경로 재정렬 (시스템, .venv, pk_system 우선)
    priority = ["system32", ".venv", "pk_system", "uv.exe", "fzf.exe", "python.exe"]
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
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
        print("✅ 사용자 PATH 환경변수가 정리되었습니다.")
        
        # 환경변수 변경 알림
        broadcast_environment_change()
        
        print(" 새 터미널을 열어서 환경변수 변경사항을 확인하세요.")
        print("📝 또는 다음 명령어로 현재 세션에 적용:")
        print("   refreshenv")
        
    except Exception as e:
        print(f"❌ 환경변수 정리 실패: {e}")
        raise

# ──────────────────────────────────────────────
def register_pk_alias() -> None:
    try:
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Command Processor") as key:
            winreg.SetValueEx(key, "AutoRun", 0, winreg.REG_SZ, f'"{F_ALIAS_CMD}"')
    except Exception as e:
        print(f"❌ Failed to register pk_alias: {e}")
        raise

# ──────────────────────────────────────────────
def install_uv(max_retry: int = 2) -> None:
    try_import_or_install("requests")
    import requests
    import shutil

    os.makedirs(D_PKG_WINDOWS, exist_ok=True)

    for attempt in range(1, max_retry + 1):
        try:
            print(f"🔁 [Attempt {attempt}] Downloading uv from {UV_URL}")
            with requests.get(UV_URL, stream=True) as r:
                r.raise_for_status()
                with open(F_UV_ZIP, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

            # Extract zip
            print("📦 Extracting uv.zip...")
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
            print("⚙️ Validating uv.exe execution...")
            result = subprocess.run([F_UV_EXE, "--version"], check=True, capture_output=True, text=True)
            print("✅ uv version:", result.stdout.strip())

            break  # Success → break retry loop

        except Exception as e:
            print(f"❌ Attempt {attempt} failed: {e}")
            if attempt >= max_retry:
                raise RuntimeError("🚫 uv installation failed after multiple attempts.") from e
            else:
                print("🔁 Retrying...")

        finally:
            try:
                if os.path.exists(F_UV_ZIP):
                    os.remove(F_UV_ZIP)
            except Exception as e:
                print(f"⚠️ Failed to remove uv.zip: {e}")

# ──────────────────────────────────────────────
def sync_uv_packages() -> None:
    try:
        if not os.path.isdir(D_PK_SYSTEM):
            raise FileNotFoundError(f"❌ Target path does not exist: {D_PK_SYSTEM}")

        os.chdir(D_PK_SYSTEM)
        os.environ["PATH"] += ";" + os.path.dirname(F_UV_EXE)

        result = subprocess.run([F_UV_EXE, "sync"])
        if result.returncode != 0:
            raise RuntimeError("❌ uv sync failed.")
    except Exception as e:
        print(f"❌ Failed during uv sync: {e}")
        raise

# ──────────────────────────────────────────────
def delete_autorun_key() -> None:
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Command Processor", 0, winreg.KEY_ALL_ACCESS) as key:
            winreg.DeleteValue(key, "AutoRun")
    except FileNotFoundError:
        print("⚠️ No AutoRun key found. Skipping.")
    except Exception as e:
        print(f"❌ Failed to delete AutoRun: {e}")
        raise

# ──────────────────────────────────────────────
def create_shortcuts() -> None:
    """바탕화면과 현재 위치에 바로가기 생성"""
    try:
        try_import_or_install("pywin32", "win32com")
        import win32com.client

        shortcut_name = "PK System Launcher"
        icon_path = os.path.join(os.environ["SystemRoot"], "System32", "shell32.dll") + ",40"

        # 생성 위치 목록: 바탕화면 + 현재 스크립트 위치
        targets = [
            os.path.join(USER_PROFILE, "Desktop", f"{shortcut_name}.lnk"),
            os.path.join(os.path.dirname(F_SHORTCUT_TARGET), f"{shortcut_name}.lnk")
        ]

        shell = win32com.client.Dispatch("WScript.Shell")

        for shortcut_path in targets:
            try:
                shortcut = shell.CreateShortcut(shortcut_path)
                shortcut.TargetPath = "cmd.exe"
                shortcut.Arguments = f'/c "{F_SHORTCUT_TARGET}"'
                shortcut.IconLocation = icon_path
                shortcut.WindowStyle = 1
                shortcut.Save()
                print(f"✅ 바로가기 생성됨: {shortcut_path}")
            except Exception as e:
                print(f"⚠️ 바로가기 생성 실패 ({shortcut_path}): {e}")

        print("\n" + "="*60)
        print("⚠ [작업표시줄 고정]은 수동으로 진행해 주세요:")
        print("1. 바탕화면 바로가기 우클릭 → [작업 표시줄에 고정]")
        print("2. 작업표시줄 왼쪽에 둘 경우 → Win + 1 단축키 가능")
        print("3. 빠른 접근을 위해 첫 번째 위치에 고정 권장")
        print("="*60)

    except Exception as e:
        print(f"❌ Failed to create shortcut(s): {e}")
        raise

# ──────────────────────────────────────────────
def main() -> None:
    print("──────────────────────────────────────────────────────────")
    print(f"[STARTED] {__file__}")
    print("──────────────────────────────────────────────────────────")

    try_import_or_install("requests")

    steps: List[Tuple[str, Callable[[], None]]] = [
        ("Registering pk_alias (1st time)", register_pk_alias),
        ("Installing uv (download/unzip/version)", install_uv),
        ("Installing fzf (download/unzip/version)", install_fzf),
        ("Syncing uv packages", sync_uv_packages),
        ("Setting up PATH with UV, FZF, and venv Python", setup_uv_path),
        ("Deleting previous AutoRun key", delete_autorun_key),
        ("Re-registering pk_alias to AutoRun", register_pk_alias),
        ("Creating desktop and working directory shortcuts", create_shortcuts),
    ]

    try:
        total_steps = len(steps)
        for i, (desc, func) in enumerate(steps, start=1):
            print_step(i, total_steps, desc)
            func()

        print_step(total_steps, total_steps, "🎉 All steps completed successfully", "green")
        
        # UV, FZF, 가상환경 Python PATH 확인
        print("\n UV PATH 확인 중...")
        verify_uv_in_path()
        
        print("\n🔍 FZF PATH 확인 중...")
        verify_fzf_in_path()
        
        print("\n🐍 가상환경 Python PATH 확인 중...")
        verify_venv_python_in_path()

    except Exception:
        print("\n❌ Error occurred during setup process.")
        traceback.print_exc()
        input(" Debug mode - Press Enter to exit.")
    finally:
        for mod, temp in temp_installed_modules.items():
            if temp:
                print(f"⚠️ Removing temporarily installed module '{mod}'...")
                subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", mod])

# ──────────────────────────────────────────────
if __name__ == "__main__":
    main()
