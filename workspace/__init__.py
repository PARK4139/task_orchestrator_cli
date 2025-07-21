import inspect
import logging
import os
import time

from pkg_py.pk_paste_as_auto import pk_copy
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
from pkg_py.pk_system_layer_color_map import PK_ANSI_COLOR_MAP
from pkg_py.pk_system_layer_directories import D_DESKTOP
from pkg_py.refactor.pk_ensure_keyboard_mouse_macro import PkMacroRoutines
from pkg_py.simple_module.ensure_elapsed_time_logged import ensure_elapsed_time_logged
from pkg_py.simple_module.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
from pkg_py.simple_module.ensure_start_time_logged import ensure_start_time_logged
from pkg_py.simple_module.get_file_id import get_file_id
from pkg_py.simple_module.get_value_by_file_id import get_value_by_file_id
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_132_get_str_from_f import get_str_from_f
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.pk_ensure_loop_delayed_at_loop_foot import pk_ensure_loop_delayed_at_loop_foot
from pkg_py.simple_module.pk_type import pk_type


def open_pycharm_parrete():
    pk_press("shift")
    pk_sleep(100)
    pk_press("shift")
    pk_sleep(500)


def press_ctrl_alt_l_nth():
    n = 3
    for _ in range(n):
        pk_sleep(100)
        pk_press("ctrl+alt+shift+l")
        pk_sleep(100)
        pk_press("enter")
        pk_sleep(100)
    pk_sleep(100)


def paste_and_enter():
    pk_press("ctrl+v")
    pk_sleep(200)
    pk_press("enter")
    # pk_sleep(500)


def move_cursor_to_top_of_pycarm_code():
    pk_press("ctrl", "home")
    pk_press("ctrl", "pgdn")
    pk_press("ctrl", "end")
    pk_press("ctrl", "home")


def extend_pycharm_code():
    pk_press("ctrl", "shift", "+")


def close_pycharm_tab():
    pk_press("ctrl", "f4")
    pk_sleep(100)


def move_pycharm_cursor_to_file(__file__):
    filename_to_dst = os.path.basename(__file__)
    pk_copy(filename_to_dst)
    pk_sleep(100)
    open_pycharm_parrete()
    pk_sleep(500)
    paste_and_enter()
    logging.info(f"[{PkMessages2025.MOVED}] {filename_to_dst}")


def move_cursor_to_text_location(text_to_move_cursor):
    pk_press("ctrl", "f")
    pk_type(text_to_move_cursor)
    pk_sleep(100)
    pk_press("enter")


