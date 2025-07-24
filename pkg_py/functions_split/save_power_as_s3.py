
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows


def save_power_as_s3():
    # 절전모드
    # cmd_to_os(cmd=rf"powercfg /setacvalueindex scheme_current sub_buttons button=1-3 action=0")
    cmd = rf"rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    if is_os_windows():
        cmd_to_os(cmd=cmd)
    else:
        cmd = get_pnx_wsl_unix_style(pnx=cmd)
        cmd_to_os(cmd=cmd)
