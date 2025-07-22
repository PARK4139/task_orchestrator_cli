def get_windows_opened_via_win32gui():
    # import win32gui  # pywin32
    import win32gui
    window_titles = []

    def enum_windows_callback(hwnd, lparam):
        if win32gui.IsWindowVisible(hwnd):
            # 창의 제목을 가져와서 리스트에 추가
            window_title = win32gui.GetWindowText(hwnd)
            if window_title:  # 제목이 비어있지 않은 창만 추가
                window_titles.append(window_title)

    win32gui.EnumWindows(enum_windows_callback, None)
    return window_titles
