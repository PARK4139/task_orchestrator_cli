
@measure_seconds
and target in " ".join(proc.info.get('cmdline', [])).lower()
break
cpu = proc.cpu_percent()
def enum_handler(hwnd, _):
def get_nx(path: str) -> str:
def get_window_title(window_title_seg: str) -> str | None:
def kill_pid_psutil(pid):
def monitor_process_state(proc, max_sec=2.5, interval=0.5):
def kill_process_v13(window_title_seg: str):
elapsed = time.time() - start
elif elapsed > 2.5:
else:
except Exception as e:
except Exception:
except psutil.TimeoutExpired:
executor.map(kill_pid_psutil, matched_pids)
failed_pids = []
failed_pids.append(pid)
for _ in range(steps):
for proc in psutil.process_iter(['pid', 'name', 'cmdline'])
from concurrent.futures import ThreadPoolExecutor
if LTA:
if elapsed > 5.0:
if failed_pids:
if matched_pids:
if not proc.is_running():
if not window_title:
if proc.info['name'].lower() == 'cmd.exe'
if win32gui.IsWindowVisible(hwnd):
if window_title_seg.lower() in title.lower():
import os
import psutil
import time
matched_pids = {
matches = []
matches.append((hwnd, title))
mem = proc.memory_info().rss / (1024 * 1024)
monitor_process_state(proc)
pass
ensure_printed(f"PK KILL '{window_title}' not found", print_color="red")
ensure_printed(f"[ERROR] {e}", print_color="red")
ensure_printed(f"[SKIP] No window found for seg='{window_title_seg}'", print_color="yellow")
ensure_printed(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
ensure_printed(f"‼️ FORCED TIMEOUT: PID={pid} took {elapsed:.2f}s", print_color="red")
ensure_printed(f"⚠️ PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")
ensure_printed(f"✅ PK KILL PID={pid} window_title={window_title}", print_color="green")
ensure_printed(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")
ensure_printed(f"❗ FAILED PIDs: {sorted(failed_pids)}", print_color="red")
ensure_printed(f"👁️ End monitoring PID={proc.pid}", print_color="blue")
ensure_printed(f"👁️ Start monitoring PID={proc.pid}", print_color="blue")
ensure_printed(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="blue")
proc = psutil.Process(pid)
proc.info['pid']
proc.kill()
proc.terminate()
proc.wait(timeout=1)
return
return matches[0][1] if matches else None
return os.path.splitext(os.path.basename(path))[0]
start = time.time()
steps = int(max_sec / interval)
target = get_nx(window_title).lower()
th = proc.num_threads()
time.sleep(interval)
title = win32gui.GetWindowText(hwnd)
try:
win32gui.EnumWindows(enum_handler, None)
window_title = get_window_title(window_title_seg)
with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
}
