def ensure_seconds_measured(func):
    from sources.objects.pk_map_colors import ANSI_COLOR_MAP
    from sources.objects.pk_local_test_activate import LTA
    import logging
    from functools import wraps
    if not LTA:
        return func

    @wraps(func)
    def wrapper(*args, **kwargs):
        import time

        time_s = time.time()

        result = func(*args, **kwargs)

        elapsed_seconds = time.time() - time_s
        elapsed_seconds_str = rf"{ANSI_COLOR_MAP['YELLOW']}elapsed_seconds={elapsed_seconds: .4f}{ANSI_COLOR_MAP['RESET']}"

        log_message = f"{func.__name__}() {elapsed_seconds_str}"

        # Check for NUL characters before logging (for debugging purposes, can be removed later)
        if '\x00' in func.__name__:
            logging.warning(f"NUL character found in function name: {repr(func.__name__)}")
        if '\x00' in elapsed_seconds_str:
            logging.warning(f"NUL character found in elapsed_seconds string: {repr(elapsed_seconds_str)}")
        if '\x00' in log_message:
            logging.warning(f"NUL character found in final log message: {repr(log_message)}")

        logging.debug(log_message)  # Removed repr()

        return result

    return wrapper
