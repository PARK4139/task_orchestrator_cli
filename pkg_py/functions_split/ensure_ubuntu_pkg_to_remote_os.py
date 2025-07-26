import random
import paramiko
import cv2
from os.path import dirname
from functools import partial
from functools import lru_cache
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_ubuntu_pkg_to_remote_os(ubuntu_pkg_n, **config_remote_os):
    if not is_internet_connected():
        ensure_printed(
            f'''can not install ubuntu pakage ({ubuntu_pkg_n}) for internet not connected  {'%%%FOO%%%' if LTA else ''}''',
            print_color='red')
        raise
    if ubuntu_pkg_n == 'docker':
        std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd='docker --version', **config_remote_os)
        if check_signiture_in_loop(time_limit=10, working_list=std_out_list,
                                   signiture="The cmd 'docker' could not be found in this WSL 2 distro.",
                                   signiture_found_ment="docker is not installed in wsl"):
            install_docker(**config_remote_os)
    elif ubuntu_pkg_n == 'net-tools':
        todo('%%%FOO%%%')
    else:
        # std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=f'{ubuntu_pkg_n} --version', **config_remote_os)
        std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(
            cmd=f'sudo apt list --installed | grep {ubuntu_pkg_n}', **config_remote_os)
        signiture = 'installed'
        if check_signiture_in_loop(time_limit=10, working_list=std_out_list, signiture=signiture,
                                   signiture_found_ment=f"{ubuntu_pkg_n} is installed in {config_remote_os['ip']}"):
            ensure_general_ubuntu_pkg(ubuntu_pkg_n=ubuntu_pkg_n, **config_remote_os)
