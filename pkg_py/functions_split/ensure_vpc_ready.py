import numpy as np
import ipdb
import datetime
import clipboard
from PySide6.QtWidgets import QApplication
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.pk_press import pk_press
from moviepy import VideoFileClip
from datetime import timedelta

from pkg_py.pk_system_object.Local_test_activate import LTA


def ensure_vpc_ready(vpc_data, wsl_data, **config_remote_os):
    if not LTA:
        ensure_hardware_right(vpc_data)

    wsl_distro_n = wsl_data.vpc_os_distro_n
    vpc_type = vpc_data.vpc_type
    with_flash_image = vpc_data.vpc_with_flash_image

    ensure_wsl_flash_directory_flashable(vpc_data)
    ensure_wsl_sdkmanager(config_remote_os)

    ensure_vpc_ubuntu_pkg_installed(vpc_data, config_remote_os)
    ensure_vpc_bsp_installed(vpc_data, config_remote_os)
    ensure_vpc_recovery_mode_entered(vpc_data, wsl_data, config_remote_os)

    ensure_vpc_flashed(vpc_data, config_remote_os)

    ensure_vpc_network_eh0_connected()  # 114

    ensure_vpc_nvidia_sdk_components_intalled(vpc_data)

    ensure_vpc_smoke_test(vpc_data)

    ensure_vpc_flash_image_saved()

    save_vpc_tracking_map_with_nvidia_serial_to_vpc_mamnagement_map_toml(vpc_data)

    ensure_vpc_report_about_vpc_basic_setup()

    ensure_vpc_os_poweroff()
