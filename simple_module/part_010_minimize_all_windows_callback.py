

def minimize_all_windows_callback(hwnd, lparam):
    import inspect
    # import win32gui  # pywin32
    import win32con  # pywin32
    func_n = inspect.currentframe().f_code.co_name

    # 창이 보이는 상태일 때만 최소화
    if win32gui.IsWindowVisible(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)  # 창을 최소화
        print(f"창 {win32gui.GetWindowText(hwnd)}를 최소화했습니다.")
