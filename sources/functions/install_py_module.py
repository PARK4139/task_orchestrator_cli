
import win32con
import toml
import threading
import socket
import shutil
import shlex
import math
import clipboard
from seleniumbase import Driver

from sources.functions.ensure_window_to_front import ensure_window_to_front

from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.get_list_sorted import get_list_sorted
from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_context import SpeedControlContext
from sources.objects.pk_local_test_activate import LTA
from os.path import dirname
from cryptography.hazmat.primitives import padding
from bs4 import ResultSet
from base64 import b64encode
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.get_pnx_unix_style import get_pnx_unix_style
from sources.functions.does_pnx_exist import is_pnx_existing


def install_py_module(module_name):
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
