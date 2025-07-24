# import win32process
import urllib
import toml
import tarfile
import speech_recognition as sr
import socket
import pyglet
import psutil
import mysql.connector
import colorama
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_video_filtered_list import get_video_filtered_list
from pkg_py.functions_split.get_d_working import get_d_working
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.pk_press import pk_press

from pkg_py.functions_split.cmd_to_os import cmd_to_os

from functools import partial
from cryptography.hazmat.backends import default_backend
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def run_acu_update_v3_exe_and_login_and_run_autoa2zdrive_release_exe(issue_log_index_data):
    # import pkg_py.system_object.static_logic as system_object.static_logic
    import inspect
    import os

    func_n = inspect.currentframe().f_code.co_name
    pk_print(str_working=rf'''{system_object.static_logic.PK_UNDERLINE}{func_n}()  {'%%%FOO%%%' if LTA else ''}''')
    AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE = rf"{system_object.static_logic.D_HOME}\Desktop\AutoA2zDrive\AutoA2ZDrive_Release_{issue_log_index_data["SW 버전"]}.exe"
    pk_print(
        str_working=rf'''AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE="{AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE}"  {'%%%FOO%%%' if LTA else ''}''')
    window_title_seg = "acu_update_v3_exe"
    if not does_pnx_exist(pnx=AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE):
        acu_update_v3_exe = rf"{system_object.static_logic.D_HOME}\Desktop\AutoA2zDrive\ACU_update_v3.exe"
        acu_update_v3_exe_p = get_p(pnx=acu_update_v3_exe)
        os.chdir(acu_update_v3_exe_p)
        cmd = rf' start cmd.exe /k "title {window_title_seg}&& {system_object.static_logic.D_HOME}\Desktop\AutoA2zDrive\ACU_update_v3.exe &" '
        cmd_to_os(cmd=cmd, mode="a")
        pw = get_token_from_f_token(f_token=rf'{system_object.static_logic.D_PKG_TXT}\token_linux_pw.txt',
                                    initial_str="")
        user_n = get_token_from_f_token(f_token=rf'{system_object.static_logic.D_PKG_TXT}\token_linux_id.txt',
                                        initial_str="")
        while 1:
            pk_sleep(milliseconds=2000)
            if is_window_opened(window_title_seg=window_title_seg):
                ensure_window_to_front(window_title_seg=window_title_seg)
                pk_sleep(milliseconds=500)
                write_like_person(str_working=user_n)
                pk_press("enter")
                write_like_person(str_working=pw)
                pk_press("enter")
                write_like_person("2")
                pk_press("enter")
                write_like_person(rf"{issue_log_index_data["SW 버전"]}")
                pk_press("enter")
                break
    else:
        run_autoa2zdrive_release_exe()

        # pk_sleep(milliseconds=15000)
        # while 1: #via ocr
        #     # text_string 바운딩박스 클릭 # GPU 연산 지원여부..
        #     # text_string = "downloading : 100%"
        #     text_string = "Press Enter Key To Quit Program...."
        #     text_coordinates = get_text_coordinates_via_easy_ocr(string=text_string)
        #     # text_coordinates = (692.0, 1047.5)
        #     if not text_coordinates:
        #         pk_sleep(milliseconds=30000)
        #     if text_coordinates:
        #         x_abs, y_abs = text_coordinates
        #         move_mouse(x_abs=x_abs, y_abs=y_abs)
        #         click_mouse_left_btn(x_abs=x_abs, y_abs=y_abs)
        #         pk_print(string = rf'''text_string="{text_string}"  {'%%%FOO%%%' if LTA else ''}''')
        #         break
        # img_pnx = rf"{system_object.static_logic.PROJECT_D}\pk_image\screenshot_Press_Enter_Key_To_Quit_Program_2024_11_21_11_30_35.png"
        # click_center_of_img_recognized_by_mouse_left(img_pnx=img_pnx, loop_limit_cnt=10)
