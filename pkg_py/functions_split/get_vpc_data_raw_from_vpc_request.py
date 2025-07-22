import zipfile
# import win32process
import win32com.client
import tomllib
import time
import sys
import subprocess
import shutil
import secrets
# import pywin32
import pyaudio
import mutagen
import hashlib
from yt_dlp import YoutubeDL
from tkinter import UNDERLINE
from selenium.webdriver.common.action_chains import ActionChains
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from gtts import gTTS
from dirsync import sync
from Cryptodome.Cipher import AES
from collections import Counter
from bs4 import BeautifulSoup
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style


def get_vpc_data_raw_from_vpc_request():
    import os

    vpc_data_raw = A2zCarDataStructure.RemoteDeviceDataStructure()

    # no
    # request_template = {}
    # request_template['vpc_type'] = 'no'
    # request_template['vpc_purpose'] = 'a2z_vehicle(undefined purpose)'  # 'a2z_vehicle(undefined purpose)', 'a2z_vehicle(For Internal A2Z Development)'
    # request_template['vpc_aifw_version'] = '2.2.4.0'
    # request_template['vpc_jetpack_version'] = '5.1.2'
    # request_template['vpc_jetson_setup_ver'] = '2.0.1'
    # request_template['vpc_side'] = 'a'
    # request_template['vpc_aifw_packing_mode'] = 1  # 1 : a2z 납품차량용   , 0 : a2z 내부테스트용
    # request_template['vpc_flash_image_version'] = '1.0.0'
    # if request_template['vpc_flash_image_version'] == '':
    #     request_template['vpc_with_flash_image'] = 0  # 0 : flash image 없음
    # else:
    #     request_template['vpc_with_flash_image'] = 1  # 1 : flash image 있음
    # request_template['vpc_identifier_number'] = f'00'
    # request_template['vpc_identifier'] = f'{request_template['vpc_type']} #{request_template['vpc_identifier_number']}'

    # nx
    # request_template = {}
    # request_template['vpc_type'] = 'nx'
    # request_template['vpc_purpose'] = 'a2z_vehicle(undefined purpose)'  # 'a2z_vehicle(undefined purpose)', 'a2z_vehicle(For Internal A2Z Development)'
    # request_template['vpc_aifw_version'] = '2.2.4.0'
    # request_template['vpc_jetpack_version'] = '5.0.2'
    # request_template['vpc_jetson_setup_ver'] = '2.0.1'
    # request_template['vpc_side'] = 'a'
    # request_template['vpc_aifw_packing_mode'] = 1  # 1 : a2z 납품차량용   , 0 : a2z 내부테스트용
    # request_template['vpc_flash_image_version'] = '1.3.0'
    # if request_template['vpc_flash_image_version'] == '':
    #     request_template['vpc_with_flash_image'] = 0  # 0 : flash image 없음
    # else:
    #     request_template['vpc_with_flash_image'] = 1  # 1 : flash image 있음
    # request_template['vpc_identifier_number'] = f'00'
    # request_template['vpc_identifier'] = f'{request_template['vpc_type']} #{request_template['vpc_identifier_number']}'

    # xc
    # request_template = {}
    # request_template['vpc_type'] = 'xc'
    # request_template['vpc_purpose'] = 'a2z_vehicle(undefined purpose)'  # 'a2z_vehicle(undefined purpose)', 'a2z_vehicle(For Internal A2Z Development)'
    # request_template['vpc_aifw_version'] = '1.2.1'
    # request_template['vpc_jetpack_version'] = '4.6.5'
    # request_template['vpc_jetson_setup_ver'] = ''
    # request_template['vpc_side'] = 'a'
    # request_template['vpc_aifw_packing_mode'] = 1  # 1 : a2z 납품차량용   , 0 : a2z 내부테스트용
    # request_template['vpc_flash_image_version'] = '1.0.0'
    # if request_template['vpc_flash_image_version'] == '':
    #     request_template['vpc_with_flash_image'] = 0  # 0 : flash image 없음
    # else:
    #     request_template['vpc_with_flash_image'] = 1  # 1 : flash image 있음
    # request_template['vpc_identifier_number'] = f'00'
    # request_template['vpc_identifier'] = f'{request_template['vpc_type']} #{request_template['vpc_identifier_number']}'

    # tab version
    request_template = {}
    request_template['vpc_type'] = get_value_completed(key_hint="request_template['vpc_type']=",
                                                       values=['xc', 'nx', 'no'])
    request_template['vpc_purpose'] = get_value_completed(key_hint="request_template['vpc_purpose']=",
                                                          values=['a2z_vehicle(undefined purpose)',
                                                                  'a2z_vehicle(undefined purpose)',
                                                                  'a2z_vehicle(For Internal A2Z Development)'])
    request_template['vpc_aifw_version'] = get_value_completed(key_hint="request_template['vpc_aifw_version']=",
                                                               values=['1.2.1', '2.2.4.1', '2.2.4.1'])
    request_template['vpc_jetpack_version'] = get_value_completed(key_hint="request_template['vpc_jetpack_version']=",
                                                                  values=['4.6.5', '5.0.2', '5.1.2'])
    request_template['vpc_jetson_setup_ver'] = get_value_completed(key_hint="request_template['vpc_jetson_setup_ver']=",
                                                                   values=['', '2.0.1', '2.0.1'])
    request_template['vpc_side'] = get_value_completed(key_hint="request_template['vpc_side']=", values=['a', 'b'])
    request_template['vpc_aifw_packing_mode'] = get_value_completed(
        key_hint="request_template['vpc_aifw_packing_mode']=", values=['1: a2z 납품차량용 ', '0: a2z 내부테스트용'])
    request_template['vpc_flash_image_version'] = get_value_completed(
        key_hint="request_template['vpc_flash_image_version']=", values=['1.0.0', '1.3.0', '1.0.0'])
    if request_template['vpc_flash_image_version'] == '':
        request_template['vpc_with_flash_image'] = '0'  # 0 : flash image 없음
    else:
        request_template['vpc_with_flash_image'] = '1'  # 1 : flash image 있음
    request_template['vpc_identifier_number'] = get_value_completed(
        key_hint="request_template['vpc_identifier_number']=",
        values=['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                '17', '18', '19', '20'])
    request_template['vpc_identifier'] = f'{request_template['vpc_type']} #{request_template['vpc_identifier_number']}'

    vpc_data_raw.vpc_local_ssh_public_key = os.path.join(D_HOME, ".ssh", "id_ed25519.pub")
    vpc_data_raw.vpc_local_ssh_private_key = os.path.expanduser("~/.ssh/id_ed25519")
    # vpc_ip_ = get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_side_{vpc_data_raw.vpc_side}.toml', initial_str="")
    # vpc_data_raw.vpc_ip = get_ip_available_by_user_input()
    # if request_template['vpc_side'] == 'a':
    #     vpc_data_raw.vpc_ip = get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_a_side.toml', initial_str="")
    # elif request_template['vpc_side'] == 'b':
    #     vpc_data_raw.vpc_ip = get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ip_vpc_b_side.toml', initial_str="")
    # else:
    #     raise
    vpc_data_raw.vpc_ip = None
    vpc_data_raw.vpc_port = get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_ssh_port_vpc.toml', initial_str="")
    vpc_data_raw.vpc_user_n = get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_user_n_vpc.toml', initial_str="")
    vpc_data_raw.vpc_pw = get_pk_token(f_token=rf'{D_PKG_TOML}/pk_token_pw_vpc.toml', initial_str="")
    vpc_data_raw.vpc_purpose = request_template['vpc_purpose']
    vpc_data_raw.vpc_available_test_ip_set = ('192.168.2.114', '192.168.2.124', '192.168.10.114',
                                              vpc_data_raw.vpc_ip)  # ensure ip 할때, vpc_dev_available_ip_list 에서 연결 가능한 것을 우선순위를 두고 자동선택하도록, pickle 써보자.
    vpc_data_raw.vpc_side = request_template['vpc_side']
    vpc_data_raw.vpc_aifw_packing_mode = request_template['vpc_aifw_packing_mode']
    vpc_data_raw.vpc_with_flash_image = request_template['vpc_with_flash_image']
    vpc_data_raw.vpc_flash_image_version = request_template['vpc_flash_image_version']
    # vpc_data_raw.vpc_aifw_version = check_latest_aifw_version_and_get_version_seleted(vpc_data_raw.vpc_identifier, aifw_version=request_template['vpc_aifw_version'])
    vpc_data_raw.vpc_aifw_version = request_template['vpc_aifw_version']
    vpc_data_raw.vpc_type = request_template['vpc_type']
    vpc_data_raw.vpc_identifier_number = request_template['vpc_identifier_number']
    vpc_data_raw.vpc_jetpack_version = check_latest_jetpack_version_and_get_version_seleted(vpc_data_raw.vpc_identifier,
                                                                                            jetpack_version=
                                                                                            request_template[
                                                                                                'vpc_jetpack_version'])
    vpc_data_raw.vpc_wired_connection_reset = {'wired_connection_no': '(not defined)', "address": rf"",
                                               "method": "auto", "gateway": "", "dns": ""}
    vpc_data_raw.vpc_wired_connection_1_new = {'wired_connection_no': 1, "address": rf"{vpc_data_raw.vpc_ip}/24",
                                               "method": "manual", "gateway": "", "dns": ""}
    vpc_data_raw.vpc_wired_connection_3_new = {'wired_connection_no': 3, "address": rf"{vpc_data_raw.vpc_ip}/24",
                                               "method": "manual", "gateway": "", "dns": ""}
    vpc_data_raw.vpc_core_cnt = get_vpc_core_cnt_via_scp(vpc_data_raw)
    vpc_data_raw.vpc_proceser_name = get_vpc_processer_name_via_scp(vpc_data_raw)
    vpc_data_raw.vpc_nvidia_serial = get_vpc_nvidia_serial_via_scp(vpc_data_raw)
    # vpc_data_raw.vpc_type = get_vpc_type_conected_via_scp(vpc_data_raw)
    # vpc_data_raw.vpc_identifier = get_vpc_identifier_matched_from_vpc_db(vpc_data_raw.vpc_nvidia_serial, vpc_data_raw.vpc_side)
    vpc_data_raw.vpc_identifier = request_template['vpc_identifier']
    return vpc_data_raw
