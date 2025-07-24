
if __name__ == "__main__":
    try:
        import traceback

        #  import assist_to_command_via_voice_kiri
        from pkg_py.functions_split.pk_print import pk_print
        #, D_PROJECT
        # from pkg_py.system_object.500_live_logic import pk_copy
        # from pkg_py.system_object.static_logic import STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED

        assist_to_command_via_voice_kiri()
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
