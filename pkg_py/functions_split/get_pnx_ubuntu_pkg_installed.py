def get_pnx_ubuntu_pkg_installed(ubuntu_pkg_n):
    import shutil
    return shutil.which(ubuntu_pkg_n)
