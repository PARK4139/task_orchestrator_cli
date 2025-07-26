

import traceback

from colorama import init as pk_colorama_init

from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.colorama_init_once import colorama_init_once
from pkg_py.functions_split.print_red import print_red
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED

# from pkg_py.system_object.500_live_logic import cmd_to_os
#, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
#, print_red

colorama_init_once()

if __name__ == "__main__":
    try:
        cmd_to_os('tmux kill-server ')
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
