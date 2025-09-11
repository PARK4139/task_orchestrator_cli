import pyaudio
import numpy as np

from sources.functions.ensure_pressed import ensure_pressed
from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
from sources.objects.pk_state_via_database import PkSqlite3DB
from mutagen.mp3 import MP3

from sources.functions.get_pnxs import get_pnxs


def locate_dip_switchitch_on_board_to_left_down():
    # if no:
    #     left_down # 위치 재확인필요
    #     #         2개 스위치 제외(A/B selector, S/W 5) # 위치 재확인필요
    todo('%%%FOO%%%')
