if __name__ == "__main__":
    import traceback
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.system_object.directories_reuseable import D_PROJECT
    from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

    import sys
    import os

    from pkg_py.system_object.etc import PK_UNDERLINE
    from pkg_py.system_object.color_map import ANSI_COLOR_MAP

    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        print(f"{ANSI_COLOR_MAP["BRIGHT_MAGENTA"]}{PK_UNDERLINE}{ANSI_COLOR_MAP["RESET"]}")
        print(f"{ANSI_COLOR_MAP["BRIGHT_MAGENTA"]}PK System info{ANSI_COLOR_MAP["RESET"]}")
        print(f"🐍 Python version: {sys.version}")
        print(f"📦 PK System version: {__import__('pkg_py').__version__}")
        print("✅ PK System is ready!")

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
