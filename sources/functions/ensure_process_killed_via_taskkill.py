import winreg
import urllib.parse
import traceback
import timeit
import subprocess
import colorama
from yt_dlp import YoutubeDL
from selenium.common.exceptions import WebDriverException
from sources.functions.get_historical_list import get_historical_list

from sources.functions.is_window_title_front import is_window_title_front
from sources.functions.ensure_command_executed import ensure_command_executed

from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING

from functools import partial as functools_partial
from Cryptodome.Cipher import AES
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.objects.pk_etc import PK_UNDERLINE
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.is_d import is_d

from sources.objects.pk_local_test_activate import LTA
import logging


def ensure_process_killed_via_taskkill(process_name=None, pid=None, debug_mode=True):
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    if process_name is not None or pid is not None:
        logging.debug(rf"{func_n}() 동작 조건 충족")
    else:
        logging.debug(rf"{func_n}() 동작 조건 불충족")
        return

    cmd = None
    if process_name != None:
        cmd = f'taskkill /f /im {process_name}"'
    elif pid != None:
        cmd = f'taskkill /f /pid {pid}"'
    ensure_command_executed(cmd=cmd)
