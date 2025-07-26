import traceback

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_do_exception_routine import ensure_do_exception_routine
from pkg_py.functions_split.ensure_do_finally_routine import ensure_do_finally_routine
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.measure_seconds import measure_seconds
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
# from pkg_py.workspace.pk_workspace import kill_cmd_exe

# from pkg_py.system_object.500_live_logic import copy, kill_cmd_exe, cmd_to_os
#
# from pkg_py.system_object.static_logic import D_PROJECT
#, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED

@measure_seconds
def _kill1(img_name):
    cmd_to_os(f'taskkill /f /im "{img_name}"')

@measure_seconds
def _kill2(img_name):
    cmd_to_os(f'wmic process where name="{img_name}" delete ')

@measure_seconds
def _kill3(img_name):
    kill_cmd_exe()

if __name__ == "__main__":
    try:
        while True:
            decision = get_value_completed(key_hint=rf"{PkMessages2025.PROCESS} {PkMessages2025.KILL}=", values=[PkMessages2025.YES, PkMessages2025.NO])
            if decision == PkMessages2025.YES:
                img_name = 'cmd.exe'

                _kill1(img_name)
                # _kill2(img_name)
                # _kill3(img_name)




    except Exception as exception:
        ensure_do_exception_routine(traceback=traceback, exception=exception)

    finally:
        ensure_do_finally_routine(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
