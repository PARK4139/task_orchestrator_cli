import sys
import sqlite3
from selenium.webdriver.common.by import By
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.pk_system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pathlib import Path
from dirsync import sync
from base64 import b64decode
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def get_all_text_with_coordinates_via_easy_ocr(image):
    import inspect
    import easyocr
    func_n = inspect.currentframe().f_code.co_name
    # EasyOCR 객체 생성
    reader = easyocr.Reader(['en', 'ko'])  # 영어와 한글을 동시에 처리하려면 'en', 'ko' 지정
    results = reader.readtext(image)

    # 추출된 텍스트와 위치 반환
    text_with_coordinates = [(result[1], result[0]) for result in results]
    return text_with_coordinates
