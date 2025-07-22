def pk_ensure_keyboard_mouse_macro(macro_routine):
    import inspect
    import logging
    import os
    import time
    from pkg_py.functions_split.ensure_pycharm_module_optimize import ensure_pycharm_module_optimize
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
    from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
    from pkg_py.pk_system_object.color_map import PK_ANSI_COLOR_MAP
    from pkg_py.pk_system_object.directories import D_DESKTOP
    from pkg_py.refactor.pk_ensure_keyboard_mouse_macro import PkMacroRoutines
    from pkg_py.functions_split.ensure_elapsed_time_logged import ensure_elapsed_time_logged
    from pkg_py.functions_split.ensure_start_time_logged import ensure_start_time_logged
    from pkg_py.functions_split.pk_print import pk_print
    func_n = inspect.currentframe().f_code.co_name
    db = PkSqlite3DB()

    # log start
    start_time = ensure_start_time_logged()
    GREEN = PK_ANSI_COLOR_MAP['GREEN']
    RESET = PK_ANSI_COLOR_MAP['RESET']
    logging.info(f"LOCAL LEPO : {GREEN}{os.getcwd()}{RESET}")
    logging.info(f"STARTED AT : {GREEN}{time.strftime('%Y-%m-%d %H:%M:%S')}{RESET}")

    # do macro routine
    if macro_routine == PkMacroRoutines.ENSURE_PYCHARM_CODE_OPTIMIZED:
        ensure_pycharm_module_optimize()
    else:
        pk_print(f'''{PkMessages2025.NOT_PREPARED_YET}{'%%%FOO%%%' if LTA else ''}''', print_color='green', mode_verbose=0)

    logging.info(f"[{PkMessages2025.DONE}] {macro_routine}")

    # end log
    duration = time.time() - start_time
    msg = f"{GREEN}ALL PROCESS COMPLETED SUCCESSFULLY. TOTAL EXECUTION TIME: {duration:.2f} SECONDS {RESET}"
    log_file_path = f"{D_DESKTOP}/result_of_{func_n}_of_{macro_routine}.txt"
    elapsed_time = ensure_elapsed_time_logged(start_time, log_file_path=log_file_path)
    # ensure_os_shutdown(seconds=10) # pk_option
