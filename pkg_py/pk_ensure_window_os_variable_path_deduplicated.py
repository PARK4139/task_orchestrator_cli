import sys
import os
import subprocess
import time

def is_admin():
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """
    Relaunches the current script as admin using ShellExecuteEx.
    """
    if sys.platform == "win32":
        import ctypes
        script = os.path.abspath(sys.argv[0])
        params = " ".join([f'"{arg}"' for arg in sys.argv[1:]])
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, f'"{script}" {params}', None, 1
            )
            sys.exit(0)
        except Exception as e:
            print(f"Failed to elevate: {e}")
            sys.exit(1)

if not is_admin():
    print("THIS PROGRAM MUST BE RUN AS ADMINISTRATOR. RESTARTING WITH ADMIN PRIVILEGES...")
    run_as_admin()
    sys.exit(0)
else:
    print("[DETECTED] ADMINISTRATOR PRIVILEGES")

print(f"FILE: {__file__}")

# Get current PATH environment variable
current_path = os.environ.get("PATH", "")
path_list = current_path.split(";")

# Remove duplicates (preserve order)
cleaned_paths = []
seen = set()
for path in path_list:
    path = path.strip()
    if path and path not in seen:
        seen.add(path)
        cleaned_paths.append(path)

# Add UV path (user defined)
uv_path = r"C:\Users\user\Downloads\pk_system\pkg_exe"
if uv_path not in seen:
    cleaned_paths.append(uv_path)

# Set new PATH
new_path = ";".join(cleaned_paths)
os.system(f'setx PATH "{new_path}"')  # Apply to system environment variable
os.environ["PATH"] = new_path         # Apply to current session immediately

# Output result
print("✅ PATH DEDUPLICATION AND UV PATH ADDITION COMPLETE.")
print("📌 UPDATED PATH:")
print(new_path)
time.sleep(10000)