def ensure_windows_deduplicated():
    from pkg_py.functions_split.pk_sleep import pk_sleep

    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared

    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.get_window_opened_list import get_window_opened_list
    from pkg_py.functions_split.ensure_windows_closed import ensure_windows_closed
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
    from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
    from pkg_py.functions_split.ensure_func_info_loaded import ensure_func_info_loaded

    import threading

    flag_to_detect_enter = 0  # 루프제어용

    def listen_enter():
        global flag_to_detect_enter
        while 1:
            input()
            flag_to_detect_enter = 1

    def run_main_loop():
        global flag_to_detect_enter
        previous_windows_opened_list = get_window_opened_list()
        len_before: int = 0
        while 1:
            # kill_windows_duplicated
            current_windows_opened_list = get_window_opened_list()
            len_current = len(current_windows_opened_list)
            if len_before != len_current:
                pk_print(f'''len_before={len_before}  {'%%%FOO%%%' if LTA else ''}''')
                pk_print(f'''len_current={len_current}  {'%%%FOO%%%' if LTA else ''}''')
                print_iterable_as_vertical(item_iterable=current_windows_opened_list,
                                           item_iterable_n="current_windows_opened_list")
                len_before = len_current
            if len(current_windows_opened_list) != len(previous_windows_opened_list):
                # pk_print(f'''len(current_windows_opened_list)={len(current_windows_opened_list)} len(previous_windows_opened_list)={len(previous_windows_opened_list)}  {'%%%FOO%%%' if LTA else ''}''',print_color="blue")
                ensure_windows_closed()
                title = ensure_func_info_loaded(func_n="ensure_windows_closed")["title"]
                ensure_window_to_front(window_title_seg=title)
                previous_windows_opened_list = current_windows_opened_list
            pk_sleep(seconds=1)
            ensure_console_cleared()

    # start thread ( in background )
    thread = threading.Thread(target=listen_enter, daemon=True)
    thread.start()

    # run main loop
    run_main_loop()
