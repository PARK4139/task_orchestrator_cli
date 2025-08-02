

import sys
import traceback

from colorama import init as pk_colorama_init

# from pkg_py.system_object.500_live_logic import ensure_command_excuted_to_os
#, STAMP_TRY_GUIDE, D_PROJECT, STAMP_UNIT_TEST_EXCEPTION_DISCOVERED
#, print_red

ensure_colorama_initialized_once()

if __name__ == "__main__":
    try:
        ensure_command_excuted_to_os(cmd=f'sudo rm -rf {D_PROJECT}/uv.lock')
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
        sys.exit(1)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)