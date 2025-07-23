


from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def ensure_and_get_port_wsl_via_sshd_config(wsl_distro_n):
    std_out_list = None
    f_sshd_config = '/etc/ssh/sshd_config'
    if is_os_windows():
        std_out_list = cmd_to_os(rf'wsl -d {wsl_distro_n} sudo cat {f_sshd_config}')
    else:
        if is_os_wsl_linux():
            if does_pnx_exist(f_sshd_config):
                std_out_list = cmd_to_os(rf'sudo cat {f_sshd_config}')
            else:
                pk_print(f'''f_sshd_config 가 없습니다. {'%%%FOO%%%' if LTA else ''}''')
                cmd_to_os(rf'echo y | sudo apt install --reinstall openssh-server')
                std_out_list = cmd_to_os(rf'sudo cat {f_sshd_config}')
        else:
            pass
    filtered_list = []
    signiture = "#Port 22"
    signiture2 = "Port "
    for std_str in std_out_list:
        if signiture in std_str:
            pk_print(working_str=rf'''The port configuration is commented out in WSL ENVIRONMENT.  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            if is_os_wsl_linux():
                cmd_to_os(rf'code {f_sshd_config}')  # todo port 변경 자동화
                guide_to_manual_remedy(prompt_remedy=f'sudo code {f_sshd_config}')
            raise
        if signiture2 in std_str:
            filtered_list.append(std_str)
    port_wsl = None
    if len(filtered_list[0]) != 0:
        port_wsl = filtered_list[0].replace(signiture2, "")
        if LTA:
            pk_print(f'''port_wsl={port_wsl} {'%%%FOO%%%' if LTA else ''}''')
    return port_wsl
