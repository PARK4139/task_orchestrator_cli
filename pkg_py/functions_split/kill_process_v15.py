
# 출력용 정렬: 유사한 것 먼저
@measure_seconds
and target in " ".join(proc.info.get('cmdline', [])).lower()
best_match_title = matches[0][1]
break
cpu = proc.cpu_percent()
def enum_handler(hwnd, _):
def get_nx(path: str) -> str:
def get_window_matches(window_title_seg: str):
def kill_pid_psutil(pid):
def monitor_process_state(proc, max_sec=2.5, interval=0.5):
def kill_process_v15(window_title_seg: str):
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
for hwnd, title, is_similar in matches:
for proc in psutil.process_iter(['pid', 'name', 'cmdline'])
from concurrent.futures import ThreadPoolExecutor
if LTA:
if elapsed > 5.0:
if failed_pids:
if matched_pids:
if not matches:
if not proc.is_running():
if proc.info['name'].lower() == 'cmd.exe'
if title:
if win32gui.IsWindowVisible(hwnd):
import os
import psutil
import time
matched_pids = {
matches = []
matches = get_window_matches(window_title_seg)
matches.append((hwnd, title, similarity))
matches.sort(key=lambda x: x[2], reverse=True)
mem = proc.memory_info().rss / (1024 * 1024)
monitor_process_state(proc)
pass
ensure_printed(f"PK KILL '{best_match_title}' not found", print_color="red")
ensure_printed(f"[ERROR] {e}", print_color="red")
ensure_printed(f"[INFO] Found {len(matches)} window(s). Similarity check:", print_color="cyan")
ensure_printed(f"[SKIP] No window found for seg='{window_title_seg}'", print_color="yellow")
ensure_printed(f"{sim_mark} [{hwnd}] {title}", print_color="cyan")
ensure_printed(f"‼️ FORCED TIMEOUT: PID={pid} took {elapsed:.2f}s", print_color="red")
ensure_printed(f"⚠️ PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")
ensure_printed(f"✅ PK KILL PID={pid} window_title={best_match_title}", print_color="green")
ensure_printed(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")
ensure_printed(f"❗ FAILED PIDs: {sorted(failed_pids)}", print_color="red")
ensure_printed(f"👁️ End monitoring PID={proc.pid}", print_color="blue")
ensure_printed(f"👁️ Start monitoring PID={proc.pid}", print_color="blue")
ensure_printed(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="blue")
ensure_printed(f"🪟 Using best match title: {best_match_title} {'%%%FOO%%%' if LTA else ''}", print_color="cyan")
proc = psutil.Process(pid)
proc.info['pid']
proc.kill()
proc.terminate()
proc.wait(timeout=1)
return
return matches
return os.path.splitext(os.path.basename(path))[0]
sim_mark = "✅" if is_similar else "  "
similarity = window_title_seg.lower() in title.lower()
start = time.time()
steps = int(max_sec / interval)
target = get_nx(best_match_title).lower()
th = proc.num_threads()
time.sleep(interval)
title = win32gui.GetWindowText(hwnd)
try:
win32gui.EnumWindows(enum_handler, None)
with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
}
