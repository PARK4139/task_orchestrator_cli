import pyaudio
import numpy as np
# from project_database.test_project_database import MySqlUtil
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_400_state_via_database import PkSqlite3DB
from mutagen.mp3 import MP3

from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def locate_dip_switchitch_on_board_to_left_down():
    # if no:
    #     left_down # 위치 재확인필요
    #     #         2개 스위치 제외(A/B selector, S/W 5) # 위치 재확인필요
    todo('%%%FOO%%%')
