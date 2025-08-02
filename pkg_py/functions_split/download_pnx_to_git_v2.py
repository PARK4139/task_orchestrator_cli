import subprocess
import speech_recognition as sr
import pygetwindow
import pyaudio
import json
import functools
import cv2
import asyncio
from selenium.common.exceptions import ElementClickInterceptedException
from pkg_py.functions_split.ensure_iterable_printed_as_vertical import ensure_iterable_printed_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.ensure_losslesscut_reran import ensure_losslesscut_reran
from pkg_py.functions_split.is_window_title_front import is_window_title_front
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.system_object.directories import D_PK_WORKING

from PIL import Image
from mutagen.mp3 import MP3
from collections import Counter
from bs4 import BeautifulSoup
from pkg_py.functions_split.ensure_video_played_at_losslesscut import ensure_video_played_at_losslesscut
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def download_pnx_to_git_v2(d_working, git_repo_url, commit_msg, branch_n):
    import traceback
    import threading
    from colorama import init as pk_colorama_init

    ensure_colorama_initialized_once()

    def ask_user_yes_no(msg, timeout=5):
        ensure_printed(f"{msg} (y/n, {timeout}초 내 응답): ", print_color='yellow')
        result = {'answer': None}

        def _get_input():
            try:
                result['answer'] = input().strip().lower()
            except Exception:
                result['answer'] = None

        thread = threading.Thread(target=_get_input)
        thread.daemon = True
        thread.start()
        thread.join(timeout)

        if result['answer'] is None:
            ensure_printed("시간 초과: 응답이 없어 작업을 건너뜁니다.", print_color='red')
            return 0

        return result['answer'] == 'y'

    try:
        if not does_pnx_exist(pnx=d_working):
            ensure_pnx_made(pnx=d_working, mode='d')

        d_git = rf"{d_working}/.git"

        if not does_pnx_exist(pnx=d_git):
            std_list = ensure_command_excuted_to_os(f'git clone -b {branch_n} {git_repo_url} {d_working}')
            debug_state_for_py_data_type('%%%CLONE%%%', std_list)

            if any("fatal:" in line.lower() for line in std_list):
                ensure_printed(f"Git clone 실패: {std_list}", print_color='red')
                return
        else:
            os.chdir(d_working)
            std_list = ensure_command_excuted_to_os(f'git pull origin {branch_n}')
            debug_state_for_py_data_type('%%%PULL%%%', std_list)

            if any("couldn't find remote ref" in line.lower() for line in std_list):
                ensure_printed(f"브랜치 '{branch_n}' 이(가) 원격 레포지토리에 없습니다.", print_color='red')
                if ask_user_yes_no(f"브랜치 '{branch_n}' 를 새로 만드시겠습니까?", timeout=10):
                    std_list = ensure_command_excuted_to_os(f'git checkout -b {branch_n}')
                    debug_state_for_py_data_type('%%%CHECKOUT_NEW_BRANCH%%%', std_list)

                    std_list = ensure_command_excuted_to_os(f'git push -u origin {branch_n}')
                    debug_state_for_py_data_type('%%%PUSH_NEW_BRANCH%%%', std_list)

                    if any("error:" in line.lower() or "failed to push" in line.lower() for line in std_list):
                        ensure_printed(f"브랜치 푸시 실패: {std_list}", print_color='red')

                        # 빈 커밋 생성 여부 질의
                        if ask_user_yes_no("커밋이 없어서 푸시에 실패한 것 같습니다. 빈 커밋을 생성할까요?", timeout=10):
                            std_list = ensure_command_excuted_to_os('git commit --allow-empty -m "init empty commit"')
                            debug_state_for_py_data_type('%%%EMPTY_COMMIT%%%', std_list)

                            std_list = ensure_command_excuted_to_os(f'git push -u origin {branch_n}')
                            debug_state_for_py_data_type('%%%PUSH_AFTER_EMPTY_COMMIT%%%', std_list)

                            if any("error:" in line.lower() or "failed to push" in line.lower() for line in std_list):
                                ensure_printed(f"빈 커밋 후 푸시도 실패했습니다: {std_list}", print_color='red')
                                return
                        else:
                            ensure_printed("사용자가 빈 커밋 생성을 취소했습니다.", print_color='red')
                            return
                else:
                    ensure_printed("사용자가 브랜치 생성을 취소했습니다.", print_color='red')
                    return
            elif any("fatal:" in line.lower() for line in std_list):
                ensure_printed(f"Git pull 실패: {std_list}", print_color='red')
                return

        ensure_printed(f"Git 작업 완료: {d_working} {'%%%FOO%%%' if LTA else ''}", print_color='green')

    except Exception:
        ensure_printed(f"{traceback.format_exc()} {'%%%FOO%%%' if LTA else ''}", print_color='red')
