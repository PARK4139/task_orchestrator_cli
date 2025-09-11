def ensure_windows_printed():
    import logging
    from functions.get_windows_opened import get_windows_opened
    for window_opened in get_windows_opened():
        logging.debug(rf'window_opened="{window_opened}"')
