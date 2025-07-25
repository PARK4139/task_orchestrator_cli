
cmdline = " ".join(proc.info['cmdline']).lower()
continue
def kill_pid_psutil(pid):
def pk_kill_process_v10(window_title_seg: str):
elapsed = time.time() - start
else:
except (psutil.NoSuchProcess, psutil.AccessDenied):
except Exception as e:
except psutil.TimeoutExpired:
executor.map(kill_pid_psutil, matched_pids)
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
from concurrent.futures import ThreadPoolExecutor
if LTA:
if elapsed > 2.0:
if matched_pids:
if not window_title:
if proc.info['name'].lower() == "cmd.exe":
if target in cmdline:
import psutil
import time
matched_pids = set()
matched_pids.add(proc.info['pid'])
pass  # 최종 타임아웃 2초 경과 후 포기
pk_print(f"PK KILL '{window_title}' not found", print_color="red")
pk_print(f"PK KILL ERROR PID={pid} : {e}", print_color="red")
pk_print(f"PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="yellow")
pk_print(f"PK KILL PID={pid} window_title=...", print_color="green")
pk_print(f"[ERROR] {e}", print_color="red")
pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
proc = psutil.Process(pid)
proc.kill()
proc.terminate()
proc.wait(timeout=1)
return
start = time.time()
target = get_nx(window_title).lower()
try:
window_title = get_window_title(window_title_seg=window_title_seg)
with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
