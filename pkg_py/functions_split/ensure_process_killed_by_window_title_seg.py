import time
from concurrent.futures import ThreadPoolExecutor

import psutil
import win32gui
import win32process

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.system_object.local_test_activate import LTA


def get_window_matches(window_title_seg: str):
    matches = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                is_similar = window_title_seg.lower() in title.lower()
                similarity = is_similar  # 간단한 유사도 판단
                matches.append((hwnd, title, similarity))

    win32gui.EnumWindows(enum_handler, None)
    matches.sort(key=lambda x: x[2], reverse=True)
    return matches


def kill_pid_psutil(pid):
    try:
        proc = psutil.Process(pid)
        proc.kill()
    except Exception as e:
        ensure_printed(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")
        return False
    return True


def monitor_process_state(proc, max_sec=2.5, interval=0.5):
    start = time.time()
    steps = int(max_sec / interval)
    ensure_printed(f"👁️ Start monitoring PID={proc.pid}", print_color="blue")

    for _ in range(steps):
        try:
            if not proc.is_running():
                break
            cpu = proc.cpu_percent()
            mem = proc.memory_info().rss / (1024 * 1024)
            th = proc.num_threads()
            ensure_printed(f"🔍 PID={proc.pid} CPU={cpu:.1f}% MEM={mem:.1f}MB TH={th}", print_color="blue")
            time.sleep(interval)
        except Exception:
            break

    elapsed = time.time() - start
    ensure_printed(f"👁️ End monitoring PID={proc.pid}", print_color="blue")

    if proc.is_running():
        ensure_printed(f"‼️ FORCED TIMEOUT: PID={proc.pid} took {elapsed:.2f}s", print_color="red")
    elif elapsed > max_sec:
        ensure_printed(f"⚠️ PK KILL PID={proc.pid} TIMEOUT_ELAPSED={elapsed:.2f}s", print_color="red")


@ensure_seconds_measured
def ensure_process_killed_by_window_title_seg(window_title_seg: str):
    matches = get_window_matches(window_title_seg)
    if not matches:
        ensure_printed(f"[SKIP] No window found for seg='{window_title_seg}'", print_color="yellow")
        return

    ensure_printed(f"[INFO] Found {len(matches)} window(s). Similarity check:", print_color="cyan")
    for hwnd, title, is_similar in matches:
        sim_mark = "✅" if is_similar else "  "
        ensure_printed(f"{sim_mark} [{hwnd}] {title}", print_color="cyan")

    best_match_hwnd, best_match_title, _ = matches[0]
    _, pid = win32process.GetWindowThreadProcessId(best_match_hwnd)

    if not pid:
        ensure_printed(f"PK KILL '{best_match_title}' not found (No PIDs)", print_color="red")
        return

    ensure_printed(f"🪟 Using best match title: {best_match_title} {'%%%FOO%%%' if LTA else ''}", print_color="cyan")

    matched_pids = {pid}
    failed_pids = []

    with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
        results = list(executor.map(kill_pid_psutil, matched_pids))
        for pid, success in zip(matched_pids, results):
            if not success:
                failed_pids.append(pid)
            else:
                try:
                    proc = psutil.Process(pid)
                    proc.terminate()
                    proc.wait(timeout=1)
                    monitor_process_state(proc)
                    ensure_printed(f"✅ PK KILL PID={pid} title_match={best_match_title}", print_color="green")
                except psutil.TimeoutExpired:
                    ensure_printed(f"⚠️ PK KILL PID={pid} TIMEOUT", print_color="red")
                except Exception as e:
                    ensure_printed(f"❌ PK KILL ERROR PID={pid} : {e}", print_color="red")

    if failed_pids:
        ensure_printed(f"❗ FAILED PIDs: {sorted(failed_pids)}", print_color="red")
