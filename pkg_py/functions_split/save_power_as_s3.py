
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.is_os_windows import is_os_windows


def save_power_as_s3():
    # 절전모드
    # ensure_command_excuted_to_os(cmd=rf"powercfg /setacvalueindex scheme_current sub_buttons button=1-3 action=0")
    cmd = rf"rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
    if is_os_windows():
        ensure_command_excuted_to_os(cmd=cmd)
    else:
        cmd = get_pnx_wsl_unix_style(pnx=cmd)
        ensure_command_excuted_to_os(cmd=cmd)
