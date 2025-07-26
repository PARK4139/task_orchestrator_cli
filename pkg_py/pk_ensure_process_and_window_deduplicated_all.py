from pkg_py.functions_split.ensure_cmd_exe_deduplicated_all import ensure_cmd_exe_deduplicated_all

if __name__ == '__main__':
    try:
        from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
        from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
        # from pkg_py.workspace.pk_workspace import ensure_cmd_exe_deduplicated, ensure_cmd_exe_deduplicated_all
        import traceback
        from pkg_py.system_object.directories_reuseable import D_PROJECT
        from pkg_py.system_object.etc import PK_UNDERLINE
        from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED
        from pkg_py.functions_split.is_os_windows import is_os_windows
        from pkg_py.functions_split.ensure_printed import ensure_printed
        from pkg_py.functions_split.ensure_windows_deduplicated import ensure_windows_deduplicated
        from pkg_py.functions_split.chcp_65001 import chcp_65001
        from pkg_py.functions_split.get_f_current_n import get_f_current_n
        from pkg_py.functions_split.deprecated_get_d_current_n_like_person import deprecated_get_d_current_n_like_person
        from pkg_py.functions_split.ensure_slept import ensure_slept

        from pkg_py.system_object.local_test_activate import LTA
        from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared

        from pkg_py.functions_split.ensure_printed import ensure_printed

        from pkg_py.functions_split.ensure_windows_closed import ensure_windows_closed
        from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
        from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
        from pkg_py.functions_split.ensure_func_info_loaded import ensure_func_info_loaded

        from pkg_py.pk_interface_graphic_user import get_windows_opened


        def ensure_windows_deduplicated_in_loop():

            import threading

            flag_to_detect_enter = 0  # 루프제어용

            def listen_enter():
                global flag_to_detect_enter
                while 1:
                    input()
                    flag_to_detect_enter = 1

            def run_main_loop():
                global flag_to_detect_enter
                previous_windows_opened_list = get_windows_opened()
                len_before: int = 0
                while 1:
                    # deduplicate explorer.exe process
                    current_windows_opened_list = get_windows_opened()
                    len_current = len(current_windows_opened_list)
                    if len_before != len_current:
                        ensure_printed(f'''len_before={len_before}  {'%%%FOO%%%' if LTA else ''}''')
                        ensure_printed(f'''len_current={len_current}  {'%%%FOO%%%' if LTA else ''}''')
                        ensure_iterable_printed_as_vertical(item_iterable=current_windows_opened_list,
                                                   item_iterable_n="current_windows_opened_list")
                        len_before = len_current
                    if len(current_windows_opened_list) != len(previous_windows_opened_list):
                        # ensure_printed(f'''len(current_windows_opened_list)={len(current_windows_opened_list)} len(previous_windows_opened_list)={len(previous_windows_opened_list)}  {'%%%FOO%%%' if LTA else ''}''',print_color="blue")
                        ensure_windows_closed()
                        title = ensure_func_info_loaded(func_n="ensure_windows_closed")["title"]
                        ensure_window_to_front(window_title_seg=title)
                        previous_windows_opened_list = current_windows_opened_list

                    # deduplicate cmd.exe process
                    ensure_cmd_exe_deduplicated_all()

                    # ensure_slept(milliseconds=500)
                    # ensure_slept(milliseconds=1000)
                    # ensure_slept(milliseconds=2000) # pk_option
                    ensure_slept(milliseconds=10000) # pk_option

                    ensure_console_cleared()

            # start thread ( in background )
            thread = threading.Thread(target=listen_enter, daemon=True)
            thread.start()

            # run main loop
            run_main_loop()

        ensure_windows_deduplicated_in_loop()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
