__author__ = 'pk == junghoon.park'

if __name__ == "__main__":
    try:
        import traceback
        # from pkg_py.system_object.500_live_logic import assist_to_ensure_f_list_organized_by_x, pk_copy
        #, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        #
        from colorama import init as pk_colorama_init

        colorama_init_once()

        pk_assist_to_ensure_f_list_organized_by_x()

        # kill_pk_program_self(self_f=__file__)
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)