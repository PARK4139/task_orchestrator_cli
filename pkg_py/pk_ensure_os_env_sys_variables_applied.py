import os
import traceback

import ipdb

from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.ensure_os_env_sys_variables_applied import ensure_os_env_sys_variables_applied
from pkg_py.functions_split.colorama_init_once import colorama_init_once
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
# from pkg_py.workspace.pk_workspace import debug_this_code_operated

if __name__ == "__main__":
    try:
        colorama_init_once()
        os.system(f"title {os.path.basename(__file__)}")  # TBD : 데코레이터로 전환
        ensure_os_env_sys_variables_applied()
        debug_this_code_operated(ipdb)
        if LTA:
            ensure_console_debuggable(ipdb)
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
#
