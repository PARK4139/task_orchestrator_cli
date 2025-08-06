if __name__ == "__main__":
    try:
        from pkg_py.functions_split.ensure_todo_list_added import ensure_todo_list_added
        from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
        from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
        from pkg_py.system_object.directories  import D_PROJECT
        # pk_#
        import traceback

        ensure_todo_list_added()
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
