from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE

from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style

from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed


def kill_losslesscut():
    f_losslesscut_exe = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    ensure_command_excuted_to_os(cmd='taskkill.exe /im LosslessCut.exe /f')
    ensure_printed(f"{get_nx(f_losslesscut_exe)} is killed", print_color='green')
