def get_process_info_by_name(process_name):
    from sources.functions.ensure_process_killed_by_pid import get_process_info_by_process_name
    return get_process_info_by_process_name(process_name)