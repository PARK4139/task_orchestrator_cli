import pyautogui
from pynput import mouse
from sources.functions.ensure_window_to_front import ensure_window_to_front
from sources.functions.is_window_title_front import is_window_title_front

from sources.objects.task_orchestrator_cli_files import F_HISTORICAL_PNX
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from pathlib import Path
from os.path import dirname
from colorama import init as pk_colorama_init

from sources.functions.get_pnx_unix_style import get_pnx_unix_style


def get_random_pw(length_limit: int):
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length_limit))
