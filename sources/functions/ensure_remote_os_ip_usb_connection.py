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



from functions.check_signiture_in_loop import check_signiture_in_loop
from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_database import PkSqlite3DB


from functools import partial as functools_partial
from functools import partial
from datetime import date
from sources.functions.get_pnxs import get_pnxs

from sources.objects.pk_local_test_activate import LTA
import logging


def ensure_remote_os_ip_usb_connection(remote_device_target_config, distro_name=None):
    import inspect
    from functions.ensure_value_completed_advanced import ensure_value_completed_advanced

    import logging

    from functions import ensure_pnx_made
    from functions.ensure_command_to_remote_os import ensure_command_to_target
    from functions.get_wsl_distro_port import get_wsl_distro_port
    from functions.ensure_dockerfile_writen import ensure_dockerfile_writen
    from functions.ensure_remote_os_as_nopasswd import ensure_remote_os_as_nopasswd
    from functions.ensure_ssh_public_key_to_remote_os import ensure_ssh_public_key_to_remote_os
    from functions.ensure_wsl_distro_enabled import ensure_wsl_distro_enabled
    from functions.ensure_wsl_distro_session import ensure_wsl_distro_session
    from functions.get_n import get_n
    from functions.get_wsl_distro_names_installed import get_wsl_distro_names_installed
    from functions.get_wsl_ip import get_wsl_ip
    from functions.get_wsl_pw import get_wsl_pw
    from functions.get_wsl_user_n import get_wsl_user_n
    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_FASTAPI, D_TASK_ORCHESTRATOR_CLI, D_USERPROFILE
    from sources.functions.get_nx import get_nx
    from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
    from sources.objects.pk_local_test_activate import LTA

    import os

    # ensure_wsl_usb_ip_connection_attached() 의 차선책
    import re

    import time

    ensure_usbipd_enabled(remote_device_target_config)

    ensure_command_executed(cmd="wsl --shutdown", encoding=Encoding.UTF8)

    std_list = ensure_command_executed(cmd="usbipd list", encoding=Encoding.UTF8)
    bus_id = None
    # signiture_list = ["APX", "Attached" or "Shared"]
    signiture_list = ["APX"]
    pattern = re.compile(r"\d+-\d")  # "2-3 패턴" # 2-12 는 안될듯 업데이트 필요
    for signiture_to_search in std_list:
        if all(signiture_ in signiture_to_search for signiture_ in signiture_list):
            match = pattern.search(signiture_to_search)
            if not match:
                logging.debug(f'''{signiture_to_search} is not matched in command({cmd}) {'%%%FOO%%%' if LTA else ''}''',
                         print_color='yellow')
                logging.debug(f'''리커버리 모드 진입을 재시도하세요.  {'%%%FOO%%%' if LTA else ''}"''')
                raise
            logging.debug(rf'''match="{match}"  {'%%%FOO%%%' if LTA else ''}''')
            bus_id = match.group()
    if bus_id is None:
        logging.debug(f'''"bus_id 가 None 입니다.  {'%%%FOO%%%' if LTA else ''} "''')
        raise
    logging.debug(rf'''bus id found, bus_id={bus_id}  {'%%%FOO%%%' if LTA else ''}''')

    # signiture = "제공된 이름의 배포가 없습니다" or 'xxxx'
    std_list = ensure_command_executed(cmd=rf"wsl -d {distro_name} -- exit")
    if check_signiture_in_loop(time_limit=10, working_list=std_list, signiture="제공된 이름의 배포가 없습니다",
                               signiture_found_ment=rf"'{cmd}' 할수없었습니다"):
        raise

    cmd = "wsl -l -v"
    std_list = ensure_command_executed(cmd=cmd, encoding='cp949')
    import ipdb
    ipdb.set_trace()

    cmd = rf"usbipd unbind -b {bus_id}"
    ensure_command_executed(cmd=cmd, encoding=Encoding.UTF8)

    cmd = rf"usbipd bind -b {bus_id}"
    ensure_command_executed(cmd=cmd, encoding=Encoding.UTF8)

    # usbipd: warning: A firewall appears to be blocking the connection; ensure TCP port 3240 is allowed.
    # powershell as admin
    # New-NetFirewallRule -DisplayName "Allow USBIP Port 3240" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 3240

    # 위 내용에 대해서 원복
    # Remove-NetFirewallRule -DisplayName "Allow USBIP Port 3240"

    # cmd = rf"usbipd attach --wsl --busid {bus_id} --auto-attach"
    cmd = rf'start "" usbipd attach --wsl --busid {bus_id} --auto-attach'
    cmd_with_window_title = rf'title "{cmd}" && {cmd}'
    ensure_command_executed_like_human(cmd=cmd_with_window_title)
    timeout = 15
    start_time = time.time()
    while 1:
        if is_window_opened(window_title_seg=cmd):
            logging.debug(rf'''[ATTEMPTED] "wsl attach"  {'%%%FOO%%%' if LTA else ''}''')
            break
        if time.time() - start_time > timeout:
            return 0
        ensure_slept(seconds=0.2)

    cmd = rf"wsl lsusb"
    time_limit = 10
    time_s = time.time()
    signiture_list = "NVidia Corp."
    ment_positive = "wsl 에 attach 되었습니다"
    while 1:
        std_list = ensure_command_executed(cmd=cmd, encoding=Encoding.CP949)
        for signiture_to_search in std_list:
            if signiture_list in signiture_to_search:
                logging.debug(f'''{ment_positive}''')
                return 1
        if time.time() - time_s > time_limit:
            return 0
        ensure_slept(seconds=0.2)
