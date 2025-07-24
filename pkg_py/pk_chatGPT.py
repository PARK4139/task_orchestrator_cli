import os

from pkg_py.functions_split.should_i_search_to_chatGPT import should_i_search_to_chatGPT

if __name__ == "__main__":
    try:
        os.system(f"title {os.path.basename(__file__)}")  # TBD : 데코레이터로 전환
        while 1:
            should_i_search_to_chatGPT()
            print()
            print()
            print()
            print()
        if LTA:
            ensure_console_debuggable()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
