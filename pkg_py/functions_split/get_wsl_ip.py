def get_wsl_ip(wsl_distro_n):
    from pkg_py.functions_split.ensure_pinged import ensure_pinged
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    std_out_list = None
    if is_os_windows():
        std_out_list = ensure_command_excuted_to_os(rf'wsl -d {wsl_distro_n} hostname -I', encoding='utf-8')
    else:
        if is_os_wsl_linux():
            std_out_list = ensure_command_excuted_to_os(rf'hostname -I', encoding='utf-8')
        else:
            pass
    wsl_ip = std_out_list[0].split(" ")[0]
    if wsl_ip:
        if not ensure_pinged(ip=wsl_ip):
            raise "pk_?????"
    return wsl_ip
