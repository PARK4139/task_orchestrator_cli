import zlib
import yt_dlp
import winreg


import urllib
import undetected_chromedriver as uc
import tqdm
import tarfile
import subprocess
import string
import socket
import shutil
import shlex
import secrets
import pywintypes

import pyglet
import pygetwindow
import pickle
import paramiko
import os
import keyboard
import json
import ipdb
import hashlib
import easyocr
import datetime
from yt_dlp import YoutubeDL
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import quote, urlparse
from urllib.parse import quote
from typing import TypeVar, List
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from prompt_toolkit import PromptSession
# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.rerun_losslesscut import rerun_losslesscut
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.print_state import print_state
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.stamps import STAMP_ATTEMPTED
from pkg_py.system_object.files import F_LOSSLESSCUT_EXE
from pkg_py.system_object.files import F_HISTORICAL_PNX
from pkg_py.system_object.encodings import Encoding
from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.get_list_calculated import get_list_calculated
from functools import lru_cache
from fastapi import HTTPException
from datetime import datetime
from datetime import date
from cryptography.hazmat.backends import default_backend
from base64 import b64encode
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.system_object.etc import PK_UNDERLINE
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def get_comprehensive_weather_information_from_web():
    import inspect
    import re
    import threading
    import traceback

    if not is_internet_connected():
        raise
    browser_debug_mode = False
    try:
        while 1:
            title = ""
            ment_about_naver_weather = ''
            results_about_naver_weather = ''
            results_about_nationwide_ultrafine_dust = ''
            ment_about_geo = ''
            results_about_geo = ''
            ment_about_pm_ranking = ''
            results_about_pm_ranking = ''

            async def crawl_pm_ranking():
                func_n = inspect.currentframe().f_code.co_name
                driver = None
                try:
                    driver = get_driver_selenium(browser_debug_mode=browser_debug_mode)
                    ment = '미세먼지랭킹 웹사이트 크롤링 결과'
                    global ment_about_pm_ranking
                    ment_about_pm_ranking = ment
                    target_url = f'https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103'
                    ensure_printed(rf'''target_url="{target_url}"  {'%%%FOO%%%' if LTA else ''}''')
                    driver.get(target_url)
                    page_src = driver.page_source
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(page_src, "lxml")
                    results = soup.find_all("table", class_="datatable")  # <table class="datatable">foo!</div>
                    soup = BeautifulSoup(str(results), "lxml")
                    results = soup.find_all("table")[-1]
                    soup = BeautifulSoup(str(results), "lxml")
                    results = soup.find_all("table")[-1].text
                    results = results.split("\n")  # 리스트
                    results = [x for x in results if x.strip()]
                    results = [x for x in results if x.strip(",")]
                    head_1 = results[1]
                    head_2 = results[2]
                    pattern = r'(\d{2}-\d{2}-\d{2} \d{2}:\d{2})([가-힣]+\(\d+\))([가-힣]+\(\d+\))'  # 정규식을 () 로 부분 부분 묶으면 tuple 형태로 수집할 수 있다.
                    body = re.findall(pattern, results[3])
                    body = list(body)  # tuple to list
                    body = [list(item) for item in body]  # LIST 내 ITEM 이 TUPLE 일 때 ITEM 을 LIST 로 변환 #의도대로 잘 변했으~

                    # 리스트 요소를 3개 단위로 개행하여 str 에 저장
                    body_ = ""
                    for i in range(0, len(body), 1):
                        body_ = body_ + body[i][0] + body[i][1] + body[i][2] + "\n"
                    body = body_
                    # body="\n".join(body) # list to str
                    results = f"{head_1}\t{head_2}\n{body}"

                    global results_about_pm_ranking
                    results_about_pm_ranking = results
                    ensure_printed(
                        str_working=rf'''results_about_pm_ranking="{results_about_pm_ranking}"  {'%%%FOO%%%' if LTA else ''}''')
                except:
                    ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
                    # driver.close()
                    driver.quit()

            async def crawl_nationwide_ultrafine_dust():
                func_n = inspect.currentframe().f_code.co_name
                driver = get_driver_selenium(browser_debug_mode=browser_debug_mode)

                # # '전국초미세먼지'(bs4 way)
                ment = '전국초미세먼지  크롤링 결과'
                global title
                title = ment
                target_url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=전국초미세먼지'
                ensure_printed(target_url, print_color='blue')
                driver.get(target_url)
                page_src = driver.page_source
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(page_src, "lxml")
                results: any
                # results=soup.find_all("body")
                from bs4 import ResultSet
                results: ResultSet = soup.find_all("div", class_="detail_box")
                results: str = results[0].text
                results: str = results.replace("지역별 초미세먼지 정보", "")
                results: str = results.replace("관측지점 현재 오전예보 오후예보", "")
                results: str = results.replace("", "")
                results___: [str] = results.split(" ")
                results___: [str] = [x for x in results___ if
                                     x.strip(" ") and x.strip("") and x.strip("\"") and x.strip("\'") and x.strip(
                                         "\'\'")]  # 불필요 리스트 요소 remove ( "" , "\"", " " ...)

                # 리스트 요소를 4개 단위로 개행하여 str 에 저장
                results_: str = ""
                for i in range(0, len(results___), 4):
                    if i == len(results___):
                        pass
                    results_ = f"{results_}\t{results___[i]}\t{results___[i + 1]}\t{results___[i + 2]}\t{results___[i + 3]}\n"
                results___ = results_
                global results_about_nationwide_ultrafine_dust
                results_about_nationwide_ultrafine_dust = results___
                ensure_printed(
                    str_working=rf'''results_about_nationwide_ultrafine_dust="{results_about_nationwide_ultrafine_dust}"  {'%%%FOO%%%' if LTA else ''}''')

            async def crawl_naver_weather():
                func_n = inspect.currentframe().f_code.co_name
                driver = get_driver_selenium(browser_debug_mode=browser_debug_mode)
                # '동안구 관양동 날씨 정보'(bs4 way)
                ment = '네이버 동안구 관양동 날씨 크롤링 결과'

                global ment_about_naver_weather
                ment_about_naver_weather = ment
                target_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=동안구+관양동+날씨'
                ensure_printed(target_url, print_color='blue')
                driver.get(target_url)
                page_src = driver.page_source
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(page_src, "lxml")
                from bs4 import ResultSet
                results: ResultSet = soup.find_all("div", class_="status_wrap")
                results: str = results[0].text
                # 리스트 요소 변경
                results: str = results.replace("오늘의 날씨", "오늘의날씨")
                results: str = results.replace(" 낮아요", "낮아요")
                results: str = results.replace(" 높아요", "높아요")
                results: str = results.replace(" 체감", "체감온도")
                results_refactored = results.split(" ")
                results_refactored: [str] = [x for x in results_refactored if
                                             x.strip(" ") and x.strip("") and x.strip("\"") and x.strip(
                                                 "\'") and x.strip("\'\'")]  # 불필요 리스트 요소 remove ( "" , "\"", " " ...)
                results_refactored: [str] = [x for x in results_refactored if x.strip("현재")]  # 리스트 요소 "오늘의"
                # 리스트 내 특정문자와 동일한 요소의 바로 뒷 요소를 가져와 딕셔너리에 저장 # 데이터의 key, value 형태가 존재하면서 순번이 key 다음 value 형태로 잘 나오는 경우 사용.
                keys_predicted = ['온도', '체감온도', '습도', '서풍', '동풍', '남풍', '북풍', '북서풍', '미세먼지', '초미세먼지', '자외선', '일출',
                                  '오늘의날씨']
                results_: dict = {}
                for i in range(len(results_refactored) - 1):
                    for key_predicted in keys_predicted:
                        if results_refactored[i] == key_predicted:
                            key = results_refactored[i]
                            value = results_refactored[i + 1]
                            results_[key] = value
                results_refactored = results_

                # results: [str]=str(results_)  # dict to str (개행을 시키지 않은)

                results: str = "\n".join(
                    [f"{key}: {value}" for key, value in results_refactored.items()])  # dict to str (개행을 시킨)

                global results_about_naver_weather
                results_about_naver_weather = results
                ensure_printed(
                    str_working=rf'''results_about_naver_weather="{results_about_naver_weather}"  {'%%%FOO%%%' if LTA else ''}''')

            async def crawl_geo_info():
                func_n = inspect.currentframe().f_code.co_name
                # '지역 정보'(bs4 way)
                driver = get_driver_selenium(browser_debug_mode=browser_debug_mode)
                ment = '지역정보 크롤링 결과'
                global ment_about_geo
                ment_about_geo = ment
                # target_url='https://map.naver.com/p'
                target_url = 'https://www.google.com/search?q=현재위치'
                ensure_printed(target_url, print_color='blue')
                driver.get(target_url)
                page_src = driver.page_source
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(page_src, "lxml")
                results: any
                # results=soup.find_all("body")
                from bs4 import ResultSet
                results: ResultSet = soup.find_all("span", class_="BBwThe")  # 지역정보 한글주소
                # results: ResultSet=soup.find_all("span", class_="fMYBhe") # 지역정보 영어주소
                results: str = results[0].text

                global results_about_geo
                results_about_geo = results
                ensure_printed(str_working=rf'''results_about_geo="{results_about_geo}"  {'%%%FOO%%%' if LTA else ''}''')

            def run_async_loop1():
                import asyncio
                func_n = inspect.currentframe().f_code.co_name
                try:
                    func_n = inspect.currentframe().f_code.co_name
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(crawl_pm_ranking())
                except:
                    ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

            def run_async_loop2():
                import asyncio
                func_n = inspect.currentframe().f_code.co_name
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(crawl_nationwide_ultrafine_dust())

            def run_async_loop3():
                import asyncio
                func_n = inspect.currentframe().f_code.co_name
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(crawl_naver_weather())

            def run_async_loop4():
                import asyncio
                func_n = inspect.currentframe().f_code.co_name
                # ensure_printed(f"def {inspect.currentframe().f_code.co_name}() is running...")
                func_n = inspect.currentframe().f_code.co_name
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                loop.run_until_complete(crawl_geo_info())

            thread1 = threading.Thread(target=run_async_loop1)
            thread1.start()

            thread2 = threading.Thread(target=run_async_loop2)
            thread2.start()

            thread3 = threading.Thread(target=run_async_loop3)
            thread3.start()

            thread4 = threading.Thread(target=run_async_loop4)
            thread4.start()

            # 모든 쓰레드 끝날때 까지 대기
            thread1.join()
            thread2.join()
            thread3.join()
            thread4.join()

            pk_speak_v2(str_working='날씨에 대한 웹크롤링 및 데이터 분석이 성공되었습니다', comma_delay=0.98)
            # 함수가 break 로 끝이 나면 창들이 창을 닫아야 dialog 들이 사라지도록 dialog 를 global 처리를 해두었음.
            global dialog4
            global dialog3
            global dialog2
            global dialog1
            dialog3 = GuiUtil.CustomQdialog(title=f"{ment_about_naver_weather}",
                                            prompt=f"{results_about_naver_weather}")
            dialog2 = GuiUtil.CustomQdialog(title=f"{title}", prompt=f"{results_about_nationwide_ultrafine_dust}")
            dialog1 = GuiUtil.CustomQdialog(title=f"{ment_about_geo}", prompt=f"{results_about_geo}")
            dialog4 = GuiUtil.CustomQdialog(title=f"{ment_about_pm_ranking}", prompt=f"{results_about_pm_ranking}")
            dialog1.show()
            dialog2.show()
            dialog3.show()
            dialog4.show()
            break
    except:
        ensure_printed(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