def ensure_pycharm_module_optimize():
    """Optimize pycharm module via keyboard-mouse macro"""
    import os
    import shutil
    import logging
    import sys
    import inspect
    import pyautogui
    from datetime import datetime
    from os import environ

    from pkg_py.pk_paste_as_auto import pk_copy
    from pkg_py.pk_system_layer_100_Local_test_activate import LTA
    from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
    from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
    from pkg_py.pk_system_layer_directories import D_PKG_ARCHIVED
    from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
    from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
    from pkg_py.simple_module.part_330_get_d_working import get_d_working
    from pkg_py.simple_module.part_832_get_values_from_historical_file_routine import get_values_from_historical_file_routine

    # d_working = rf"{environ['USERPROFILE']}\Downloads\pk_system\pkg_py\workspace"
    d_working = rf"{environ['USERPROFILE']}\Downloads\pk_system\pkg_py\simple_module"
    func_n = inspect.currentframe().f_code.co_name
    db = PkSqlite3DB()
    PROCESS_NAME = PkMacroRoutines.ENSURE_PYCHARM_CODE_OPTIMIZED
    EXCLUDED_PREFIXES = ["a2z_", "prefix_to_exclude_"]
    ALLOWED_EXTENSIONS = [".py"]
    key_name = "DIRECTORY_TO_DO_MACRO_ROUTINE"
    if LTA:
        DIRECTORY_TO_DO_MACRO_ROUTINE = os.path.normpath(
            d_working
        )
    else:
        DIRECTORY_TO_DO_MACRO_ROUTINE = os.path.normpath(
            get_values_from_historical_file_routine(
                file_id=db.get_id(key_name, func_n),
                key_hint=f'{key_name}=',
                values_default=[get_d_working()]
            )
        )

    if not does_pnx_exist(DIRECTORY_TO_DO_MACRO_ROUTINE):
        ensure_pk_system_exit_silent()

    timestamp = datetime.now().strftime("%Y_%m%d_%H%M_%S")
    wd_name = os.path.basename(DIRECTORY_TO_DO_MACRO_ROUTINE.rstrip("/\\"))
    archive_basename = os.path.join(
        D_PKG_ARCHIVED,
        f"{wd_name}_archived_before_work_via_{func_n}_{timestamp}"
    )
    archive_output = f"{archive_basename}.tar.bz2"

    os.makedirs(D_PKG_ARCHIVED, exist_ok=True)
    shutil.make_archive(archive_basename, 'bztar', root_dir=DIRECTORY_TO_DO_MACRO_ROUTINE)
    logging.info(f"[{PkMessages2025.COMPRESSED}] {archive_output}")

    logging.info(f"[{PkMessages2025.STARTED}] {PROCESS_NAME}")

    file_names = os.listdir(DIRECTORY_TO_DO_MACRO_ROUTINE)
    filtered_files = [
        f for f in file_names
        if os.path.isfile(os.path.join(DIRECTORY_TO_DO_MACRO_ROUTINE, f))
           and not any(f.startswith(prefix) for prefix in EXCLUDED_PREFIXES)
           and os.path.splitext(f)[1].lower() in ALLOWED_EXTENSIONS
    ]

    loop_cnt = 1
    file_cnt = 1
    file_first_cnt = file_cnt
    total_file_cnt = len(filtered_files)

    key_name = "file_skip_limit"
    file_skip_limit = db.get_values(db_id=db.get_id(key_name, func_n))
    if file_skip_limit is None:
        file_skip_limit = get_values_from_historical_file_routine(
            file_id=get_file_id(key_name, func_n),
            key_hint=f'{key_name}=',
            values_default=[str(file_first_cnt), str(total_file_cnt)],
            editable=True,
        )
    file_skip_limit = int(file_skip_limit)

    mouse_x, mouse_y = pyautogui.position()
    file_name_last = None

    try:
        for file_name in filtered_files:
            file_abspath = os.path.join(DIRECTORY_TO_DO_MACRO_ROUTINE, file_name)
            new_x, new_y = pyautogui.position()
            if (new_x, new_y) != (mouse_x, mouse_y):
                logging.info(f"[{PkMessages2025.DETECTED}] {PkMessages2025.MOUSE_MOVEMENT}")
                sys.exit(0)
            if file_cnt < file_skip_limit:
                logging.info(f"[{PkMessages2025.SKIPPED}] {file_cnt}/{total_file_cnt}")
            elif get_str_from_f(file_abspath).strip().startswith("def"):
                logging.info(f"[{PkMessages2025.SKIPPED}] {file_cnt}/{total_file_cnt} for detected contents started as 'def' ")
            else:
                logging.info(f"[{PkMessages2025.STARTED}] {file_cnt}/{total_file_cnt}")
                logging.info(f"[{PkMessages2025.STARTED}] {file_name}")
                file_name_last = file_name

                file_base = os.path.splitext(file_name)[0]
                pk_copy(file_base)
                open_pycharm_parrete()
                paste_and_enter()
                move_cursor_to_top_of_pycarm_code()
                extend_pycharm_code()
                press_ctrl_alt_l_nth()
                close_pycharm_tab()

                pk_ensure_loop_delayed_at_loop_foot(loop_cnt, mode_level=2, miliseconds_limit=50)
                loop_cnt += 1

            file_cnt += 1  # ✅ 단일 위치에서 증가

    except Exception as e:
        logging.info(f"[ERROR] 예외 발생: {e}")
    finally:
        if LTA:
            ensure_console_cleared()

        move_pycharm_cursor_to_file(__file__)
        move_pycharm_cursor_to_file(__file__)

        key_name = "file_skip_limit"
        logging.info(f'''file_cnt={file_cnt} {'%%%FOO%%%' if LTA else ''}''')
        db.set_values(db_id=db.get_id(key_name, func_n), values=file_cnt - 1)

        key_name = "string_location"
        text_to_move_cursor = get_value_by_file_id(file_id=get_file_id(key_name, func_n))
        logging.info(f'''text_to_move_cursor={text_to_move_cursor} {'%%%FOO%%%' if LTA else ''}''')
        move_cursor_to_text_location(text_to_move_cursor=text_to_move_cursor)
        logging.info(f"[{PkMessages2025.STOPPED}] {file_cnt - 1}/{total_file_cnt}")


def pk_ensure_keyboard_mouse_macro(macro_routine):
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