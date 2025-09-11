def is_window_opened(window_title_seg):
    import logging
    from sources.functions.get_windows_opened_with_hwnd import get_windows_opened_with_hwnd
    windows = get_windows_opened_with_hwnd()
    for windows_title_opened in windows:
        if window_title_seg in windows_title_opened:
            logging.debug(f'''"{window_title_seg}" window is opened''')
            return True
    logging.debug(f'''"{window_title_seg}" window is not opened''')
    return False
