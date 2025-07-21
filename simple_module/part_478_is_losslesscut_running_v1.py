def is_losslesscut_running_v1():
    from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
    from pkg_py.simple_module.part_005_get_nx import get_nx
    from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
    from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
    from pkg_py.simple_module.part_014_pk_print import pk_print
    # too slow

    f_losslesscut_exe = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    std_list = cmd_to_os(cmd='tasklist.exe | findstr "LosslessCut.exe"')
    if len(std_list) == 0:
        pk_print(f"{get_nx(f_losslesscut_exe)} is not running", print_color='red')
        return False
    pk_print(f"{get_nx(f_losslesscut_exe)} is running", print_color='green')
    return True
