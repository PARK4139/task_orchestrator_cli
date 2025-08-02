def ensure_pycharm_module_optimize():
    from pkg_py.refactor.pk_ensure_keyboard_mouse_macro import PkMacroRoutines
    import os
    import shutil
    import logging
    import sys
    import inspect
    import pyautogui
    from datetime import datetime
    from os import environ
    from pkg_py.functions_split.close_pycharm_tab import close_pycharm_tab
    from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
    from pkg_py.functions_split.extend_pycharm_code import extend_pycharm_code
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_str_from_f import get_str_from_f
    from pkg_py.functions_split.get_value_by_file_id import get_value_by_file_id
    from pkg_py.functions_split.ensure_cursor_moved_to_text_location import ensure_cursor_moved_to_text_location
    from pkg_py.functions_split.move_cursor_to_top_of_pycarm_code import move_cursor_to_top_of_pycarm_code
    from pkg_py.functions_split.move_pycharm_cursor_to_file import move_pycharm_cursor_to_file
    from pkg_py.functions_split.open_pycharm_parrete import open_pycharm_parrete
    from pkg_py.functions_split.paste_and_enter import paste_and_enter
    from pkg_py.functions_split.press_ctrl_alt_l_nth import press_ctrl_alt_l_nth
    from pkg_py.functions_split.ensure_loop_delayed_at_loop_foot import ensure_loop_delayed_at_loop_foot
    from pkg_py.functions_split.ensure_copied import ensure_copied
    from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
    from pkg_py.functions_split.get_d_working import get_d_working
    from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.state_via_database import PkSqlite3DB
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.system_object.directories import D_PKG_ARCHIVED

    d_working = rf"{environ['USERPROFILE']}\Downloads\pk_system\pkg_py"
    func_n = inspect.currentframe().f_code.co_name
    db = PkSqlite3DB()
    PROCESS_NAME = PkMacroRoutines.ENSURE_PYCHARM_CODE_OPTIMIZED
    EXCLUDED_PREFIXES = ["a2z_", "prefix_to_exclude_"]
    ALLOWED_EXTENSIONS = [".py"]
    key_name = "DIRECTORY_TO_DO_MACRO_ROUTINE"
    if LTA:
        DIRECTORY_TO_DO_MACRO_ROUTINE = os.path.normpath(d_working)
    else:
        DIRECTORY_TO_DO_MACRO_ROUTINE = os.path.normpath(
            get_values_from_historical_file_routine(
                file_id=db.get_db_id(key_name, func_n),
                key_hint=f'{key_name}=',
                options_default=[get_d_working()]
            )
        )

    if not does_pnx_exist(DIRECTORY_TO_DO_MACRO_ROUTINE):
        ensure_pk_system_exit_silent()

    timestamp = datetime.now().strftime("%Y_%m%d_%H%M_%S")
    wd_name = os.path.basename(DIRECTORY_TO_DO_MACRO_ROUTINE.rstrip("/\\"))
    archive_basename = os.path.join(D_PKG_ARCHIVED, f"{wd_name}_archived_before_work_via_{func_n}_{timestamp}")
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
    logging.debug(f"[DEBUG] filtered_files={filtered_files}")

    if not filtered_files:
        logging.info(f"[{PkMessages2025.STOPPED}] No files matched filter condition.")
        ensure_pk_system_exit_silent()

    total_file_cnt = len(filtered_files)

    # 🔹 file_skip_limit 먼저 불러오고 file_cnt를 그 다음에 초기화해야 함
    key_name = "file_skip_limit"
    file_skip_limit = db.get_values(db_id=db.get_db_id(key_name, func_n))
    if file_skip_limit is None:
        file_skip_limit = get_values_from_historical_file_routine(
            file_id=get_file_id(key_name, func_n),
            key_hint=f'{key_name}=',
            options_default=["0", str(total_file_cnt)],
            editable=True,
        )
    file_skip_limit = int(file_skip_limit)

    loop_cnt = 1
    file_cnt = file_skip_limit + 1  # ✅ Save point 이후부터 시작

    mouse_x, mouse_y = pyautogui.position()
    file_name_last = None
    logging.info(f"[INFO] total_file_cnt={total_file_cnt}, file_skip_limit={file_skip_limit}")
    try:
        for file_name in filtered_files:
            file_abspath = os.path.join(DIRECTORY_TO_DO_MACRO_ROUTINE, file_name)
            new_x, new_y = pyautogui.position()
            if (new_x, new_y) != (mouse_x, mouse_y):
                logging.warning(f"[{PkMessages2025.DETECTED}] Mouse moved: start=({mouse_x},{mouse_y}) → now=({new_x},{new_y})")
                sys.exit(0)

            if file_cnt <= file_skip_limit:
                logging.info(f"[{PkMessages2025.SKIPPED}] {file_cnt}/{total_file_cnt} (reason: file_cnt <= file_skip_limit)")
            elif get_str_from_f(file_abspath).strip().startswith("def"):
                logging.info(f"[{PkMessages2025.SKIPPED}] {file_cnt}/{total_file_cnt} (reason: content starts with 'def')")
            else:
                logging.info(f"[{PkMessages2025.STARTED}] {file_cnt}/{total_file_cnt}")
                logging.info(f"[{PkMessages2025.STARTED}] {file_name}")
                file_name_last = file_name

                file_base = os.path.splitext(file_name)[0]
                ensure_copied(file_base)
                open_pycharm_parrete()
                paste_and_enter()
                move_cursor_to_top_of_pycarm_code()
                extend_pycharm_code()
                press_ctrl_alt_l_nth()
                close_pycharm_tab()

                ensure_loop_delayed_at_loop_foot(loop_cnt, mode_level=2, miliseconds_limit=50)
                loop_cnt += 1

            file_cnt += 1

    except Exception as e:
        logging.exception(f"[ERROR] 예외 발생: {e}")
    finally:
        move_pycharm_cursor_to_file(__file__)
        move_pycharm_cursor_to_file(__file__)

        key_name = "file_skip_limit"
        logging.info(f"[INFO] file_cnt={file_cnt}")
        db.set_values(db_id=db.get_db_id(key_name, func_n), values=file_cnt - 1)

        key_name = "cursor_location"
        text_to_move_cursor = get_value_by_file_id(file_id=get_file_id(key_name, func_n))
        logging.info(f"[INFO] text_to_move_cursor={text_to_move_cursor}")
        ensure_cursor_moved_to_text_location(text_to_move_cursor=text_to_move_cursor)
        logging.info(f"[{PkMessages2025.STOPPED}] {file_cnt - 1}/{total_file_cnt}")
