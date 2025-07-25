
# ensure_pk_system_exit_silent()
# ipdb.set_trace()  # 🔍 디버깅 시작 지점
# ✅ 종료 전에 실행
_, pid = win32process.GetWindowThreadProcessId(hwnd)
def enum_handler(hwnd, matched_hwnds):
def pk_kill_process_v16(window_title: str, exact: bool = True):
def try_kill_pid(pid):
else:
except Exception as e:
except ImportError as e:
except psutil.TimeoutExpired:
exe = proc.name().lower()
executor.map(try_kill_pid, matched_pids)
failed_pids = []
failed_pids.append(pid)
for hwnd, title in matched_hwnds:
from concurrent.futures import ThreadPoolExecutor
if exact:
if exe == "cmd.exe":
if failed_pids:
if not matched_hwnds:
if not matched_pids:
if not title:
if title.lower() == window_title.lower():
if win32gui.IsWindowVisible(hwnd):
if window_title.lower() in title.lower():
import logging
import psutil
import win32gui
import win32process
logging.debug(f"[ENUM] hwnd={hwnd}, title='{title}', target='{window_title}'")
logging.error(f"[ERROR] No valid PID found for window title: '{window_title}'")
logging.error(f"[EnumWindows ERROR] {e}")
logging.error(f"[FAILED PIDs] {sorted(failed_pids)}")
logging.error(f"[FAILED] PID={pid} error: {e}")
logging.error(f"[IMPORT ERROR] {e}. Please install pywin32.")
logging.info(f"[HWND->PID] title='{title}' → pid={pid}")
logging.info(f"[INFO] Found {len(matched_hwnds)} matched window(s) for '{window_title}'")
logging.info(f"[KILLED] PID={pid} ('{window_title}') exe='{exe}'")
logging.info(f"[MATCHED:EXACT] '{title}'")
logging.info(f"[MATCHED:PARTIAL] '{title}'")
logging.warning(f"[SKIP] No window matched for: '{window_title}' (exact={exact})")
logging.warning(f"[SKIP] Not killing cmd.exe (PID={pid})")
logging.warning(f"[WARN] Failed to get PID from hwnd={hwnd}: {e}")
matched_hwnds = []
matched_hwnds.append((hwnd, title))
matched_pids = set()
matched_pids.add(pid)
proc = psutil.Process(pid)
proc.kill()
proc.terminate()
proc.wait(timeout=1)
return
title = win32gui.GetWindowText(hwnd).strip()
try:
win32gui.EnumWindows(lambda h, _: enum_handler(h, matched_hwnds), None)
window_title = window_title.strip()
with ThreadPoolExecutor(max_workers=min(4, len(matched_pids))) as executor:
