import os

from pkg_py.functions_split.should_i_search_to_chatGPT import should_i_search_to_chatGPT

if __name__ == "__main__":
    try:
        ensure_window_title_replaced(get_nx(__file__))
        while 1:
            should_i_search_to_chatGPT()
        if LTA:
            ensure_console_debuggable()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
