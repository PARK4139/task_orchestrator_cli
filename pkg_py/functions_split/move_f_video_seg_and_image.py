import zlib
import urllib
import undetected_chromedriver as uc
import tomllib
import shlex
import pyaudio
import psutil
import os
import colorama
from urllib.parse import quote
from PySide6.QtWidgets import QApplication
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_list_written_to_f import ensure_list_written_to_f
from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_f import is_f
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def move_f_video_seg_and_image(d_working, d_dst_extension_to_move=None):
    import os
    import shutil

    # 대상 d 생성
    for _, d_n in d_dst_extension_to_move.items():
        d = os.path.join(d_working, d_n)
        if not os.path.exists(d):
            os.makedirs(d)

    # d 내 f 탐색 및 이동
    for f_nx in os.listdir(d_working):
        f = os.path.join(d_working, f_nx)

        # f만 처리
        if is_f(f):
            # f_ext = f_nx.split('.')[-1].lower()  # 확장자를 소문자로 변환

            d_n = None
            for key, dir_name in d_dst_extension_to_move.items():  # todo : dir_name 를 d_n 으로 변경 후 정상적인지 테스트 해보기
                if key in f_nx.lower():  # f 이름 또는 확장자에 키가 포함되면 매핑
                    d_n = dir_name
                    break

            if d_n:
                d_dst = os.path.join(d_working, d_n)
                f_dst = os.path.join(d_dst, f_nx)

                # 동일한 f이 있을 경우 이름 변경
                base, ext = os.path.splitext(f_nx)
                counter = 1
                while os.path.exists(f_dst):
                    f_dst = os.path.join(d_dst, f"{base}_{counter}{ext}")
                    counter += 1

                # f 이동
                try:
                    shutil.move(f, f_dst)
                    ensure_printed(f"f 이동 {f_dst}", print_color='green')
                except Exception as e:
                    ensure_printed(f"f 이동 {f_dst}. 오류: {e}", print_color='red')
