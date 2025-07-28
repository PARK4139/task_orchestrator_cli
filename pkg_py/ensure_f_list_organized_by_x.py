__author__ = 'pk == junghoon.park'

from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

if __name__ == "__main__":
    try:
        import traceback
        # from pkg_py.system_object.500_live_logic import assist_to_ensure_f_list_organized_by_x, ensure_copied
        #, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
        #
        from colorama import init as pk_colorama_init

        ensure_colorama_initialized_once()

        ensure_f_list_organized_by_x()

        # kill_pk_program_self(self_f=__file__)
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)