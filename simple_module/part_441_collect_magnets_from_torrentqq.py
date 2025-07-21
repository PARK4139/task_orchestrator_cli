# import win32process
import win32con
import urllib.parse
import urllib
import threading
import subprocess
import keyboard
import functools
import chardet
from zipfile import BadZipFile
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pytube import Playlist
from pynput import mouse
from pkg_py.simple_module.part_633_print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_016_pk_print_once import pk_print_once
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.pk_system_layer_files import F_POT_PLAYER_MINI_64_EXE
from pkg_py.pk_system_layer_directories import D_PKG_TXT
from PIL import Image
from functools import lru_cache
from enum import Enum
from colorama import init as pk_colorama_init
from bs4 import ResultSet
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.pk_system_layer_100_os import is_os_windows
from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def collect_magnets_from_torrentqq(search_keyword=None, driver=None, via_f_txt=True):
    import sys

    import traceback

    try:
        if not is_internet_connected():
            raise

        collect_magnets_from_nyaa_si_txt = rf'{D_PKG_TXT}/collect_magnets_from_nyaa_si.txt'
        magnets_set = set()

        # [OPTION]
        # window_title_seg = get_nx(collect_magnets_from_nyaa_si_txt)
        # if not is_window_open(window_title_seg=window_title_seg):
        # open_pnx_by_ext(pnx=f_func_n_txt)
        # move_window_to_front(window_title_seg=window_title_seg)
        # cmd_to_os(cmd=rf'explorer "{f_func_n_txt}" ', debug_mode=True, mode="a")

        # [OPTION]
        # search_keyword = search_keyword
        # search_keyword ="________________"
        # search_keyword = input_validated("serch_keyword")

        # [OPTION]
        # filtered_list.append(search_keyword)
        filtered_list = get_list_contained_with_stamp_from_f(f=collect_magnets_from_nyaa_si_txt, STAMP=STAMP_TORRENTQQ)

        # 전처리
        pk_print(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        filtered_list = get_list_removed_element_contain_prompt(working_list=filtered_list,
                                                                prompt="#")  # 시작 문자가 '#'인 요소를 remove
        pk_print(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        filtered_list = get_list_striped_element(working_list=filtered_list)
        pk_print(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        filtered_list = get_list_removed_element_empty(working_list=filtered_list)
        pk_print(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        filtered_list = get_list_deduplicated(working_list=filtered_list)
        pk_print(f'''search_keyword_list={filtered_list}  {'%%%FOO%%%' if LTA else ''}''')
        print_iterable_as_vertical(item_iterable=filtered_list, item_iterable_n='search_keyword_list')
        pk_print(working_str=rf'''len(search_keyword_list)="{len(filtered_list)}"  {'%%%FOO%%%' if LTA else ''}''')

        # if driver is None:
        #     driver = get_driver_selenium_solved_cloudflare_sequrity()
        # get_driver_selenium_solved_cloudflare_sequrity() 재사용하면 magnet_link not found

        for search_keyword in filtered_list:
            # magnets_set = magnets_set | get_magnets_set_from_torrent_qq(search_keyword=search_keyword, driver=driver)# fail
            magnets_set = magnets_set | get_magnets_set_from_torrent_qq(search_keyword=search_keyword)

            # save magnets collected
            magnets_txt = rf'{D_PKG_TXT}/pk_magnets.txt'
            magnets_list = get_list_url_decoded_element(magnets_set)
            magnets_list = [magnet for magnet in sorted(magnets_list, key=lambda magnet: magnet.split("&dn=")[
                1] if "&dn=" in magnet else "")]
            magnets_list = [magnet for magnet in sorted(magnets_list, key=lambda magnet: magnet.split("&mgt_url=")[
                1] if "&mgt_url=" in magnet else "")]
            write_list_to_f(f=magnets_txt, working_list=magnets_list, mode="a")

            # magnets 중복remove
            magnets_list = get_list_from_f(f=magnets_txt)
            magnets_list = get_list_striped_element(working_list=magnets_list)
            magnets_list = get_list_removed_element_empty(working_list=magnets_list)
            magnets_list = get_list_deduplicated(working_list=magnets_list)
            write_list_to_f(f=magnets_txt, working_list=magnets_list, mode="w")

        # search_keyword_list 목록추가, search_keyword_list 중복remove
        filtered_list = get_list_from_f(f=collect_magnets_from_nyaa_si_txt) + filtered_list
        filtered_list = get_list_striped_element(working_list=filtered_list)
        filtered_list = get_list_removed_element_empty(working_list=filtered_list)
        filtered_list = get_list_deduplicated(working_list=filtered_list)
        write_list_to_f(f=collect_magnets_from_nyaa_si_txt, working_list=filtered_list, mode="w")

    except:
        traceback.print_exc(file=sys.stdout)
