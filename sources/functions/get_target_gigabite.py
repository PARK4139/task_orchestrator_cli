import sys
import socket
import pythoncom
import pygetwindow
import pyaudio
import importlib
from selenium.common.exceptions import WebDriverException
import logging
from sources.objects.pk_etc import PkFilter
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_database import PkSqlite3DB

from functools import partial
from bs4 import BeautifulSoup
from base64 import b64decode
from sources.functions.get_nx import get_nx


def get_target_gigabite(target_path):
    return get_target_bite(target_path.strip()) / 1024 ** 3
