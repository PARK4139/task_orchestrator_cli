if __name__ == "__main__":
    import os

    from pkg_py.functions_split.ensure_git_project_pushed import ensure_git_project_pushed
    from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
    from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
    from pkg_py.functions_split.get_nx import get_nx
    import traceback

    from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
    from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
    from pkg_py.system_object.directories import D_PROJECT_MEMO
    from pkg_py.system_object.directories  import D_PROJECT
    # pk_#

    try:

        ensure_window_title_replaced(get_nx(__file__))
        os.chdir(D_PROJECT_MEMO)
        state = ensure_git_project_pushed(with_commit_massage=False)
        if state["state"]:
            ensure_program_suicided(__file__)  # pk_option

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
