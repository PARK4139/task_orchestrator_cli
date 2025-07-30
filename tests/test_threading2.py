# -*- coding: utf-8 -*-



if __name__ == '__main__':
    #  import deprecated_get_d_current_n_like_person, get_f_current_n, chcp_65001, get_os_n
    #, print_yellow
    #, D_PKG_WINDOWS
    import threading
    import time

    try:
        if get_os_n() == 'windows':
            chcp_65001()

        # 전역 플래그를 사용해 루프 재exec  제어
        flag_to_detect_enter = 0


        def listen_enter():
            global flag_to_detect_enter
            while 1:
                input()
                flag_to_detect_enter = 1


        def main_loop():
            global flag_to_detect_enter
            while 1:
                # liost

                # todo
                print("todo")

                # sleep
                sleep_seconds = 3
                for _ in range(sleep_seconds):
                    if flag_to_detect_enter:
                        ensure_printed("Enter detected Restarting loop...", print_color="blue")

                        # todo
                        print("todo")

                        flag_to_detect_enter = 0
                        ensure_printed(f"wait for enter %%%FOO%%%", print_color='white')
                        break
                    time.sleep(1)

        # thread run ( in background )
        thread = threading.Thread(target=listen_enter, daemon=True)
        thread.start()

        # main loop run 
        main_loop()

    except Exception as e:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

        

        





