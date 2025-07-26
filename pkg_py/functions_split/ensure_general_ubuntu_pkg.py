from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_general_ubuntu_pkg(ubuntu_pkg_n, **config_remote_os):
    std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(cmd=f'sudo apt install {ubuntu_pkg_n}',
                                                              **config_remote_os)
    if not len(std_err_list) == 0:
        for std_err_str in std_err_list:
            ensure_printed(str_working=rf'{std_err_str}', print_color='red')
    ensure_printed(str_working=rf'''{ubuntu_pkg_n} installed in {config_remote_os['ip']} {'%%%FOO%%%' if LTA else ''}''',
             print_color='green')
