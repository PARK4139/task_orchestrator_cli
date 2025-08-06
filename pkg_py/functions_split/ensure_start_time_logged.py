def ensure_start_time_logged(log_file_path=None):
    from pkg_py.functions_split.print_and_save_log_to_file import print_and_save_log_to_file
    import inspect
    import time
    from pkg_py.system_object.directories import D_DESKTOP
    from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP

    if log_file_path is None:
        func_n = inspect.currentframe().f_code.co_name
        log_file_default = f"{D_DESKTOP}/result_of_{func_n}.txt"
        log_file_path = log_file_default
    start_time = time.time()
    msg = f"{PK_ANSI_COLOR_MAP['YELLOW']}STARTED AT : {time.strftime('%Y-%m-%d %H:%M:%S')} {PK_ANSI_COLOR_MAP['RESET']}"
    print_and_save_log_to_file(msg, log_file_path)
    return start_time
