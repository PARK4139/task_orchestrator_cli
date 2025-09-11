import os
import platform
import shutil
import subprocess
import winreg
from pathlib import Path

def print_step(message):
    """Prints a formatted step message."""
    print(f"\n--- {message} ---")

def remove_registry_key(hive, key_path, value_name):
    """Removes a specific value from a registry key."""
    try:
        with winreg.OpenKey(hive, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
            winreg.DeleteValue(key, value_name)
            print(f"Successfully removed registry value: {value_name}")
    except FileNotFoundError:
        print(f"Registry value not found (already removed): {value_name}")
    except Exception as e:
        print(f"Error removing registry value {value_name}: {e}")

def clean_user_path(paths_to_remove):
    """Removes specified paths from the user's PATH environment variable."""
    try:
        key_path = "Environment"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
            current_path, value_type = winreg.QueryValueEx(key, "PATH")
            original_paths = current_path.split(';')
            
            # Normalize paths for comparison
            normalized_paths_to_remove = {str(Path(p).resolve()).lower() for p in paths_to_remove if p}

            new_paths = [
                p for p in original_paths 
                if p and str(Path(p).resolve()).lower() not in normalized_paths_to_remove
            ]

            if len(new_paths) < len(original_paths):
                new_path_str = ';'.join(new_paths)
                winreg.SetValueEx(key, "PATH", 0, value_type, new_path_str)
                print("Successfully cleaned user PATH environment variable.")
                # Broadcast the change
                import ctypes
                HWND_BROADCAST = 0xFFFF
                WM_SETTINGCHANGE = 0x001A
                ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment")
                print("Environment variable changes broadcasted to the system.")
            else:
                print("No project-specific paths found in user PATH. No changes made.")

    except FileNotFoundError:
        print("PATH environment variable not found in registry.")
    except Exception as e:
        print(f"Error cleaning user PATH: {e}")

def delete_file(file_path):
    """Deletes a file if it exists."""
    try:
        if file_path.exists():
            file_path.unlink()
            print(f"Successfully deleted file: {file_path}")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")

def main():
    """Main function to run the uninstallation process."""
    if platform.system().lower() != "windows":
        print("This uninstaller is for Windows only.")
        return

    print("Starting task_orchestrator_cli uninstallation (Python script part)...")

    # Define paths based on project structure
    d_project_root = Path(__file__).parent.parent.parent
    d_system_resources = d_project_root / "system_resources"
    d_venv_windows = d_project_root / ".venv_windows"
    f_alias_bat = d_system_resources / "ensure_pk_alias_enabled.bat"
    desktop = Path.home() / "Desktop"
    
    # --- 1. Remove Registry Entries ---
    print_step("Removing Registry Entries")
    remove_registry_key(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Command Processor", "AutoRun")
    remove_registry_key(winreg.HKEY_CURRENT_USER, "Environment", "PYTHONPATH")
    
    # Clean PATH
    paths_to_remove = [
        str(d_system_resources),
        str(d_venv_windows / "Scripts"),
        str(d_project_root / "resources"),
    ]
    clean_user_path(paths_to_remove)

    # --- 2. Delete Files and Shortcuts ---
    print_step("Deleting Files and Shortcuts")
    delete_file(f_alias_bat)
    delete_file(desktop / "task_orchestrator_cli_launcher.lnk")
    delete_file(d_system_resources / "task_orchestrator_cli_launcher.lnk")

    print("\nPython script part of the uninstallation complete.")
    print("The batch file will now remove the remaining files and virtual environment.")

if __name__ == "__main__":
    main()