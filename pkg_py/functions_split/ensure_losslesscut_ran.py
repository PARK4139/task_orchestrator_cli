from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.local_test_activate import LTA


@ensure_seconds_measured
def ensure_losslesscut_ran():
    import os
    f_losslesscut_exe = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    ensure_command_excuted_to_os(cmd=rf'''start "" /MAX "{f_losslesscut_exe}"''', mode='a')



def is_losslesscut_enabled():
    import os
    f_losslesscut_exe = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    if not os.path.exists(f_losslesscut_exe):
        if LTA:
            ensure_printed(f"{get_nx(f_losslesscut_exe)} is not installed", print_color='red')
        return False
    else:
        if LTA:
            ensure_printed(f"{get_nx(f_losslesscut_exe)} is installed", print_color='green')
        return True