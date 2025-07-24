

import winreg

import tqdm
import tarfile
import subprocess
import requests
import re
import random, math
import random
import psutil
import platform
import paramiko
import json
import ipdb
import chardet

from urllib.parse import urlparse
from selenium.webdriver.chrome.service import Service
from PySide6.QtWidgets import QApplication
from pynput import mouse
from prompt_toolkit import PromptSession
from pkg_py.functions_split.get_f_video_to_load import get_f_video_to_load
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.system_object.files import F_FFMPEG_EXE
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.system_object.state_via_database import PkSqlite3DB
from pkg_py.system_object.state_via_context import SpeedControlContext
from pkg_py.system_object.is_os_windows import is_os_windows
from functools import partial as functools_partial
from fastapi import HTTPException
from Cryptodome.Random import get_random_bytes
from concurrent.futures import ThreadPoolExecutor
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def copy_pnx_with_overwrite(pnx, dst):
    # 같은이름의 f이 이미 있으면 copy 하지 않음

    import shutil
    import traceback

    try:
        # shutil.copy2(pnx, dst)  # shutil.copy2 copies the file and metadata, overwrites if exists # 사용중인 f에 대해서는 권한문제있어서 복사불가한 방식
        # cmd=f'copy "{pnx}" "{dst}"' # d 복사안됨
        # cmd=f'xcopy /E /H /K /Y "{pnx}" "{dst}"'
        # cmd=f'robocopy "{pnx}" "{dst}" /E /Z /R:3 /W:5 /COPYALL /DCOPY:T'
        # cmd=f'robocopy "{pnx}" "{dst}" /E /Z /R:3 /W:5 /COPY:DATSOU /DCOPY:T'
        # cmd=f'runas /user:Administrator robocopy "{pnx}" "{dst}" /E /Z /R:3 /W:5 /COPY:DATSOU /DCOPY:T'
        # cmd=rf'powershell -cmd "Start-Process cmd -ArgumentList \'/c robocopy \"{pnx}\" \"{dst}\" /E /Z /R:3 /W:5 /COPY:DATSOU /DCOPY:T\' -Verb runAs"'
        # cmd=rf'powershell -cmd "Start-Process cmd -ArgumentList \'/c xcopy \\"{pnx}\\" \\"{dst}\\" "'
        # cmd=rf'powershell -cmd "Start-Process cmd -ArgumentList \'/c xcopy \\"{pnx}\\" \\"{dst}\\" /E /H /K /Y\' -Verb runAs"'
        # subprocess.run(cmd, shell=True, check=True)
        # press("enter", interval=0.6)
        pnx = get_pnx_os_style(pnx=pnx)
        pnx = pnx.replace("\"", "")
        if pnx.strip() == "":
            pk_print(str_working=rf''' {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            return
        pnx_p = get_p(pnx)
        pnx_n = get_n(pnx)
        f_zip = rf'{pnx_p}/{pnx_n}.zip'
        f_zip = get_pnx_os_style(pnx=f_zip)
        f_zip_new = rf"{dst}/{get_nx(pnx=f_zip)}"
        f_zip_new = get_pnx_os_style(pnx=f_zip_new)

        # remove
        if does_pnx_exist(pnx=f_zip_new):
            move_pnx_to_pk_recycle_bin(pnx=f_zip_new)

        # compress
        compress_pnx_via_bz_exe(pnx=pnx, f_zip=f_zip)

        # move
        shutil.move(src=f_zip, dst=dst)

        # decompress
        pk_decompress_f_via_zip(f=f_zip_new)

        # remove
        move_pnx_to_pk_recycle_bin(pnx=f_zip_new)
    except:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')

        pk_chdir(D_PROJECT)
