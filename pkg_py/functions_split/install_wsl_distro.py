from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os


def install_wsl_distro(wsl_distro_n):
    std_list = ensure_command_excuted_to_os(cmd=f'wsl --install -d {wsl_distro_n}')
