import winreg
import webbrowser
import shutil
import psutil
import pandas as pd
import cv2
from zipfile import BadZipFile
from yt_dlp import YoutubeDL
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from functools import partial as functools_partial
from fastapi import HTTPException
from dirsync import sync
from cryptography.hazmat.primitives import padding
from bs4 import ResultSet
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.pk_system_object.directories import D_DOWNLOADS
from pkg_py.functions_split.get_list_calculated import get_list_calculated
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.pk_print import pk_print


def make_version_new_v_1_0_1(via_f_txt=False, working_list=None, debug_mode=True):
    import inspect
    import os
    import re
    import shutil

    func_n = inspect.currentframe().f_code.co_name
    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'
    ensure_pnx_made(pnx=f_func_n_txt, mode='f')
    open_pnx_by_ext(pnx=f_func_n_txt)

    def get_next_versioned_nx(f_nx, debug_mode=True):
        func_n = inspect.currentframe().f_code.co_name
        name, ext = os.path.splitext(f_nx)
        files = os.listdir("pkg_friday")

        # 정규표현식으로 "v1.x.y" 형태의 버전을 찾기
        versioned_files = [f for f in files if re.match(fr"{re.escape(name)}_v\d+\.\d+\.\d+{re.escape(ext)}", f)]

        if versioned_files:
            latest_version = max(versioned_files, key=lambda x: list(map(int, re.findall(r"\d+", x)[-3:])))
            major, minor, patch = map(int, re.findall(r"\d+", latest_version)[-3:])
            patch += 1
            next_version = f"{major}.{minor}.{patch}"
        else:
            next_version = "1.0.0"
        next_versioned_pnx = f"{name}_v{next_version}{ext}"
        pk_print(f'''next_versioned_pnx="{next_versioned_pnx}" ''', print_color='white')
        return next_versioned_pnx

    def cp_and_mv_with_version(src, debug_mode=True):
        func_n = inspect.currentframe().f_code.co_name
        # make new version
        # cp
        if not does_pnx_exist(src):
            pk_print(f"{src} f을 찾을 수 없습니다.")
            return
        src_nx = get_nx(src)
        f_next_versioned_nx = get_next_versioned_nx(src_nx)
        shutil.copy2(src, f_next_versioned_nx)
        pk_print(f'''src="{src}"''')
        pk_print(f'''f_next_versioned_nx="{f_next_versioned_nx}"''')
        pk_print(f"''{src}'를  {f_next_versioned_nx}'로 copied.")
        f = src
        f_nx = get_nx(f)
        f_n = get_n(f)
        f_x = get_x(f)

        files = os.listdir("pkg_friday")

        dst = rf"{D_DOWNLOADS}\deprecated"
        os.makedirs(dst, exist_ok=True)

        # mv
        # 버전 f만 추출 #최신버전 원본제외
        f_list_versioned_required = files
        f_list_versioned_required = get_list_leaved_element_contain_prompt(working_list=f_list_versioned_required,
                                                                           prompt=f_n)
        f_list_versioned_required.remove(f_nx)  # 원본제외
        f_list_versioned_required.remove(f_next_versioned_nx)  # 최신버전제외
        print_iterable_as_vertical(item_iterable=f_list_versioned_required, item_iterable_n="f_list_versioned_required")

        pk_print(f'''f="{f}"''')
        pk_print(f'''f_n="{f_n}"''')
        pk_print(f'''f_x="{f_x}"''')
        pk_print(f'''len(f_list_versioned_required)={len(f_list_versioned_required)}''')
        pk_print(f'''len(f_list_versioned_required) >= 1="{len(f_list_versioned_required) >= 1}"''')
        if len(f_list_versioned_required) > 1:
            for f in f_list_versioned_required:
                shutil.move(f, dst)
                pk_print(f"'{f}' moved to '{dst}'")

    if via_f_txt == True and working_list is None:
        working_list = get_list_from_f(f=f_func_n_txt)
        working_list = get_list_removed_element_contain_prompt(working_list=working_list, prompt="#")
        working_list = get_list_replaced_element_from_str_to_str(working_list=working_list, from_str='\n', to_str='')
        for item_str in working_list:
            item_str = get_str_replaced_from_str_to_str_new(item_str=item_str, from_str='PROJECT_D', to_str=D_PROJECT)
            # item=get_pnx_windows_style(pnx=item)
            item_str = get_pnx_unix_style(pnx=item_str)
            pk_print(f'''item_str="{item_str}"''')
            cp_and_mv_with_version(item_str)
    if via_f_txt is not True and working_list is not None:
        for f in working_list:
            cp_and_mv_with_version(f)
