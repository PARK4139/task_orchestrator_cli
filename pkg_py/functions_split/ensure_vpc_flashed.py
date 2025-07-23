# import win32gui
import toml
import subprocess, time
import pyglet
import pickle
import paramiko
import keyboard
import inspect
import importlib
import cv2
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from prompt_toolkit.styles import Style
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.pk_print import pk_print

from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.state_via_context import SpeedControlContext

from passlib.context import CryptContext
from mutagen.mp3 import MP3
from functools import lru_cache
from fastapi import HTTPException
from datetime import date
from cryptography.hazmat.backends import default_backend
from collections import Counter
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.pk_system_object.local_test_activate import LTA

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_vpc_flashed(wsl_data, vpc_data, config_remote_os):
    import time

    # pk_print(str_working=rf'''flash 를 진행하기 위해서 불필요한 창들을 끕니다  {'%%%FOO%%%' if LTA else ''}''', print_color='blue')
    # answer = input(rf"{get_stamp_func_n(func_n=func_n)} >")
    # cmd_to_os(cmd=rf'taskkill /f /im "cmd.exe" ', debug_mode=False)
    # process_kill_wsl_exe(debug_mode=False)
    # process_kill_cmd_exe(debug_mode=False)
    # process_kill_powershell_exe(debug_mode=False)

    wsl_window_title_seg = f"{wsl_data.vpc_user_n}@{wsl_data.HOSTNAME}"
    pk_print(str_working=rf'''wsl_window_title_seg="{wsl_window_title_seg}"  {'%%%FOO%%%' if LTA else ''}''')

    # sudo find -type f -name "flash.sh"
    # sudo find . -type f -name "flash.sh" # f 찾기 #재귀적으로

    if 'no' in vpc_data.vpc_identifier:
        with_flash_image = vpc_data.vpc_with_flash_image
        if vpc_with_flash_image == 0:
            cmd_to_remote_os(cmd='sdkmanager',
                             **config_remote_os)  # excute sdkmanager    # todo sdkmanager cli 로 업그레이드 시도

            ensure_remote_os_connection(**config_remote_os)  # test_ip

            ensure_vpc_jetpack(**config_remote_os)

            ensure_jetson_setup()

            ensure_remote_os_connection(**config_remote_os)  # test_ip

            ensure_power_saving_mode_diasble()
            ensure_screen_black_never()
            ensure_maxn()
            reboot_vpc()

        if vpc_with_flash_image == 1:
            ensure_remote_os_connection(**config_remote_os)

        ensure_vpc_aifw_running(vpc_data, config_remote_os)  # todo
    elif 'nx' in vpc_data.vpc_identifier:
        pass
    elif 'xc' in vpc_data.vpc_identifier:
        while 1:
            # todo : reference : XC도 4.6.6 고정되고 나면 플래시 이미지로만 관리
            if vpc_with_flash_image == 0:
                cmd_to_wsl_os_like_person_deprecated(cmd=rf"echo {pw} | sudo -S ./flash.sh -r jetson-xavier mmcblk0p1",
                                                     remote_os_distro_n=wsl_distro_n,
                                                     wsl_window_title_seg=wsl_window_title_seg)

                # vpc 추가설정
                #  ntp
                #  stacksize

                gen_vpc_flash_image()

            elif vpc_with_flash_image == 1:
                # cd
                # cmd = "cd ~/Downloads/flash/xc_flash/Linux_for_Tegra/"
                # cmd_to_wsl_os_like_person_deprecated(cmd=cmd, remote_os_distro_n=vpc_os_n, wsl_window_title_seg=wsl_window_title_seg, exit_mode=exit_mode)

                # ensure system.img* and system.img.raw
                ensure_location_about_system_img_and_system_img_raw(**config_remote_os)

                # flash
                cmd = rf"echo {pw} | sudo -S ./flash.sh -r jetson-xavier mmcblk0p1"
                cmd_to_wsl_os_like_person_deprecated(cmd=cmd, remote_os_distro_n=wsl_distro_n,
                                                     wsl_window_title_seg=wsl_window_title_seg)

                # sudo mv /home/pk_system/Downloads/flash/xc_flash/Linux_for_Tegra/system.img* /home/pk_system/Downloads/flash/xc_flash/Linux_for_Tegra/rootfs/bin/

                # cmd = rf'sudo find -type f -name "system.img*"'
                # cmd_to_wsl_like_person(cmd=cmd, remote_os_distro_n=remote_os_distro_n, wsl_window_title_seg=wsl_window_title_seg)
                #
                # cmd = rf'df -h'
                # cmd_to_wsl_like_person(cmd=cmd, remote_os_distro_n=remote_os_distro_n, wsl_window_title_seg=wsl_window_title_seg)
                #
                # cmd = rf'explorer \\wsl$'
                # cmd_to_os(cmd=cmd)

                time_s_local = time.localtime(time_s)
                check_manual_task_iteractively(
                    f'''The flash has Started at {time_s_local.tm_hour:02}:{time_s_local.tm_min:02}. Has the flash ended?''')

                elapsed_seconds = time.time() - time_s
                elapsed_minutes = elapsed_seconds / 60

                pk_print(
                    str_working=rf'''FLASH : This function took {elapsed_minutes} minutes  {'%%%FOO%%%' if LTA else ''}''',
                    print_color="green")
                # todo : elapsed_minutes 이걸 f에 매번 기록, 공정시간 자동통계
                # 해당공정이 통계시간보다 느리거나 빠르게 종료되었다는 것을 출력 하도록

            check_manual_task_iteractively(question=rf'''DID YOU EXIT WSL FLASH PROGRAM AT LOCAL?  %%%FOO%%%''')
            check_manual_task_iteractively(question=rf'''DID YOU EXIT WSL ATTACH PROGRAM AT LOCAL?  %%%FOO%%%''')
            # todo : 플래시이미지 재생성 후 해당 내용 네트워크 설정 자동화 후 추후삭제예정
            check_manual_task_iteractively(
                question=rf'''DID YOU SET WIRED CONNECTION 3 AS {vpc_data.vpc_wired_connection_3_new} ?  %%%FOO%%%''')
            ensure_vpc_side_mode(vpc_data=vpc_data, **config_remote_os)
            if not ensure_vpc_accessable(vpc_data, **config_remote_os):
                # history : ensure_vpc_accessable() 수행 -> vpc 접속안됨 -> Wired Connection 활성화 실패->gui 통해서 2.76 으로 ssh 접속 시도->fail->flash 재수행->success
                # flash 재수행해야 하는 경우로 판단
                continue
    elif 'evm' in vpc_data.vpc_identifier:
        if vpc_data.vpc_with_flash_image == 0:
            cmd_to_remote_os(cmd='sdkmanager',
                             **config_remote_os)  # excute sdkmanager    # todo sdkmanager cli 로 업그레이드 시도
            # sdkmanager    #  sdkmanager --archived-versions 이거 아님. # 안될때 sudo sdkmanager 로그인 했다가 종료하고 sdkmanager 로 다시 접속
            # cmd_run_via_wsl(wsl_cmd=wsl_cmd, remote_os_distro_n=remote_os_distro_n, window_title_seg=wsl_windows_title_seg)

            # WSL 에서 실행중인데 cmd  를 관리자 권한으로 실행하고 WSL 을 실행해서 sdkmanger 실행했는데 여전히 You do not have permission to access the download folder. 나와
            # download 폴더를 변경 create and select pk_download   -> ~/Downloads/pk_nvidia ->   flash/evm_flash

            # nvidia developer login
            # 로그인웹이 자동으로 안열리는 경우, 재부팅부터 해보자, QR code 로 시도
            # smart phone 에서 QR 촬영을 해서 smart phone web 열리면 로그인
            # 다른거 치라는데 패스워드 치면 됨.
            # 로그인 되면서 device type select 창이 나옴.
            # Jetson AGX Xavier
            # OK
            # Later

            # show all versions
            # 4.6.6
            # [fail] ensure only os without nvidia sdk component
            # ensure both os and nvidia sdk component
            # continue
            # ensure download now. install later. disable # 이거 체크하면 flash 진행하지 않음
            # ensure I accpet the terms and conditions of the license agreements. able
            # continue
            # manual flash try, # 안해도 될 듯 download now. install later. able 처리해서 발생한 문제
            # wait for OEM Configuration setting pop up
            # Runtime # OEM Configuration # 자꾸 안되서 Runtime 안하고 pre-config 로 해봄 pre-config는 default 임
            # Flash
            # finish

            # [fail] ensure ubuntu OEM : in evm
            # evm
            # EVM terminal x
            # accept blah lisence
            # display on
            # agree
            # english
            # english(US)
            # english(US)
            # seoul
            # nvidia
            # nvidia
            # nvidia
            # nvidia
            # nvidia
            # MAXN
            # log in automatically
            # Install # if this process fail, retry flash

            # set evm network wired connection 1 as 192.168.2.124 22 192.168.1.1 8.8.8.8 manualy in evm
            # sudo apt update in evm
            # skip check
            # pkill sdkmanger-gui
            # sdkmanger
            # ensure only nvidia sdk component without os(jetpack)
            # Ethernet
            # 192.168.2.124
            # nvidia
            # nvidia
            # install

            # ensure log in automatically

            # ensure MAXN

            # ensure no passwd

            # ensure stack size 10240 #MEMORY LEAK 예방 #10240로 합의
            # sudo vi /etc/security/limits.conf
            # #End of file
            # nvidia hard stack 10240
            # nvidia soft stack 10240
            # ubuntu hard stack 10240
            # ubuntu soft stack 10240
            # root hard stack 10240
            # root soft stack 10240
            # :wq
            # cat /etc/security/limits.conf

            # ensure ntp available
            # sudo vi /etc/systemd/timesyncd.conf
            # [Time]
            # NTP=192.168.10.10 #server ip(control PC)
            # FallbackNTP=ntp.ubuntu.com
            # RootDistanceMaxSec=15 #5→15
            # PollIntervalMinSec=32
            # PollIntervalMaxSec=2048
            # # timedatectl set-ntp no #자동 시간동기화 해제
            # # date
            # # timedatectl set-time "2024-10-28 13:26:00" #수동 시간 SETTING

            # ensure auto reboot

            # make flash image # started at 15:18
            # recovery mode again
            # sudo find /home -type f -name "flash.sh"
            # evm_flash_jetpack_4_6_6_ready.img 는 ip124,  ntp, stack, ensure 함.
            # evm_flash_jetpack_4_6_6_with_side_a.img
            # evm_flash_jetpack_4_6_6_with_side_b.img
            # sudo ./flash.sh -r -k APP -G evm_flash_jetpack_4_6_6_ready.img jetson-xavier mmcblk0p1
            # sudo ./flash.sh -r -k APP -G evm_flash_jetpack_4_6_6_with_side_a.img jetson-xavier mmcblk0p1
            # sudo ./flash.sh -r -k APP -G evm_flash_jetpack_4_6_6_with_side_b.img jetson-xavier mmcblk0p1
            # sudo find /home -type f -name "evm_flash_jetpack_4_6_6*"
            # ended at mkr.
            pass
        elif vpc_data.vpc_with_flash_image == 1:
            # sudo ./flash.sh -r -k APP -G EVM_flash_241125.img jetson-xavier mmcblk0p1
            pass
    else:
        pk_print(f'''unknown vpc_data.identifier ({vpc_data.vpc_identifier}) {'%%%FOO%%%' if LTA else ''}''',
                 print_color='red')
        raise
