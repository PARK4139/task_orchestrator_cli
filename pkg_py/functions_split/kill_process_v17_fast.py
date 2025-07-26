
cmdline = " ".join(proc.info['cmdline']).lower()
continue
def kill_process_v17_fast(window_title_seg: str):
except (psutil.NoSuchProcess, psutil.AccessDenied):
for pid in matched_pids:
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
if LTA:
if not matched_pids:
if not window_title:
if proc.info['name'].lower() == "cmd.exe":
if target in cmdline:
import subprocess
matched_pids = set()
matched_pids.add(proc.info['pid'])
ensure_printed(f"PK KILL '{window_title}' not found", print_color="red")
ensure_printed(f"PK KILL PID={pid} window_title={window_title}", print_color="green")
ensure_printed(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
return
stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
target = get_nx(window_title).lower()
try:
window_title = get_window_title(window_title_seg=window_title_seg)
