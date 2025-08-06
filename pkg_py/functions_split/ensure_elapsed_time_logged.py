def ensure_elapsed_time_logged(start_time, log_file_path=None):
    from pkg_py.functions_split.print_and_save_log_to_file import print_and_save_log_to_file
    from pkg_py.system_object.color_map import PK_ANSI_COLOR_MAP
    import time
    from pkg_py.system_object.map_massages import PkMessages2025
    import inspect
    from pkg_py.system_object.directories import D_DESKTOP

    if log_file_path is None:
        func_n = inspect.currentframe().f_code.co_name
        log_file_default = f"{D_DESKTOP}/result_of_{func_n}.txt"
        log_file_path = log_file_default
    duration = time.time() - start_time
    elapsed_time = rf"{duration:.2f}"
    msg = f"{PK_ANSI_COLOR_MAP['YELLOW']}ENDED AT : {duration:.2f} {PkMessages2025.SECONDS} {PK_ANSI_COLOR_MAP['RESET']}"
    print_and_save_log_to_file(msg, log_file_path)

    # pk_option
    # print_marker_and_stop()

    # pk_option
    # ensure_pk_system_exit_silent()
    return elapsed_time
