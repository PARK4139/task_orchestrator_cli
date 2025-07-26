def is_losslesscut_running_v1():
    from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
    from pkg_py.functions_split.ensure_printed import ensure_printed
    # too slow

    f_losslesscut_exe = get_pnx_windows_style(pnx=F_LOSSLESSCUT_EXE)
    std_list = cmd_to_os(cmd='tasklist.exe | findstr "LosslessCut.exe"')
    if len(std_list) == 0:
        ensure_printed(f"{get_nx(f_losslesscut_exe)} is not running", print_color='red')
        return False
    ensure_printed(f"{get_nx(f_losslesscut_exe)} is running", print_color='green')
    return True
