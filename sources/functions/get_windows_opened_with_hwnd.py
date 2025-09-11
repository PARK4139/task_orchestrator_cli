def get_windows_opened_with_hwnd():
    # return get_windows_opened_with_hwnd_via_psutil()
    # return get_windows_opened_with_hwnd_via_pygetwindow()
    return get_windows_opened_with_hwnd_via_win32gui()


def get_windows_opened_with_hwnd_via_win32gui():
    # pywin32
    import win32gui
    windows = []

    def enum_windows_callback(hwnd, lparam):
        if win32gui.IsWindowVisible(hwnd):
            window_title = win32gui.GetWindowText(hwnd)
            if window_title:
                windows.append((window_title, hwnd))

    win32gui.EnumWindows(enum_windows_callback, None)
    return windows
