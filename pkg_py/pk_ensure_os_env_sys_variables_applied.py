import os
import traceback

import ipdb

from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
from pkg_py.functions_split.ensure_os_env_sys_variables_applied import ensure_os_env_sys_variables_applied
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
# from pkg_py.workspace.pk_workspace import ensure_this_code_operated

if __name__ == "__main__":
    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))
        ensure_os_env_sys_variables_applied()
        ensure_this_code_operated(ipdb)
        if LTA:
            ensure_console_debuggable(ipdb)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
#
