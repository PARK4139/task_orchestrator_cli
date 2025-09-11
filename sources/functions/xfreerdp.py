from functions.cmd_to_wsl_os_like_human import cmd_to_wsl_os_like_human
from sources.functions.ensure_command_executed import ensure_command_executed


def xfreerdp(users, ip, distro_name, wsl_window_title_seg, pw, exit_mode):
    # todo
    cmd = 'wsl sudo apt update'
    ensure_command_executed(cmd=cmd)

    cmd = 'sudo apt install freerdp2-x11'
    ensure_command_executed(cmd=cmd)

    #         ensure_writen_like_human(rf'xfreerdp /v:{ip}:3390 /u:{users} /p:{pw} /sec:nla /clipboard',distro_name=distro_name, wsl_window_title_seg=wsl_window_title_seg)
    #         ensure_writen_like_human(rf'xfreerdp /v:{ip}:3390 /u:{users} /p:{pw} /sec:tls /clipboard',distro_name=distro_name, wsl_window_title_seg=wsl_window_title_seg)
    cmd_to_wsl_os_like_human(cmd=rf'xfreerdp /v:{ip}:3390 /u:{users} /p:{pw} /clipboard',
                             distro_name=distro_name, wsl_window_title_seg=wsl_window_title_seg)
