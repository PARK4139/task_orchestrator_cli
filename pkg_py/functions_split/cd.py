import zlib
import yt_dlp
import win32com.client
import toml
import threading
import shlex
import pygetwindow
import os.path
import ipdb
import cv2
import colorama
import chardet
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from seleniumbase import Driver
from pynput import mouse
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.directories import D_PKG_TXT
from base64 import b64decode
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.pk_system_object.directories import D_WORKING, D_DOWNLOADS
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.get_pnxs import get_pnxs


def cd(sys_argv):
    '''
    [archived]
    [개요]
    타이핑 최소화

    [참고]
    pk_cd.cmd 에 종속적으로 동작
    실제로 cd 되지 않음. cd 할 경로를 f_cd_txt 에 저장함 pk_cd.cmd 에서 cd 함

    [사용법]
    pk cd 로 가용 cd {index} 출력
    cd {index} 호출하여 사용
    '''

    import os
    import sys
    f_cd_txt = os.path.join(D_PKG_TXT, "pk_cd.txt")
    if not does_pnx_exist(f_cd_txt):
        ensure_pnx_made(f_cd_txt, mode='f')
    d_working_list = get_pnxs(with_walking=0, d_working=get_d_working_in_python(), filter_option='d')
    minus_list = [rf"{D_PKG_PY}/???.py"]
    minus_list = [get_pnx_os_style(element) for element in minus_list]
    plus_list = [
        D_PKG_PY,
        D_PROJECT,
        D_WORKING,
        D_DOWNLOADS,
        D_HOME,
        D_DESKTOP,
    ]
    d_working_with_idx_dict = get_TBD_pnx_working_with_idx_dict(origin_list=d_working_list, minus_list=minus_list,
                                                                pnx_plus_list=plus_list)
    # d_working_without_idx_list = get_pnx_working_without_idx_list(pnx_working_with_idx_dict=d_working_with_idx_dict)
    d_working_idx_list = get_idx_list(item_iterable=d_working_with_idx_dict)
    # d_working_idx_list = list(map(str, d_working_idx_list))  # each (element ->> str(element))
    if LTA:
        ensure_printed(f'''len(sys_argv)={len(sys_argv)} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''f_cd_txt={f_cd_txt} {'%%%FOO%%%' if LTA else ''}''')
    if len(sys_argv) == 1:
        return
    elif len(sys_argv) == 2:
        nx_by_user_input = sys_argv[1]
        if LTA:
            ensure_printed(f'''nx_by_user_input={nx_by_user_input} {'%%%FOO%%%' if LTA else ''}''')
        if str.isdigit(nx_by_user_input):
            if LTA:
                ensure_printed(f'''인자가 숫자입니다. {'%%%FOO%%%' if LTA else ''}''')
            return
        else:
            if LTA:
                ensure_printed(f'''인자가 숫자가 아닙니다. {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            else:
                if does_pnx_exist(sys.argv[1]):
                    d_dst = os.path.abspath(sys.argv[1])
                    save_d_to_f(d=d_dst, f=f_cd_txt)
                return
