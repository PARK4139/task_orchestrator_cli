from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_pnx_ubuntu_pkg_installed import get_pnx_ubuntu_pkg_installed

from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_ubuntu_pkg_installed(ubuntu_pkg_n):
    import shutil

    while 1:
        ubuntu_pkg_bin = shutil.which(ubuntu_pkg_n)
        if not ubuntu_pkg_bin:
            ensure_printed(f"{ubuntu_pkg_n} is not installed")
            ensure_printed(f"try to install {ubuntu_pkg_n} now")
            ensure_command_excuted_to_os(f"sudo apt install -y {ubuntu_pkg_n}")
            ubuntu_pkg_bin = get_pnx_ubuntu_pkg_installed(ubuntu_pkg_n)
            if ubuntu_pkg_bin is None:
                continue
        else:
            ensure_printed(f"{ubuntu_pkg_n} is installed")
            break
