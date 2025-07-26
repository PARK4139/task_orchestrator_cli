
"""
closed_hwnds = []
closed_hwnds.append((hwnd, title))
def enum_handler(hwnd, _):
def kill_process_v16_1(window_title: str, exact: bool = True):
else:
except Exception as e:
if exact:
if not closed_hwnds:
if not title:
if title.lower() == window_title.lower():
if win32gui.IsWindowVisible(hwnd):
if window_title.lower() in title.lower():
import logging
import win32con
import win32gui
logging.error(f"[EnumWindows ERROR] {e}")
logging.info(f"[CLOSE:EXACT] '{title}' (hwnd={hwnd})")
logging.info(f"[CLOSE:PARTIAL] '{title}' (hwnd={hwnd})")
logging.info(f"[INFO] Closed {len(closed_hwnds)} window(s) for '{window_title}'")
logging.warning(f"[SKIP] No window matched for: '{window_title}' (exact={exact})")
return
title = win32gui.GetWindowText(hwnd).strip()
try:
win32gui.EnumWindows(lambda h, _: enum_handler(h, closed_hwnds), None)
win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
window_title = window_title.strip()
창 제목이 정확히 일치(또는 부분 일치)하는 모든 창에 WM_CLOSE 메시지를 보내 창만 닫는다.
