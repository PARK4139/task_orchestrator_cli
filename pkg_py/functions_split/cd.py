
# d_working_idx_list = list(map(str, d_working_idx_list))  # each (element ->> str(element))
# d_working_without_idx_list = get_pnx_working_without_idx_list(pnx_working_with_idx_dict=d_working_with_idx_dict)
'''
D_DESKTOP,
D_DOWNLOADS,
D_HOME,
D_PKG_PY,
D_PROJECT,
D_WORKING,
[archived]
[개요]
[사용법]
[참고]
]
cd {index} 호출하여 사용
d_dst = os.path.abspath(sys.argv[1])
d_working_idx_list = get_idx_list(item_iterable=d_working_with_idx_dict)
d_working_list = get_pnx_list(with_walking=0, d_working=get_d_working_in_python(), filter_option='d')
d_working_with_idx_dict = get_TBD_pnx_working_with_idx_dict(origin_list=d_working_list, minus_list=minus_list,
def pk_cd(sys_argv):
elif len(sys_argv) == 2:
else:
ensure_pnx_made(f_cd_txt, mode='f')
f_cd_txt = os.path.join(D_PKG_TXT, "pk_cd.txt")
from base64 import b64decode
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.print import pk_print
from pkg_py.pk_system_object.directories import D_PKG_PY
from pkg_py.pk_system_object.directories import D_PKG_TXT
from pkg_py.pk_system_object.directories import D_WORKING, D_DOWNLOADS
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from pkg_py.pk_system_object.encodings import Encoding
from pkg_py.pk_system_object.files import F_FFMPEG_EXE
from pkg_py.pk_system_object.local_test_activate import LTA
from pynput import mouse
from seleniumbase import Driver
from urllib.parse import urlparse
from webdriver_manager.chrome import ChromeDriverManager
if LTA:
if does_pnx_exist(sys.argv[1]):
if len(sys_argv) == 1:
if not does_pnx_exist(f_cd_txt):
if str.isdigit(nx_by_user_input):
import chardet
import colorama
import cv2
import ipdb
import os
import os.path
import pygetwindow
import shlex
import sys
import threading
import toml
import win32com.client
import yt_dlp
import zlib
minus_list = [get_pnx_os_style(element) for element in minus_list]
minus_list = [rf"{D_PKG_PY}/???.py"]
nx_by_user_input = sys_argv[1]
pk cd 로 가용 cd {index} 출력
pk_cd.cmd 에 종속적으로 동작
pk_print(f'''f_cd_txt={f_cd_txt} {'%%%FOO%%%' if LTA else ''}''')
pk_print(f'''len(sys_argv)={len(sys_argv)} {'%%%FOO%%%' if LTA else ''}''')
pk_print(f'''nx_by_user_input={nx_by_user_input} {'%%%FOO%%%' if LTA else ''}''')
pk_print(f'''인자가 숫자가 아닙니다. {'%%%FOO%%%' if LTA else ''}''', print_color='red')
pk_print(f'''인자가 숫자입니다. {'%%%FOO%%%' if LTA else ''}''')
plus_list = [
pnx_plus_list=plus_list)
return
save_d_to_f(d=d_dst, f=f_cd_txt)
실제로 cd 되지 않음. cd 할 경로를 f_cd_txt 에 저장함 pk_cd.cmd 에서 cd 함
타이핑 최소화
