# import win32gui
import uuid
import subprocess
import re
import pandas as pd
import functools
import browser_cookie3
from webdriver_manager.chrome import ChromeDriverManager
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT

from passlib.context import CryptContext
from functools import lru_cache
from collections import Counter
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list
from pkg_py.simple_module.part_001_is_d import is_d
from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def build_pk_project_via_pyinstaller():
    import os

    # 프로젝트 d로 이동
    os.chdir(D_PROJECT)

    if does_pnx_exist(pnx=D_VENV):
        pk_print(f"{D_VENV} d가 있습니다")

        # 현재d의 불필요한 타겟들을 삭제
        items_useless = [
            rf"{D_PROJECT}\pk.exe",
            rf"{D_PROJECT}\build",
            rf"{D_PROJECT}\dist",
            rf"{D_PROJECT}\_internal",
            rf"{D_PROJECT}\dist.zip",
            rf"{D_PROJECT}\pk.spec",
        ]
        for item in items_useless:
            remove_pnx_parmanently(pnx=item)

        # pip 업그레이드
        cmd_to_os(cmd="python -m pip install --upgrade pip")

        # pip 업그레이드
        cmd_to_os(cmd="pip install pyinstaller --upgrade")

        if not LTA:
            cmd_to_os(cmd=rf"python -m PyInstaller -i .\pkg_png\icon.PNG pk_test_test.py")

        if LTA:
            cmd_to_os(cmd=rf'echo d | xcopy ".\pkg_mp3" ".\dist\pk_test_test\_internal\pkg_mp3" /e /h /k /y')

        # f = f'{D_PROJECT}/pk_temp.py'
        # write_f(f)

        # 가상환경을 활성화하고, 그 후에 파이썬 스크립트 exec
        # run

        # pk_temp.py
        # os.remove(f)

    else:
        pk_print(f"{D_VENV} d가 없습니다")
