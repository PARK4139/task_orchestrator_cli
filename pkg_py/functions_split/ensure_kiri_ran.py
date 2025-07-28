import urllib
import toml
import toml
import sys
import sqlite3
import speech_recognition as sr
import socket


import platform
import os.path
import mysql.connector
import ipdb
import functools
import datetime
import cv2
import clipboard
import chardet
from zipfile import BadZipFile
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.get_historical_list import get_historical_list
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.system_object.directories_reuseable import D_PROJECT

from passlib.context import CryptContext
from os.path import dirname
from os import path
from moviepy import VideoFileClip
from fastapi import HTTPException
from datetime import timedelta
from datetime import date
from cryptography.hazmat.backends import default_backend
from Cryptodome.Random import get_random_bytes
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut
from pkg_py.system_object.directories import D_PK_WORKING, D_PKG_PKL, D_PKG_PY
from pkg_py.system_object.directories import D_PKG_PY
# from pkg_py.system_object.is_os_windows import is_os_windows


from pkg_py.functions_split.get_pnx_windows_style import get_pnx_windows_style
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.system_object.local_test_activate import LTA

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_kiri_ran():
    import random
    import traceback
    import speech_recognition as sr

    from colorama import init as pk_colorama_init
    import os
    ensure_colorama_initialized_once()

    # ensure wsl
    config_remote_os = {}
    wsl_distro_n = "Ubuntu-24.04"
    config_remote_os['os_distro_n'] = wsl_distro_n
    config_remote_os['ip'] = get_wsl_ip(wsl_distro_n)
    config_remote_os['port'] = ensure_and_get_wsl_port(wsl_distro_n)
    config_remote_os['user_n'] = get_wsl_user_n(wsl_distro_n)
    config_remote_os['pw'] = get_wsl_pw(wsl_distro_n)
    config_remote_os['local_ssh_public_key'] = os.path.join(D_HOME, ".ssh", "id_ed25519.pub")
    config_remote_os['local_ssh_private_key'] = os.path.expanduser("~/.ssh/id_ed25519")
    ensure_wsl_distro_enabled(wsl_distro_n=wsl_distro_n)
    ensure_wsl_distro_session(wsl_distro_n=wsl_distro_n)

    ensure_python_pkg_to_remote_os(py_pkg_n='SpeechRecognition', **config_remote_os)
    ensure_python_pkg_to_remote_os(py_pkg_n='PyAudio', **config_remote_os)

    # ensure_general_ubuntu_pkg()
    # mpg123 을 wsl 에 install 해서 써볼까? mpg123은 제어가 쉬울지도
    # ensure_ubuntu_pkg_to_remote_os(ubuntu_pkg_n='mpg123', ** config_remote_os)

    if not is_os_windows():
        cmd = 'sudo apt install mpg123'
        ensure_command_excuted_to_os(cmd=cmd)

    if is_internet_connected():
        # recognizer=sr.Recognizer()
        # with sr.Microphone() as source:
        #     ensure_printed(str_working="음성을 말하세요...")
        #     recognizer.adjust_for_ambient_noise(source)
        #     audio=recognizer.listen(source)
        pass
    else:
        # # CMU Sphinx로 음성 인식 (오프라인 사용 가능)
        # try:
        #     speak("음성을 인식 중...")
        #     text=recognizer.recognize_sphinx(audio)
        #     speak("인식된 텍스트: " + text)
        # except sr.UnknownValueError:
        #     speak("음성을 이해할 수 없습니다.")
        # except sr.RequestError as e:
        #     speak(f"음성 인식 서비스에 오류가 발생했습니다: {e}")
        pass

    # speak_like_parrot("테스트입니다")

    # os.system(rf"mpg123 ./{temp_mp3}")  # Linux 재생 명령
    # os.system(rf"start {temp_mp3}")  # Windows용 재생 명령

    recognizer = None
    if is_mic_device_connected():
        ensure_printed(f'''mic is connected. {'%%%FOO%%%' if LTA else ''}''')
        recognizer = sr.Recognizer()
    else:
        ensure_printed(f'''mic is disconnected. {'%%%FOO%%%' if LTA else ''}''', print_color='red')

    loop_cnt = 0
    while 1:
        if loop_cnt == 0:
            ice_breaking_ments = [
                "hello! i am mini, i am ready to assist",
                "Hello! How can I assist you today?",
                "",
            ]
            ice_breaking_ment = get_element_random(working_list=ice_breaking_ments)
            ensure_printed_and_speak(ice_breaking_ment)
        if loop_cnt % 11 == 0:
            ice_breaking_ments = [
                "please. give a command.",
                "i am boring. give a command."
                "i am boring. give a something."
                # get_str_today_day_info(),
            ]
            ice_breaking_ment = get_element_random(working_list=ice_breaking_ments)
            ensure_printed_and_speak(ice_breaking_ment)

        try:
            if str_working is None:
                with sr.Microphone() as source:
                    # recognizer.adjust_for_ambient_noise(source, duration=1.0)  # 주변 소음 보정 # adjust_for_ambient_noise no attribution
                    while 1:
                        try:
                            ensure_printed("지금 말씀하실것을 추천드립니다.", print_color='blue')
                            # audio = recognizer.listen(source, phrase_time_limit=10)  # 음성 듣기
                            str_working = recognizer.recognize_google(audio, language="ko")  # Google STT
                            break
                        except sr.UnknownValueError:
                            ensure_printed(f"UnknownValueError {str_working}")
                        except sr.RequestError as e:
                            ensure_printed(f"Google Speech Recognition service access", print_color='red')
            str_working = str_working.replace(' ', '')
            ensure_printed(rf"{str_working}", print_color='blue')
            if any(keyword in str_working for keyword in ["ipdb"]):
                import ipdb
                ipdb.set_trace()
            elif any(keyword in str_working for keyword in ["테스트", "test"]):
                pk_count_down()
            elif any(keyword in str_working for keyword in ["휴지통비워", "휴지통정리", "empty_trash_bin"]):
                empty_recycle_bin()
                ensure_printed_and_speak("I have emptied the trash bin")
            elif any(keyword in str_working for keyword in ["플레인", "플래인"]):
                ensure_printed_and_speak("yes. i am here")
            elif any(keyword in str_working for keyword in ["영어공부"]):
                ensure_printed_and_speak("What is the weather like?")
                ensure_slept(seconds=random.randint(a=200, b=500))
                ensure_printed_and_speak(
                    "I can't directly access weather information, but if you share your location, I can guide you!")
                ensure_slept(seconds=random.randint(a=200, b=500))
                ensure_printed_and_speak("Quit")
                ensure_slept(seconds=random.randint(a=200, b=500))
                ensure_printed_and_speak("Ending the conversation. Goodbye!")
            elif any(keyword in str_working for keyword in ["업무_d_생성", '업무_d_']):
                make_d_with_timestamp(d_nx=rf"생산관리", dst=rf"{D_PK_WORKING}")
                ensure_directory_made_for_work()
            elif any(keyword in str_working for keyword in ["sound interactive mode"]):
                # ensure_todo_list_guided(days=1)  # todo : add : 등록된 스케쥴시간확인
                ensure_printed(str_working="Please give a cmd", print_color='blue')
                # print_and_speak("시키실 일 없으신가요.", after_delay=1.0) #random
                with sr.Microphone() as source:
                    # recognizer.adjust_for_ambient_noise(source)
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    # audio=recognizer.listen(source, time_limit=15, phrase_time_limit=10)
                    audio = recognizer.listen(source,
                                              phrase_time_limit=10)  # phrase_time_limit: Limit the maximum length of a phrase.
                    str_working = recognizer.recognize_google(audio, language="ko")
            elif any(keyword in str_working for keyword in ["버전자동업데이트", '버저닝']):
                make_version_new(via_f_txt=True)
            elif any(keyword in str_working for keyword in ["프로젝트백업", "백업", "백업해라"]):

                restart_f_list_with_new_window_as_async([rf"{D_PKG_PY}/pk_kill_cmd_exe.py"])
            elif any(keyword in str_working for keyword in ["프로젝트백업", "백업", "백업해라"]):

                restart_f_list_with_new_window_as_async([rf"{D_PKG_PY}/pk_back_up_project.py"])
            elif any(keyword in str_working for keyword in ["텔레그램으로 백업"]):
                import nest_asyncio
                import asyncio
                f = back_up_pnx_without_venv_and_idea(pnx_working=D_PROJECT, d_dst=D_ARCHIVED, with_timestamp=0)
                nest_asyncio.apply()
                # asyncio.run(send_f_via_telegram_bot(f)) #  --> limit discovered : 단일파일 50MB 이상은 전송 불가 --> send_f_via_telegram_bot_v2(f)
                # send_f_via_telegram_bot_v2(f) # -->  fail --> timeout
                asyncio.run(move_f_via_telegram_bot_v3(f))  # -->
                # change_os_mode_to_power_saving_mode_as_s4()
                return  # return is necceary code, 처리 안시키면 PC 부팅 시 최대절전모드로 무한 진입, 컴퓨터 전원 재연결해야 된다 -> keyword = '' and use continue -> 시도하면 아마될듯
                keyword = ''
                continue
            elif any(keyword in str_working for keyword in ["퇴근해", "자자"]):

                restart_f_list_with_new_window_as_async([rf"{D_PKG_PY}/pk_자자.py"])
                keyword = ''
                continue
            elif any(keyword in str_working for keyword in ["트리정리"]):

                restart_f_list_with_new_window_as_async([rf"{D_PKG_PY}/pk_organize_tree.py"])
                keyword = ''
                continue
            elif any(keyword in str_working for keyword in ["피케이"]):
                cmd_f_in_cmd_exe_like_person(cmd_prefix='python', f=rf"{D_PROJECT}/ensure_pk_system_started")
            elif any(keyword in str_working for keyword in ["할일", "스케쥴러", "스케쥴가이드"]):
                ensure_todo_list_guided()
            elif any(keyword in str_working for keyword in ["토렌트", "토렌트다운로드"]):
                pass
            elif any(keyword in str_working for keyword in ["유튜브다운로드"]):
                pass
            elif any(keyword in str_working for keyword in ["youtube channel download", "유튜브채널다운로드"]):
                pass
            elif any(keyword in str_working for keyword in
                     ["ytctd", "youtube channel thumbnail download", "유튜브채널썸네일다운로드"]):
                youtube_channel_main_page_url = input('youtube_channel_main_page_url=')
                youtube_channel_main_page_url = youtube_channel_main_page_url.strip()
                download_youtube_thumbnails_from_youtube_channel_main_page_url(youtube_channel_main_page_url)
            elif any(keyword in str_working for keyword in ["오늘무슨날", "무슨날"]):
                ensure_spoken('today is christmas. happy christmas')
                ensure_spoken('today is newyear')
            elif any(keyword in str_working for keyword in ["오늘날짜", "날짜"]):
                speak_today_info_as_korean()
            elif any(keyword in str_working for keyword in ["요일", "오늘요일", "몇요일"]):
                ensure_spoken(f'{get_weekday_as_english()}')
            elif any(keyword in str_working for keyword in ["시간", "몇시야", "몇시"]):
                HH = get_time_as_('%H')
                mm = get_time_as_('%M')
                ensure_spoken(f'{int(HH)} hour {int(mm)} minutes')
            elif any(keyword in str_working for keyword in ["몇분이야", "몇분", "몇분"]):
                mm = get_time_as_('%M')
                ensure_spoken(f'{int(mm)} minutes')
            elif any(keyword in str_working for keyword in ["몇초야", "몇초"]):
                server_seconds = get_time_as_('%S')
                ensure_spoken(f'{server_seconds} seconds')
            elif any(keyword in str_working for keyword in ["날씨"]):
                ensure_printed_and_speak("Searching for weather...")
                get_comprehensive_weather_information_from_web()
            elif any(keyword in str_working for keyword in ["음악"]):
                ensure_sound_track_played()
                ensure_printed_and_speak("Playing music...")
            elif any(keyword in str_working for keyword in ["게임", "미니게임"]):
                run_up_and_down_game()
                ensure_printed_and_speak("Playing mini game...")
            elif any(keyword in str_working for keyword in ["exit"]):
                raise
            elif any(keyword in str_working for keyword in ["비디오"]):
                play_my_video_track()
                ensure_printed_and_speak("Playing video...")
            elif any(keyword in str_working for keyword in ["최대절전모드", "powersave", "sleep"]):
                save_power_as_s4()
                return  # return is necceary code, 처리 안시키면 PC 부팅 시 최대절전모드로 무한 진입, 컴퓨터 전원 재연결해야 된다.
            elif any(keyword in str_working for keyword in ["화면보호기", "화면보호"]):
                save_screen()
            else:
                ensure_printed(rf"it was Unknown command", print_color='yellow')  # woas
        except:
            ensure_printed_and_speak(f'''{__file__} 코드 exec 중 오류가 발생했습니다" ''', print_color='red')
            ensure_printed(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
            if not is_mic_device_connected():
                ensure_printed(f'''mic is disconnected. {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        loop_cnt += 1
        ensure_slept(milliseconds=200)
