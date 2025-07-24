def minimize_all_windows():
    import inspect
      # pywin32
    func_n = inspect.currentframe().f_code.co_name
    win32gui.EnumWindows(minimize_all_windows_callback, None)
