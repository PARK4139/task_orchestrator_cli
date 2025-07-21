

def minimize_all_windows():
    # import win32gui  # pywin32
    win32gui.EnumWindows(minimize_all_windows_callback, None)
