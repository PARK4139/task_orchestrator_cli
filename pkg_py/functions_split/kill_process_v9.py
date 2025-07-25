
cmdline = " ".join(proc.info['cmdline']).lower()
continue
def kill_pid(pid):
def pk_kill_process_v9(window_title_seg: str):
else:
except (psutil.NoSuchProcess, psutil.AccessDenied):
except Exception as e:
executor.map(kill_pid, matched_pids)
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
from concurrent.futures import ThreadPoolExecutor
if LTA:
if matched_pids:
if not window_title:
if proc.info['name'].lower() == "cmd.exe":
if target in cmdline:
import psutil
import subprocess
matched_pids = set()
matched_pids.add(proc.info['pid'])
pk_print(f"PK KILL '{window_title}' not found", print_color="red")
pk_print(f"PK KILL PID={pid} window_title={window_title}", print_color="green")
pk_print(f"[ERROR] {e}", print_color="red")
pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
return
stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
target = get_nx(window_title).lower()
try:
window_title = get_window_title(window_title_seg=window_title_seg)
with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
