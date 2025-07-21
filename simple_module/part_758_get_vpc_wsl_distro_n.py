

def get_vpc_wsl_distro_n(vpc_type):
    if not is_office_pc():
        return PK_WSL_DISTRO_N
    wsl_distro_n = None
    if vpc_type == 'no':
        wsl_distro_n = 'wsl_ubuntu_20_04_no_flash'
    if vpc_type == 'nx':
        wsl_distro_n = 'wsl_ubuntu_20_04_nx_flash_at_250416'
    if vpc_type == 'xc':
        wsl_distro_n = 'wsl_ubuntu_18_04_xc_flash_at_250416'
    if vpc_type == 'evm':
        wsl_distro_n = 'wsl_ubuntu_18_04_evm_flash'
    return wsl_distro_n
