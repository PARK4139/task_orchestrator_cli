# @ensure_seconds_measured
def ensure_signiture_found_in_souts_for_milliseconds_limited(cmd: str, signiture: str, milliseconds_limited, encoding='utf-8'):
    import logging
    import time
    import traceback

    from functions import ensure_slept, ensure_command_executed
    from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose

    try:
        time_s = time.time()
        is_found = False
        while True:
            if is_found:
                break
            sout, _ = ensure_command_executed(cmd=cmd, encoding=encoding)
            lines = sout
            for line in lines:
                if signiture in line:
                    is_found = True
                    continue
            ensure_slept(milliseconds=80)
            if (time.time() - time_s) * 1000 > milliseconds_limited:
                logging.warning(f'Timed out after {milliseconds_limited} milliseconds')
                return False
        if is_found:
            return True

    except:
        ensure_debug_loged_verbose(traceback)
    finally:
        pass
