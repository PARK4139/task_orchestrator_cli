# -*- coding: utf-8 -*-



if __name__ == '__main__':
    try:
        import traceback
        #  import deprecated_get_d_current_n_like_person, get_f_current_n, chcp_65001, get_os_n, organize_tree, gather_empty_d, get_p, organize_d_list_by_stamp
        # from pkg_py.system_object.static_logic import D_PROJECT, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, STAMP_EXCEPTION_DISCOVERED, D_PK_WORKING
        #
        #
        import threading
        import time
        
        if get_os_n() == 'windows':
            chcp_65001()

        # [OPTION]
        # while 1:
        #     organize_tree(d_src=rf"D:\pk_classifying")
        #     sleep(hours=3)
        #     ensure_printed(f'''wait for oraganize tree in loop %%%FOO%%%''', print_color='blue')

        flag_to_detect_enter = 0

        def input_listener():
            global flag_to_detect_enter
            while 1:
                input()
                flag_to_detect_enter = 1


        def run_input_listener_loop():
            global flag_to_detect_enter

            # [OPTION]
            # d_working = rf"G:\Downloads"
            d_working = D_PK_WORKING

            # [OPTION]
            with_walking = True

            while 1:
                for _ in range(3 * 3600):  # 3시간 (3600초) 동안 1초씩 sleep
                    if flag_to_detect_enter:
                        flag_to_detect_enter = 0
                        ensure_printed("Enter detected Restarting loop...", print_color="blue")

                        organize_tree(d_working=d_working, with_walking=with_walking)
                        gather_empty_d(d_working=get_p(d_working))
                        # organize_d_list_by_stamp(d=get_p(d_working))
                        gather_empty_d(d_working=d_working)
                        organize_d_list_by_stamp(d=d_working)
                        ensure_printed(f"wait for enter %%%FOO%%%", print_color='white')
                        break
                    time.sleep(1)

        # thread run ( in background )
        listener_thread = threading.Thread(target=input_listener, daemon=True)
        listener_thread.start()

        run_input_listener_loop()

    except Exception as e:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')
        for traceback_format_exc_str in traceback_format_exc_list:
            ensure_printed(str_working=f'{STAMP_EXCEPTION_DISCOVERED} {traceback_format_exc_str}', print_color='red')
        ensure_printed(str_working=f'{PK_UNDERLINE}', print_color='red')

        

        
