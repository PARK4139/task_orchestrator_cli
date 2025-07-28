
import subprocess
import shutil
import pythoncom
import os.path
import easyocr
import cv2
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from prompt_toolkit import PromptSession
from pkg_py.functions_split.is_losslesscut_running import is_losslesscut_running
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.system_object.etc import PkFilter
from pkg_py.system_object.files import F_POT_PLAYER_MINI_64_EXE
# from pkg_py.system_object.print_red import print_red
from PIL import Image
from datetime import timedelta
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def classify_pnx_list_at_tree(d_working, mode, with_walking, debug_mode=True):
    ensure_printed(str_working=rf'''d="{d_working}" mode="{mode}"  {'%%%FOO%%%' if LTA else ''}''')

    if mode == 'f':
        # todo : ref : f이 너무 많을떄(file_cnt_limit이 100개(?) 넘어가면) without_walking=True
        # classify_pnxs_to_pkg_compressed(pnx)
        # classify_pnxs_to_pkg_document(pnx)
        # classify_pnxs_to_pkg_video(pnx)
        # classify_pnxs_to_pk_image(pnx)
        # classify_pnxs_to_pkg_soundtrack(pnx)
        # classify_pnxs_to_special_keyword_dir(pnx)

        # classify_pnxs_to_pkg_compressed(src=src, without_walking=False)
        # classify_pnxs_to_pkg_document(pnx=src, without_walking=False)
        # classify_pnxs_to_pkg_video(pnx=src, without_walking=False)
        # classify_pnxs_to_pk_image(pnx=src, without_walking=False)
        # classify_pnxs_to_pkg_soundtrack(pnx=src, without_walking=False)
        classify_pnx_list_to_d_special_keyword(d_src=d_working, with_walking=with_walking)

        # classify_pnxs_to_pn_dir(src=src)
        # classify_pnxs_to_pk_image_via_ai() #todo : add : AI 이미지 분류기
        # classify_pnxs_to_pkg_video_via_ai() #todo : add : AI 동영상 분류기 # 동영상 내용보고 분류기준에 따라 분류
        # merge_pnxs_via_text_file() # todo : add : merge d and d
