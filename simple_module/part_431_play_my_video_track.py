import yt_dlp
import timeit
import ipdb
from tkinter import UNDERLINE
from selenium.webdriver.common.keys import Keys
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext

from pkg_py.simple_module.part_005_get_nx import get_nx


def play_my_video_track():
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    # cmd_to_os(cmd=rf'taskkill /f /im "PotPlayer64.exe" ', debug_mode=True)

    # 보던 거 재생
    # 바탕화면에 있는 PotPlayer64.dpl 를 pkg_video에 복사
    ensure_pnx_made(pnx=F_PKG_VIDEO_POTPLAYER64_DPL, mode='f')
    cmd_to_os(cmd=rf'explorer "{F_PKG_VIDEO_POTPLAYER64_DPL}" ')

    # 보지않은 거 틀기
    # classifying 안의 비디오들 재생
    pass
