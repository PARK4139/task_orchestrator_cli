
def enum_handler(hwnd, _):
def pk_ensure_process_deduplicated(window_title_seg: str, exact=True):
except Exception as e:
for hwnd in to_close:
hwnds = []
hwnds.append(hwnd)
if (exact and title == window_title) or (not exact and window_title in title):
if LTA:
if not hwnds:
if not window_title:
if win32gui.IsWindowVisible(hwnd):
import win32con
import win32gui
pk_print(f"[CLOSE] HWND={hwnd} closed for window_title='{win32gui.GetWindowText(hwnd)}'", print_color="green")
pk_print(f"[DEBUG] window_title={window_title} {'%%%FOO%%%' if LTA else ''}")
pk_print(f"[ERROR] {e}", print_color="red")
pk_print(f"[SKIP] No matching windows for '{window_title}'", print_color="red")
pk_print(f"[SURVIVED] HWND={survivor_hwnd} kept alive → '{win32gui.GetWindowText(survivor_hwnd)}'", print_color="yellow")
return
survivor_hwnd = hwnds[0]
title = win32gui.GetWindowText(hwnd)
to_close = hwnds[1:]
try:
win32gui.EnumWindows(enum_handler, None)
win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
window_title = get_window_title(window_title_seg=window_title_seg)
