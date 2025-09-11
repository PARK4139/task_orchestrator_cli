import sys
import sqlite3
from selenium.webdriver.common.by import By
from prompt_toolkit import PromptSession
from sources.functions.get_historical_list import get_historical_list
from sources.functions.is_window_opened_via_window_title import is_window_opened_via_window_title
from sources.functions.ensure_console_cleared import ensure_console_cleared

from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
from sources.objects.pk_state_via_context import SpeedControlContext
from pathlib import Path
from dirsync import sync
from base64 import b64decode
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from sources.objects.pk_local_test_activate import LTA
import logging


def get_all_text_with_coordinates_via_easy_ocr(image):
    import inspect
    import easyocr
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    # EasyOCR 객체 생성
    reader = easyocr.Reader(['en', 'ko'])  # 영어와 한글을 동시에 처리하려면 'en', 'ko' 지정
    results = reader.readtext(image)

    # 추출된 텍스트와 위치 반환
    text_with_coordinates = [(result[1], result[0]) for result in results]
    return text_with_coordinates
