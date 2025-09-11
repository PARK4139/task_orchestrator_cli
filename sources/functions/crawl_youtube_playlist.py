import yt_dlp

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
from sources.functions.get_historical_list import get_historical_list
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.get_video_filtered_list import get_video_filtered_list
import logging

from sources.functions.set_pk_context_state import set_pk_context_state
from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from sources.objects.pk_state_via_database import PkSqlite3DB
from PIL import Image
from passlib.context import CryptContext
from os import path
from functools import partial
from datetime import timedelta
from datetime import datetime
from cryptography.hazmat.primitives import padding
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
from sources.functions.get_pnx_windows_style import get_pnx_windows_style
from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style


def crawl_youtube_playlist(url: str):
    import inspect
    import tqdm

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

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
        ensure_slept(seconds=0.0001)
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
