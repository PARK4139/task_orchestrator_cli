import win32con
import win32com.client
import tomllib
import tomllib
import sqlite3
import mysql.connector
import ipdb
import asyncio
from webdriver_manager.chrome import ChromeDriverManager
from telegram import Bot
from selenium.webdriver.support.ui import WebDriverWait
from prompt_toolkit import PromptSession
from pkg_py.functions_split.pk_print_state import pk_print_state

from pkg_py.pk_system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
from datetime import timedelta
from datetime import datetime, timedelta
from base64 import b64encode
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.pk_system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def download_aifw(vpc_data, config_remote_os):
    if vpc_data.vpc_type == 'no':
        # 도커 컨테이너 내부의 특정경로에서 git clone 해야함, 도커내부에 명령어를 수행해야함. cmd_to_remote_os 로 docker container 제어 가능한지 확인이 필요.
        cmd_to_docker_container(cmd='mkdir -p ~/Workspace/ai_framwork/build')
        # cd ~/Workspace
        # git clone http://192.168.1.39:8090/ai_framework -b {aifw_branch_n}?
    elif vpc_data.vpc_type == 'nx':
        cmd_to_docker_container(cmd='mkdir -p ~/works/')
        # cd ~/works/
        # # git clone http://192.168.1.39:8090/ai_dept/ai_framework
        # git clone http://211.171.108.170:8003/ai_dept/ai_framework
