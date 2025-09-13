from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_signiture_found_in_lines(signiture: str, lines, milliseconds_limited=5):
    import time
    import traceback

    import logging

    from functions import ensure_slept
    from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

    try:
        time_s = time.time()
        is_found = False
        while True:
            if is_found:
                break
            for line in lines:
                if signiture in line:
                    is_found = True
                    continue
            ensure_slept(milliseconds=80)
            if time.time() - time_s > milliseconds_limited:
                logging.warning(f'Timed out after {milliseconds_limited} milliseconds')
                return False
        if is_found:
            return True

    except:
        ensure_debug_loged_verbose(traceback)
    finally:
        pass
