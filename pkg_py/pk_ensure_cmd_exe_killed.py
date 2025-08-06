import traceback

from pkg_py.functions_split import ensure_slept, ensure_console_cleared
from pkg_py.functions_split.ensure_cmd_exe_killed import ensure_cmd_exe_killed
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.system_object.directories  import D_PROJECT
# pk_#

if __name__ == "__main__":
    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        loop_mode = False  # pk_option

        if loop_mode == True:
            while True:
                ensure_console_cleared()
                ensure_cmd_exe_killed()
                ensure_slept(milliseconds=5000)
        else:
            ensure_cmd_exe_killed()

        # ensure_console_debuggable(ipdb=ipdb) # pk_option

    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__)
