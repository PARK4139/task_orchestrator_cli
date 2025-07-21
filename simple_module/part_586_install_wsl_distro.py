from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os


def install_wsl_distro(wsl_distro_n):
    std_list = cmd_to_os(cmd=f'wsl --install -d {wsl_distro_n}')
