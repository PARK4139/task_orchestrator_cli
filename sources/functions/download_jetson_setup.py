import secrets
import numpy as np
import easyocr
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

from sources.functions.ensure_command_executed import ensure_command_executed

from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from cryptography.hazmat.backends import default_backend
from sources.functions.get_nx import get_nx


def download_jetson_setup():
    todo('%%%FOO%%%')
