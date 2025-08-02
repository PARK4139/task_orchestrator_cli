import traceback

from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
# from pkg_py.workspace.pk_workspace import kill_cmd_exe

# from pkg_py.system_object.500_live_logic import copy, kill_cmd_exe, ensure_command_excuted_to_os
#
# from pkg_py.system_object.static_logic import D_PROJECT
#, STAMP_TRY_GUIDE, STAMP_EXCEPTION_DISCOVERED

@ensure_seconds_measured
def _kill1(img_name):
    ensure_command_excuted_to_os(f'taskkill /f /im "{img_name}"')

@ensure_seconds_measured
def _kill2(img_name):
    ensure_command_excuted_to_os(f'wmic process where name="{img_name}" delete ')

@ensure_seconds_measured
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
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE)
        
