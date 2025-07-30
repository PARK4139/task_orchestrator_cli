if __name__ == "__main__":
    import traceback
    from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
    from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_youtube_cookies_available import ensure_youtube_cookies_available
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

    try:
        if ensure_youtube_cookies_available():
            ensure_printed("✅ YouTube 쿠키가 성공적으로 설정되었습니다!", print_color="green")
        else:
            ensure_printed("❌ YouTube 쿠키 설정에 실패했습니다.", print_color="red")
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
