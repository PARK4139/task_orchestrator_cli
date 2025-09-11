from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_process_names_by_window_title(window_title):
    import logging

    from sources.functions.get_pids_by_window_title import get_pids_by_window_title
    from sources.functions.get_process_name_by_pid import get_process_name_by_pid
    process_names = []
    pids = get_pids_by_window_title(window_title)
    logging.debug(rf"pids={pids}")
    for pid in pids:
        process_name = get_process_name_by_pid(pid)
        logging.debug(rf"pid {pid} of process_name={process_name}")
        process_names.append(process_name)

    return process_names
