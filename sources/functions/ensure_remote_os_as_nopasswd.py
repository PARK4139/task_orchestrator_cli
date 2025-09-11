import zlib
import zipfile
import webbrowser
import urllib.parse
import traceback
import tqdm
import toml
import toml
import re

import pythoncom
import pyglet
import os
import numpy as np
import nest_asyncio
import chardet
import calendar
from urllib.parse import quote
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.is_window_opened import is_window_opened
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_pressed import ensure_pressed
import logging


from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_files import F_FFMPEG_EXE
from sources.objects.pk_map_texts import PkTexts
from sources.objects.pk_state_via_database import PkSqlite3DB

from os.path import dirname
from mutagen.mp3 import MP3
from dirsync import sync
from datetime import datetime, time
from dataclasses import dataclass
from colorama import init as pk_colorama_init
from collections import Counter
from sources.objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_value_completed import ensure_value_completed
from pathlib import Path
from sources.functions.get_list_calculated import get_list_calculated
from sources.functions.is_d import is_d
from sources.functions.is_os_wsl_linux import is_os_wsl_linux
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.is_os_wsl_linux import is_os_wsl_linux

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs
from sources.functions.get_d_working import get_d_working


def ensure_remote_os_as_nopasswd(**remote_device_target_config):
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

    try:

        local_ssh_public_key = remote_device_target_config['local_ssh_public_key']
        local_ssh_private_key = remote_device_target_config['local_ssh_private_key']
        ip = remote_device_target_config['ip']
        port = remote_device_target_config['port']
        user_n = remote_device_target_config['user_n']
        pw = remote_device_target_config['pw']
        # public_key = remote_device_target_config['public_key']

        cmd = f"sudo grep -n '{user_n} ALL=(ALL:ALL) NOPASSWD:ALL' /etc/sudoers"
        std_outs, std_err_list = ensure_command_to_remote_os_with_pubkey(cmd=cmd, **remote_device_target_config)
        signiture = f"{user_n} ALL=(ALL:ALL) NOPASSWD:ALL"
        for std_out_str in std_outs:
            if signiture in std_out_str:
                logging.debug("THE ENTRY IS ALREADY PRESENT")
                return 1
            else:
                cmd = f"echo '{pw}' | sudo -S bash -c \"echo '{user_n} ALL=(ALL:ALL) NOPASSWD:ALL' >> /etc/sudoers\""
                std_outs, std_err_list = ensure_command_to_remote_os_with_pubkey(cmd=cmd, **remote_device_target_config)
                if not len(std_err_list) == 0:
                    for std_err_str in std_err_list:
                        logging.debug(rf'{"[ REMOTE ERROR ]"} {std_err_str}')
                if not len(std_outs) == 0:
                    for std_out_str in std_outs:
                        logging.debug(rf'{"[ REMOTE DEBUG ]"} {std_out_str}')
                cmd = f"sudo visudo -c"
                std_outs, std_err_list = ensure_command_to_remote_os_with_pubkey(cmd=cmd, **remote_device_target_config)
                if not len(std_err_list) == 0:
                    for std_err_str in std_err_list:
                        logging.debug(rf'{"[ REMOTE ERROR ]"} {std_err_str}')
                if not len(std_outs) == 0:
                    for std_out_str in std_outs:
                        logging.debug(rf'{"[ REMOTE DEBUG ]"} {std_out_str}')
    except:
        import traceback
        logging.debug(rf"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ")
