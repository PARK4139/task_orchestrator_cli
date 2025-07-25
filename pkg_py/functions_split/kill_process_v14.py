
@pk_measure_seconds
and target in " ".join(proc.info.get('cmdline', [])).lower()
cpu = proc.cpu_percent(interval=duration)
def enum_handler(hwnd, _):
def get_nx(path: str) -> str:
def get_window_title(window_title_seg: str) -> str | None:
def kill_pid_psutil(pid):
def monitor_process_state(proc, duration=1.0):
def pk_kill_process_v14(window_title_seg: str):
elapsed = time.time() - start
else:
except Exception as e:
except Exception:
except psutil.TimeoutExpired:
executor.map(kill_pid_psutil, matched_pids)
failed_pids = []
failed_pids.append(pid)
for proc in psutil.process_iter(['pid', 'name', 'cmdline'])
from concurrent.futures import ThreadPoolExecutor
if LTA:
if elapsed > 2.5:
if elapsed > 5.0:
if failed_pids:
if matched_pids:
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
monitor_process_state(proc, duration=0.5)
pass
pk_print(f"PK KILL '{window_title}' not found", print_color="red")
pk_print(f"[ERROR] {e}", print_color="red")
pk_print(f"[SKIP] No window found for seg='{window_title_seg}'", print_color="yellow")
pk_print(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
pk_print(f"‼️ FORCED TIMEOUT: PID={pid} took {elapsed:.2f}s", print_color="red")
pk_print(f"⚠️ PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")
pk_print(f"✅ PK KILL PID={pid} window_title={window_title}", print_color="green")
pk_print(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")
pk_print(f"❗ FAILED PIDs: {sorted(failed_pids)}", print_color="red")
pk_print(f"👁️ Monitor PID={proc.pid}", print_color="blue")
pk_print(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="blue")
proc = psutil.Process(pid)
proc.info['pid']
proc.kill()
proc.terminate()
proc.wait(timeout=1)
return
return  # 💥 병목 방지용 조기 종료
return matches[0][1] if matches else None
return os.path.splitext(os.path.basename(path))[0]
start = time.time()
target = get_nx(window_title).lower()
th = proc.num_threads()
title = win32gui.GetWindowText(hwnd)
try:
win32gui.EnumWindows(enum_handler, None)
window_title = get_window_title(window_title_seg)
with ThreadPoolExecutor(max_workers=4) as executor:
}
