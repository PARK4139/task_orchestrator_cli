def ensure_wsl_ip_printed():
    from pkg_py.functions_split.get_wsl_ip import get_wsl_ip
    wsl_ip = get_wsl_ip(wsl_distro_n="Ubuntu-24.04")
    print(wsl_ip)
