from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
from pkg_py.functions_split.get_d_working_in_python import get_pwd_in_python
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
from pkg_py.functions_split.ensure_copied import ensure_copied
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.local_test_activate import LTA



import traceback

from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
from pkg_py.functions_split.get_nx import get_nx
import ipdb

from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

if __name__ == "__main__":
    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))

        pwd = get_pwd_in_python()
        ensure_printed(f'''pwd={pwd} {'%%%FOO%%%' if LTA else ''}''')

        ensure_copied(pwd)

        ensure_pk_program_suicided(self_f=__file__) # pk_option

        if LTA:
            ensure_console_debuggable(ipdb)
    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)
    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)

