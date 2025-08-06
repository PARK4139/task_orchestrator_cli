if __name__ == "__main__":
    import traceback
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_youtube_cookies_available import ensure_youtube_cookies_available
    from pkg_py.system_object.directories  import D_PROJECT
    # pk_#
    from pkg_py.system_object.map_massages import PkMessages2025

    try:
        if ensure_youtube_cookies_available():
            ensure_printed(f"✅ {PkMessages2025.YOUTUBE_COOKIES_SET_SUCCESS}!", print_color="green")
        else:
            ensure_printed(f"❌ {PkMessages2025.YOUTUBE_COOKIES_SET_FAILED}.", print_color="red")
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
