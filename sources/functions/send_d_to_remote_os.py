
import threading
import pandas as pd
import os.path
import keyboard
import inspect
import colorama
from selenium.webdriver.common.action_chains import ActionChains
from prompt_toolkit import PromptSession
from sources.functions.ensure_iterable_log_as_vertical import ensure_iterable_log_as_vertical
from sources.functions.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.set_pk_context_state import set_pk_context_state

from PIL import Image
from passlib.context import CryptContext
from os import path
from enum import Enum
from dataclasses import dataclass
from Cryptodome.Cipher import AES
from collections import Counter
from pathlib import Path

from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging


def send_d_to_remote_os(d_local_src, d_remote_dst, **remote_device_target_config):
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


    import shutil

    import os
    import paramiko

    ip = remote_device_target_config['ip']
    pw = remote_device_target_config['pw']
    port = remote_device_target_config['port']
    user_n = remote_device_target_config['user_n']
    local_ssh_public_key = remote_device_target_config['local_ssh_public_key']

    ssh = None
    sftp = None
    f_zip_local = None
    try:
        # compress from d_local to f_zip_local
        f_zip_nx = os.path.basename(d_local_src) + ".zip"
        f_zip_local = os.path.join(os.path.dirname(d_local_src), f_zip_nx)
        f_zip_local = Path(f_zip_local)
        shutil.make_archive(base_name=f_zip_local.replace(".zip", ""), format="zip", root_dir=d_local_src)
        if is_pnx_existing(f_zip_local):
            logging.debug(f"compress d from d_local to f_zip_local({f_zip_local})")

        f_zip_remote = os.path.join(d_remote_dst, f_zip_nx).replace("\\", "/")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=user_n, password=pw)
        sftp = ssh.open_sftp()

        # send d as f_zip
        logging.debug(f"start to send d as f_zip from {f_zip_local} to {f_zip_remote}")
        sftp.put(f_zip_local, f_zip_remote)
        logging.debug(f"send d as f_zip from {f_zip_local} to {f_zip_remote}")

        # decompress in remote
        cmd = f"unzip -o {f_zip_remote} -d {d_remote_dst}"
        stdin, stdout, stderr = ssh.exec_command(cmd)  # 이 방식.

        # ensure d existance
        # todo

    except Exception as e:
        print(f"Error during directory transfer: {e}")
        raise
    finally:
        if sftp:
            sftp.close()
        if ssh:
            ssh.close()
        # 잔여 pnx 삭제
        if os.path.exists(f_zip_local):
            os.remove(f_zip_local)
        if LTA:
            logging.debug("SSH connection closed.")
