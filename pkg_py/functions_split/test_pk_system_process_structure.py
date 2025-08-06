def test_pk_system_process_structure():
    if __name__ == "__main__":
        from pkg_py.functions_split.ensure_program_suicided import ensure_program_suicided
        import traceback
        from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
        from pkg_py.functions_split.get_nx import get_nx
        from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
        from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
        from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
        from pkg_py.system_object.directories  import D_PROJECT
        # pk_#
        try:
            ensure_colorama_initialized_once()
            ensure_window_title_replaced(get_nx(__file__))

            # TODO write core code, here

            ensure_program_suicided(__file__) # pk_option

            # pk_option
            # state =
            # if state["state"]:
            #     ensure_program_suicided(__file__)
            # if LTA:
            #     ensure_console_debuggable(ipdb=ipdb)

            # pk_option
            # ensure_console_debuggable(ipdb=ipdb)
        except Exception as exception:
            ensure_exception_routine_done(traceback=traceback, exception=exception)
        finally:
            ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
