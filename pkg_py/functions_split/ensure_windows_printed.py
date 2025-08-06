def ensure_windows_printed():
    from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_windows_opened import get_windows_opened
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    window_opened_list = get_windows_opened()
    ensure_console_cleared()
    for window_opened in window_opened_list:
        ensure_printed(str_working=rf'[{func_n}] "{window_opened}" ')
