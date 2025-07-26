
import json
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.get_pnx_list import get_pnx_list


def remmina(users, ip, remote_os_distro_n, wsl_window_title_seg, pw, exit_mode):
    # todo
    cmd = 'wsl sudo apt update'
    ensure_command_excuted_to_os(cmd=cmd)

    cmd = 'sudo apt install remmina'
    ensure_command_excuted_to_os(cmd=cmd)

    cmd_to_wsl_os_like_person(cmd=rf'remmina -c rdp://{users}@{ip}', remote_os_distro_n=remote_os_distro_n,
                              wsl_window_title_seg=wsl_window_title_seg)
    pass
