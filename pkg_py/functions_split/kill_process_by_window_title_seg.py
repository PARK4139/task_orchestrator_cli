
# 유사도 높은 첫 번째 타이틀로 선택
# 해당 타이틀을 가진 윈도우들의 PID 직접 수집
@pk_measure_seconds
_, pid = win32process.GetWindowThreadProcessId(hwnd)
best_match_hwnd, best_match_title, _ = matches[0]
break
continue
cpu = proc.cpu_percent()
def enum_handler(hwnd, _):
def get_window_matches(window_title_seg: str):
def kill_pid_psutil(pid):
def monitor_process_state(proc, max_sec=2.5, interval=0.5):
def pk_kill_process_by_window_title_seg(window_title_seg: str):
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
from concurrent.futures import ThreadPoolExecutor
if LTA:
if elapsed > 5.0:
if failed_pids:
if is_similar:
if matched_pids:
if not matches:
if not proc.is_running():
if title:
if win32gui.IsWindowVisible(hwnd):
import psutil
import time
matched_pids = set()
matched_pids.add(pid)
matches = []
matches = get_window_matches(window_title_seg)
matches.append((hwnd, title, similarity))
matches.sort(key=lambda x: x[2], reverse=True)
mem = proc.memory_info().rss / (1024 * 1024)
monitor_process_state(proc)
pass
pk_print(f"PK KILL '{best_match_title}' not found (No PIDs)", print_color="red")
pk_print(f"[ERROR] {e}", print_color="red")
pk_print(f"[INFO] Found {len(matches)} window(s). Similarity check:", print_color="cyan")
pk_print(f"[SKIP] No window found for seg='{window_title_seg}'", print_color="yellow")
pk_print(f"{sim_mark} [{hwnd}] {title}", print_color="cyan")
pk_print(f"‼️ FORCED TIMEOUT: PID={pid} took {elapsed:.2f}s", print_color="red")
pk_print(f"⚠️ PK KILL PID={pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")
pk_print(f"✅ PK KILL PID={pid} title_match={best_match_title}", print_color="green")
pk_print(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")
pk_print(f"❗ FAILED PIDs: {sorted(failed_pids)}", print_color="red")
pk_print(f"👁️ End monitoring PID={proc.pid}", print_color="blue")
pk_print(f"👁️ Start monitoring PID={proc.pid}", print_color="blue")
pk_print(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="blue")
pk_print(f"🪟 Using best match title: {best_match_title} {'%%%FOO%%%' if LTA else ''}", print_color="cyan")
proc = psutil.Process(pid)
proc.kill()
proc.terminate()
proc.wait(timeout=1)
return
return matches
sim_mark = "✅" if is_similar else "  "
similarity = window_title_seg.lower() in title.lower()
start = time.time()
steps = int(max_sec / interval)
th = proc.num_threads()
time.sleep(interval)
title = win32gui.GetWindowText(hwnd)
try:
win32gui.EnumWindows(enum_handler, None)
with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
