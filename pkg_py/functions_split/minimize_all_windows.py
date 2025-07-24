

def minimize_all_windows():
      # pywin32
    win32gui.EnumWindows(minimize_all_windows_callback, None)
