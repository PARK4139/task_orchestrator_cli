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
import logging

from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.encodings import Encoding
from sources.objects.pk_state_via_database import PkSqlite3DB
from datetime import timedelta
from datetime import datetime, timedelta
from base64 import b64encode
from sources.functions.get_list_calculated import get_list_calculated

from sources.functions.is_os_windows import is_os_windows
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA
from sources.functions.does_pnx_exist import is_pnx_existing


def download_aifw (target_device_data, remote_device_target_config):
    if target_device_data.target_device_type == 'no':
        # 도커 컨테이너 내부의 특정경로에서 git clone 해야함, 도커내부에 명령어를 수행해야함. ensure_command_to_remote_os 로 docker container 제어 가능한지 확인이 필요.
        cmd_to_docker_container(cmd='mkdir -p ~/Workspace/ai_framwork/build')
        # cd ~/Workspace
        # git clone http://192.168.1.39:8090/ai_framework -b {aifw_branch_n}?
    elif target_device_data.target_device_type == 'nx':
        cmd_to_docker_container(cmd='mkdir -p ~/works/')
        # cd ~/works/
        # # git clone http://192.168.1.39:8090/ai_dept/ai_framework
        # git clone http://211.171.108.170:8003/ai_dept/ai_framework
