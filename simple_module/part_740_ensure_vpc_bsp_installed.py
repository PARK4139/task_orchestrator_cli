import zlib
# import win32gui
import webbrowser
import traceback
import toml
from zipfile import BadZipFile
from selenium.common.exceptions import ElementClickInterceptedException
from pynput import mouse
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_etc import PkFilter
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from os import path
from functools import lru_cache
from fastapi import HTTPException
from datetime import date
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_002_is_f import is_f
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ensure_vpc_bsp_installed(vpc_data, config_remote_os):
    if 'no' in vpc_data.vpc_identifier:
        #  \\a2z_AINas_2\30_VISION_DEV\ACU_NO\90_received\20250325 ACU_NO 최종 제출 자료 2차\몹티콘-ACUNO 최종결과물\몹티콘-ACUNO 최종결과물\5.SW 자료\01.BSP\BSP_250312.tar.bz2
        if not is_module_flashed_by_mtc():
            # mtc 모듈은 flash 되어 들어와서 bsp flash 이미지를 tar
            # LINUX_for_Tegra 의 상위 폴더 에서 sudo 붙여서 BSP 압축해제 # 꽤 걸림
            cmd_to_remote_os("cd ~/working_directory_for_flash", config_remote_os)
            # cmd_to_remote_os("sudo tar -xvf BSP20240305.tar", config_remote_os)  # BSP20240305.tar 는 초기버전.
            cmd_to_remote_os("sudo tar -jxvf Flash_Image_Release_1.3.0.tar.bz2 ",
                             config_remote_os)  # a2z 40 nas/30_VISION_DEV/ACU_NX/20_flash/의 최신디렉토리의 파일을 받아야함.
            # tar 인 경우: -j remove->-xvf
        pass
    elif 'nx' in vpc_data.vpc_identifier:
        pass
    elif 'xc' in vpc_data.vpc_identifier:
        pass
    elif 'evm' in vpc_data.vpc_identifier:
        # Driver Package (BSP) DOWNLOAD
        # sudo mv "/mnt/c/Users/user/Downloads/Jetson_LINUX_R32.7.5_aarch64.tbz2" /Downloads/flash/EVM_flash/
        # sudo tar -jxvf /Downloads/flash/EVM_flash/Jetson_LINUX_R32.7.5_aarch64.tbz2 #압축해제
        # sudo find -type f -name "Jetson_LINUX_R32.7.5_aarch64.tbz2"

        # ensure existance JETSON_LINUX_R32.7.5_AARCH64.TBZ2
        #    explorer https://developer.nvidia.com/jetpack-sdk-465  # jetpack 4.6.5 Driver for Jetson AGX Xavier
        #    sudo mv /mnt/c/Users/user/Downloads/Tegra_LINUX_Sample-Root-Filesystem_R32.7.5_aarch64.tbz2 /Downloads/flash/EVM_flash/LINUX_for_Tegra/rootfs

        # ensure tar
        # sudo tar -jxvf /Downloads/flash/EVM_flash/LINUX_for_Tegra/rootfs/Tegra_LINUX_Sample-Root-Filesystem_R32.7.5_aarch64.tbz2 #압축해제
        # sudo find -type f -name "Tegra_LINUX_Sample-Root-Filesystem_R32.7.5_aarch64.tbz2"
        pass
    else:
        pk_print(f'''unknown vpc_data.identifier ({vpc_data.vpc_identifier}) {'%%%FOO%%%' if LTA else ''}''',
                 print_color='red')
        raise
