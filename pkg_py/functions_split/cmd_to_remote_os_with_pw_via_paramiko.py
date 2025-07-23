import threading
import speech_recognition as sr
import shlex
import pywintypes
import easyocr
from selenium.webdriver.common.keys import Keys
from pytube import Playlist
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from functools import partial
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def cmd_to_remote_os_with_pw_via_paramiko(ip, port, user_n, pw, cmd):
    # todo   config_remote_os 를 16 usages 에 적용할것.
    # todo : pw 가 보안적으로 필요한 경우는 이 함수를 쓰자

    import paramiko
    import traceback

    if LTA:
        pk_print(f"{STAMP_REMOTE_DEBUG} {STAMP_TRY_GUIDE} ssh -p {port} {user_n}@{ip} ")
    pk_print(f"{STAMP_REMOTE_DEBUG} cmd={cmd}")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # Connect to the server
        ssh.connect(hostname=ip, port=port, username=user_n, password=pw, timeout=10)
        # pk_print("{STAMP_DEBUG} SSH connection established")

        # Execute the cmd
        stdin, stdout_stream, stderr_stream = ssh.exec_command(cmd)
        std_out_str = stdout_stream.read().decode('utf-8').strip()
        std_err_str = stderr_stream.read().decode('utf-8').strip()

        # Debugging output
        std_out_list = get_list_from_str(item_str=std_out_str)
        std_err_list = get_list_from_str(item_str=std_err_str)
        if len(std_out_list) > 1:
            for index, item in enumerate(std_out_list):
                pk_print(f"{STAMP_REMOTE_DEBUG} {item}")
        if len(std_err_list) > 1:
            for index, item in enumerate(std_err_list):
                pk_print(f"{STAMP_REMOTE_ERROR} {item}")

        # Raise an error if there is output in stderr
        if std_err_str:
            pk_print(f"{STAMP_REMOTE_ERROR} {cmd} : {std_err_str}", print_color='red')

        std_out_str = std_out_str.strip()
        std_err_str = std_err_str.strip()
        return std_out_str, std_err_str
    except:
        pk_print(f"{STAMP_REMOTE_ERROR} {traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''} ", print_color='red')
        return std_out_str, traceback.format_exc()
    finally:
        ssh.close()
        if LTA:
            pk_print(rf"{STAMP_REMOTE_DEBUG} SSH connection closed.")
