import traceback

# from pkg_py.pk_system_object.static_logic import STAMP_UNIT_TEST_EXCEPTION_DISCOVERED, UNDERLINE, STAMP_TRY_GUIDE, STAMP_PYTHON_DEBUGGING_NOTE, D_PROJECT, STAMP_EXCEPTION_DISCOVERED
# from pkg_py.pk_system_object.print_red import print_red

if __name__ == "__main__":
    #

    try:
        # todo
        import threading
        import time

        # flag로 loop1에서 loop2 내부 제어  #  state_context   또는 state_sqlite로 하는 편이.
        flag_to_detect_enter = 0


        def loop1():
            global flag_to_detect_enter
            pk_print(f"%%%FOO%%%", print_color='green')
            while 1:
                input()
                flag = True
                pk_print(f"%%%FOO%%%", print_color='green')


        def loop2():
            global flag_to_detect_enter
            while 1:
                print(11111111111111111111111111111111111)
                if flag_to_detect_enter:
                    flag = False
                    pk_print(f"%%%FOO%%%", print_color='blue')
                    break
                pk_print(f"%%%FOO%%%", print_color='blue')
                time.sleep(5)


        # loop1 쓰레드 시작(백그라운드)
        loop1_thread = threading.Thread(target=loop1, daemon=True)
        loop1_thread.start()

        # loop2 쓰레드 시작
        loop2()

    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
