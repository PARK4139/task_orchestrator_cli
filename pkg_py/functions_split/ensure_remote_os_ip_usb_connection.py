import undetected_chromedriver as uc
import tomllib
import toml
import tarfile
import string
import shlex
import random
import pyglet
import pandas as pd
import nest_asyncio
import hashlib
import functools
import datetime
from telegram import Bot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.get_list_calculated import get_list_calculated

from functools import partial as functools_partial
from functools import partial
from datetime import date
from pkg_py.functions_split.get_pnx_list import get_pnx_list

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def ensure_remote_os_ip_usb_connection(config_remote_os, remote_os_distro_n=None):
    # ensure_wsl_usb_ip_connection_attached() 의 차선책
    import re

    import time

    ensure_usbipd_installed(config_remote_os)

    cmd_to_os(cmd="wsl --shutdown", encoding=Encoding.UTF8)

    std_list = cmd_to_os(cmd="usbipd list", encoding=Encoding.UTF8)
    bus_id = None
    # signiture_list = ["APX", "Attached" or "Shared"]
    signiture_list = ["APX"]
    pattern = re.compile(r"\d+-\d")  # "2-3 패턴" # 2-12 는 안될듯 업데이트 필요
    for signiture_to_search in std_list:
        if all(signiture_ in signiture_to_search for signiture_ in signiture_list):
            match = pattern.search(signiture_to_search)
            if not match:
                pk_print(f'''{signiture_to_search} is not matched in command({cmd}) {'%%%FOO%%%' if LTA else ''}''',
                         print_color='red')
                pk_print(f'''리커버리 모드 진입을 재시도하세요.  {'%%%FOO%%%' if LTA else ''}"''', print_color='red')
                raise
            pk_print(str_working=rf'''match="{match}"  {'%%%FOO%%%' if LTA else ''}''')
            bus_id = match.group()
    if bus_id is None:
        pk_print(f'''"bus_id 가 None 입니다.  {'%%%FOO%%%' if LTA else ''} "''', print_color='red')
        raise
    pk_print(str_working=rf'''bus id found, bus_id={bus_id}  {'%%%FOO%%%' if LTA else ''}''', print_color="green")

    # signiture = "제공된 이름의 배포가 없습니다" or 'xxxx'
    std_list = cmd_to_os(cmd=rf"wsl -d {remote_os_distro_n} -- exit")
    if check_signiture_in_loop(time_limit=10, working_list=std_list, signiture="제공된 이름의 배포가 없습니다",
                               signiture_found_ment=rf"'{cmd}' 할수없었습니다"):
        raise

    cmd = "wsl -l -v"
    std_list = cmd_to_os(cmd=cmd, encoding='utf-16')
    import ipdb
    ipdb.set_trace()

    cmd = rf"usbipd unbind -b {bus_id}"
    cmd_to_os(cmd=cmd, encoding=Encoding.UTF8)

    cmd = rf"usbipd bind -b {bus_id}"
    cmd_to_os(cmd=cmd, encoding=Encoding.UTF8)

    # usbipd: warning: A firewall appears to be blocking the connection; ensure TCP port 3240 is allowed.
    # powershell as admin
    # New-NetFirewallRule -DisplayName "Allow USBIP Port 3240" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 3240

    # 위 내용에 대해서 원복
    # Remove-NetFirewallRule -DisplayName "Allow USBIP Port 3240"

    # cmd = rf"usbipd attach --wsl --busid {bus_id} --auto-attach"
    cmd = rf'start "" usbipd attach --wsl --busid {bus_id} --auto-attach'
    cmd_with_window_title = rf'title "{cmd}" && {cmd}'
    cmd_to_os_like_person(cmd=cmd_with_window_title)
    timeout = 15
    start_time = time.time()
    while 1:
        if is_window_opened(window_title_seg=cmd):
            pk_print(str_working=rf'''[ATTEMPTED] "wsl attach"  {'%%%FOO%%%' if LTA else ''}''')
            break
        if time.time() - start_time > timeout:
            return 0
        pk_sleep(seconds=0.2)

    cmd = rf"wsl lsusb"
    time_limit = 10
    time_s = time.time()
    signiture_list = "NVidia Corp."
    ment_positive = "wsl 에 attach 되었습니다"
    while 1:
        std_list = cmd_to_os(cmd=cmd, encoding=Encoding.CP949)
        for signiture_to_search in std_list:
            if signiture_list in signiture_to_search:
                pk_print(f'''{ment_positive}''', print_color="green")
                return 1
        if time.time() - time_s > time_limit:
            return 0
        pk_sleep(seconds=0.2)
