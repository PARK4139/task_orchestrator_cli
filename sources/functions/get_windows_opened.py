# @ensure_seconds_measured
def get_windows_opened():
    import win32gui
    windows = []

    def enum_windows_callback(hwnd, lparam):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if window_title:
                windows.append((window_title))
    win32gui.EnumWindows(enum_windows_callback, None)
    return windows
