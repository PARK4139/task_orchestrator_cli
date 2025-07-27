import os
import subprocess
import sys
import traceback
import zipfile
import winreg
from typing import Callable, List, Tuple

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
def register_pk_alias() -> None:
    try:
        user_profile = os.environ["USERPROFILE"]
        pk_alias_path = os.path.join(user_profile, "Downloads", "pk_system", "pkg_windows", "pk_alias.cmd")
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Command Processor") as key:
            winreg.SetValueEx(key, "AutoRun", 0, winreg.REG_SZ, f'"{pk_alias_path}"')
    except Exception as e:
        print(f"❌ Failed to register pk_alias: {e}")
        raise

# ──────────────────────────────────────────────
def install_uv() -> None:
    try_import_or_install("requests")
    import requests

    user_profile = os.environ["USERPROFILE"]
    d_pkg_exe = os.path.join(user_profile, "Downloads", "pk_system", "pkg_exe")
    uv_zip_path = os.path.join(user_profile, "Downloads", "uv.zip")
    uv_exe_path = os.path.join(d_pkg_exe, "uv.exe")
    uv_url = "https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-pc-windows-msvc.zip"

    os.makedirs(d_pkg_exe, exist_ok=True)

    try:
        with requests.get(uv_url, stream=True) as r:
            r.raise_for_status()
            with open(uv_zip_path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    except Exception as e:
        print(f"❌ Failed to download uv: {e}")
        raise

    try:
        with zipfile.ZipFile(uv_zip_path, 'r') as zip_ref:
            zip_ref.extractall(d_pkg_exe)
    except Exception as e:
        print(f"❌ Failed to extract uv zip: {e}")
        raise

    if not os.path.exists(uv_exe_path):
        raise FileNotFoundError(f"❌ uv.exe not found at: {uv_exe_path}")

    try:
        subprocess.run([uv_exe_path, "--version"], check=True)
    except Exception as e:
        print(f"❌ uv verification failed: {e}")
        raise

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_READ) as key:
            try:
                old_path, _ = winreg.QueryValueEx(key, "Path")
            except FileNotFoundError:
                old_path = ""
    except Exception:
        old_path = ""

    if d_pkg_exe not in old_path:
        try:
            new_path = f"{old_path};{d_pkg_exe}" if old_path else d_pkg_exe
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
            print(f"uv path added to PATH: {d_pkg_exe}")
        except Exception as e:
            print(f"❌ Failed to update PATH: {e}")
            raise
    else:
        print("⚠️ uv path already in PATH. Skipping update.")

    try:
        os.remove(uv_zip_path)
    except FileNotFoundError:
        print("⚠️ uv.zip not found for cleanup. Skipping.")
    except Exception as e:
        print(f"⚠️ Failed to remove uv.zip: {e}")

# ──────────────────────────────────────────────
def sync_uv_packages() -> None:
    try:
        user_profile = os.environ["USERPROFILE"]
        d_pk_system = os.path.join(user_profile, "Downloads", "pk_system")
        uv_exe = os.path.join(user_profile, "Downloads", "pk_system", "pkg_exe", "uv.exe")

        if not os.path.isdir(d_pk_system):
            raise FileNotFoundError(f"❌ Target path does not exist: {d_pk_system}")

        os.chdir(d_pk_system)
        os.environ["PATH"] += ";" + os.path.dirname(uv_exe)

        result = subprocess.run([uv_exe, "sync"])
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
    try:
        try_import_or_install("pywin32", "win32com")
        import win32com.client

        user_profile = os.environ["USERPROFILE"]
        script_path = os.path.join(user_profile, "Downloads", "pk_system", "pkg_windows", "ensure_pk_system_ran.cmd")
        shortcut_name = "PK System Launcher"
        icon_path = os.path.join(os.environ["SystemRoot"], "System32", "shell32.dll") + ",40"

        targets = [
            os.path.join(user_profile, "Desktop", f"{shortcut_name}.lnk"),
            os.path.join(os.path.dirname(script_path), f"{shortcut_name}.lnk")
        ]

        shell = win32com.client.Dispatch("WScript.Shell")

        for shortcut_path in targets:
            shortcut = shell.CreateShortcut(shortcut_path)
            shortcut.TargetPath = "cmd.exe"
            shortcut.Arguments = f'/c "{script_path}"'
            shortcut.IconLocation = icon_path
            shortcut.WindowStyle = 1
            shortcut.Save()

        print("\n⚠ [Pin to Taskbar] must be done manually:")
        print("1. Right-click the desktop shortcut → [Pin to Taskbar]")
        print("2. To access quickly: use Win + 1 if pinned to the first position\n")

    except Exception as e:
        print(f"❌ Failed to create shortcut(s): {e}")
        raise

# ──────────────────────────────────────────────
def main() -> None:
    print("──────────────────────────────────────────────────────────")
    print(f"[STARTED] {__file__}.py")
    print("──────────────────────────────────────────────────────────")

    try_import_or_install("requests")

    steps: List[Tuple[str, Callable[[], None]]] = [
        ("Registering pk_alias (1st time)", register_pk_alias),
        ("Installing uv (download/unzip/version/PATH)", install_uv),
        ("Syncing uv packages", sync_uv_packages),
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

    except Exception:
        print("\n❌ Error occurred during setup process.")
        traceback.print_exc()
        input("🛠 Debug mode - Press Enter to exit.")
    finally:
        for mod, temp in temp_installed_modules.items():
            if temp:
                print(f"⚠️ Removing temporarily installed module '{mod}'...")
                subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", mod])

# ──────────────────────────────────────────────
if __name__ == "__main__":
    # TODO : 환경별 검증 필요
    main()
