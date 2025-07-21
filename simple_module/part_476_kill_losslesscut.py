from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE

from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style

from pkg_py.simple_module.part_014_pk_print import pk_print

from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_014_pk_print import pk_print


def kill_losslesscut():
    f_losslesscut_exe = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    cmd_to_os(cmd='taskkill.exe /im LosslessCut.exe /f')
    pk_print(f"{get_nx(f_losslesscut_exe)} is killed", print_color='green')
