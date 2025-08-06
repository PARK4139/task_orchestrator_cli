if __name__ == "__main__":
    try:
        from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
        from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
        from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
        from pkg_py.system_object.directories  import D_PROJECT
        # pk_#
        import traceback
        from colorama import init as pk_colorama_init

        ensure_colorama_initialized_once()
        ensure_files_organized_by_x() # todo
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
