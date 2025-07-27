

def get_wsl_data_raw_data(vpc_data_raw):
    import os

    wsl_data_raw = A2zCarDataStructure.RemoteDeviceDataStructure()
    # if not is_wsl_distro_enabled(wsl_distro_n=PK_WSL_DISTRO_N):
    #     ensure_wsl_distro_enabled(wsl_distro_n='Ubuntu-24.04')
    #     mkr.

    wsl_data_raw.vpc_os_distro_n = get_vpc_wsl_distro_n(vpc_data_raw.vpc_type)
    wsl_distro_n = wsl_data_raw.vpc_os_distro_n
    wsl_data_raw.vpc_ip = get_wsl_ip(wsl_distro_n)
    wsl_data_raw.vpc_port = ensure_and_get_wsl_port(wsl_distro_n)
    wsl_data_raw.vpc_user_n = get_wsl_user_n(wsl_distro_n)
    wsl_data_raw.vpc_pw = get_wsl_pw(wsl_distro_n)
    wsl_data_raw.vpc_local_ssh_public_key = os.path.join(D_HOME, ".ssh", "id_ed25519.pub")
    wsl_data_raw.vpc_local_ssh_private_key = os.path.expanduser("~/.ssh/id_ed25519")
    return wsl_data_raw
