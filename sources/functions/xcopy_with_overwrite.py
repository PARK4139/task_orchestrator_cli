import urllib
import toml
import requests
import random
import pygetwindow
import nest_asyncio
import colorama

from yt_dlp import YoutubeDL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.functions.ensure_console_cleared import ensure_console_cleared
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.encodings import Encoding

from PIL import Image
from enum import Enum
from Cryptodome.Cipher import AES
from sources.functions.is_f import is_f
from sources.functions.is_os_windows import is_os_windows

from sources.objects.pk_local_test_activate import LTA
import logging


def xcopy_with_overwrite(pnx, pnx_future):
    import inspect
    import subprocess
    import traceback

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    try:
        result = ensure_command_executed_like_human_as_admin(rf'echo a | xcopy "{pnx}" "{pnx_future}" /e /h /k /y')
        if result == subprocess.CalledProcessError:
            if is_f(pnx):
                ensure_command_executed_like_human_as_admin(rf'echo f | xcopy "{pnx}" "{pnx_future}" /e /h /k /y')
            else:
                ensure_command_executed_like_human_as_admin(rf'echo d | xcopy "{pnx}" "{pnx_future}" /e /h /k /y')
    except Exception:
        logging.debug(rf"traceback.format_exc()={traceback.format_exc()}")
