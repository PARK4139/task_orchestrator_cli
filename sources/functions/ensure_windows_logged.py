from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_windows_logged():
    import logging
    import logging
    from sources.functions.ensure_console_cleared import ensure_console_cleared
    from sources.functions.get_windows_opened_with_hwnd import get_windows_opened_with_hwnd
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    window_opened_list = get_windows_opened_with_hwnd()
    ensure_console_cleared()
    for window_opened in window_opened_list:
        logging.debug(rf'[{func_n}] "{window_opened}" ')
