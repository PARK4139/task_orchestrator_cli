def ensure_pycharm_window_to_front():
    import logging

    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.functions.get_pids import get_pids
    try:
        logging.debug("Attempting to get PIDs for pycharm64.exe")
        pids = get_pids(process_img_n="pycharm64.exe")
        if not pids:
            return
        for pid in pids:
            logging.debug(f"Attempting to bring PID {pid} to front.")
            ensure_window_to_front(pid=pid)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        import traceback
        ensure_debug_loged_verbose(traceback)
