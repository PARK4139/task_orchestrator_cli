
import threading
import pandas as pd
import os.path
import keyboard
import inspect
import colorama
from selenium.webdriver.common.action_chains import ActionChains
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed_once import ensure_printed_once
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
# pk_#
from PIL import Image
from passlib.context import CryptContext
from os import path
from enum import Enum
from dataclasses import dataclass
from Cryptodome.Cipher import AES
from collections import Counter
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def send_d_to_remote_os(d_local_src, d_remote_dst, **config_remote_os):
    import shutil

    import os
    import paramiko

    ip = config_remote_os['ip']
    pw = config_remote_os['pw']
    port = config_remote_os['port']
    user_n = config_remote_os['user_n']
    local_ssh_public_key = config_remote_os['local_ssh_public_key']

    ssh = None
    sftp = None
    f_zip_local = None
    try:
        # compress from d_local to f_zip_local
        f_zip_nx = os.path.basename(d_local_src) + ".zip"
        f_zip_local = os.path.join(os.path.dirname(d_local_src), f_zip_nx)
        f_zip_local = get_pnx_os_style(pnx=f_zip_local)
        shutil.make_archive(base_name=f_zip_local.replace(".zip", ""), format="zip", root_dir=d_local_src)
        if does_pnx_exist(f_zip_local):
            ensure_printed(f"compress d from d_local to f_zip_local({f_zip_local})")

        f_zip_remote = os.path.join(d_remote_dst, f_zip_nx).replace("\\", "/")

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=user_n, password=pw)
        sftp = ssh.open_sftp()

        # send d as f_zip
        ensure_printed(f"start to send d as f_zip from {f_zip_local} to {f_zip_remote}")
        sftp.put(f_zip_local, f_zip_remote)
        ensure_printed(f"send d as f_zip from {f_zip_local} to {f_zip_remote}", print_color="green")

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
            ensure_printed("SSH connection closed.")
