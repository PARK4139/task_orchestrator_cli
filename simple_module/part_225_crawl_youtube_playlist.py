import yt_dlp
# import win32gui
import webbrowser
import tomllib
import tarfile
import sqlite3
import shutil
import pythoncom
import pygetwindow
import psutil
import math
import datetime
from yt_dlp import YoutubeDL
from urllib.parse import urlparse
from urllib.parse import quote
from seleniumbase import Driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_layer_files import F_LOSSLESSCUT_EXE
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from PIL import Image
from passlib.context import CryptContext
from os import path
from functools import partial
from datetime import timedelta
from datetime import datetime
from cryptography.hazmat.primitives import padding
from pkg_py.pk_system_layer_directories import D_PKG_PY
from pkg_py.simple_module.part_014_get_pnx_windows_style import get_pnx_windows_style
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def crawl_youtube_playlist(url: str):
    import inspect
    import tqdm

    func_n = inspect.currentframe().f_code.co_name

    # url 전처리
    url = url.strip()

    # driver 설정
    total_percent = 100
    driver = get_driver_selenium(browser_debug_mode=False)
    with tqdm(total=total_percent, ncols=79, desc="driver 설정 진행률") as process_bar:
        global title
        title = 'html  href 크롤링 결과'
        target_url = url
        driver.get(target_url)
        page_src = driver.page_source
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page_src, "lxml")
        pk_sleep(seconds=0.0001)
        process_bar.update(total_percent)
    driver.close()

    names = soup.find_all("a", id="video-title")
    hrefs = soup.find_all("a", id="video-title")
    # hrefs=copy.deepcopy(names)

    # list 에 저장
    name_list = []
    href_list = []
    # view_list=[]
    for i in range(len(names)):
        name_list.append(names[i].text.strip())
        # view_list.append(view[i].get('aria-label').split()[-1])
    for i in hrefs:
        href_list.append('{}{}'.format('https://www.youtube.com', i.get('href')))

    # str 에 저장
    result_list = []
    for index, url in enumerate(href_list):
        # results_list.append(f"{name_list[index]}   {hrefs_list[index]}")
        result_list.append(f"{href_list[index]}")  # href 만 출력
    results_str = "\n".join(result_list)

    # fail
    # dialog=GuiUtil.CustomQdialog(title=f"크롤링결과보고", ment=f"{results}", btns=[YES], auto_click_positive_btn_after_seconds="")
    # dialog.exec()

    # fail
    # GuiUtil.pop_up_as_complete(title="크롤링결과보고", ment=f"{results}")

    # success
    # debug_as_gui(f"{results}") # 테스트용 팝업    GuiUtil 로 옮기는 게 나을 지 고민 중이다.

    # success
    # 비동기로 진행 가능
    global dialog
    dialog = GuiUtil.CustomQdialog(title=f"크롤링결과보고", prompt=f"({len(href_list)}개 playlist 추출됨)\n\n{results_str}")
    dialog.show()
