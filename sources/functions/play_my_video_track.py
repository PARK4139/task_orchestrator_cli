import yt_dlp
import timeit
import ipdb
from tkinter import UNDERLINE
from selenium.webdriver.common.keys import Keys
from prompt_toolkit import PromptSession
from sources.functions.get_f_video_to_load import get_f_video_to_load
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.objects.pk_state_via_context import SpeedControlContext

from sources.functions.get_nx import get_nx


def play_my_video_track():
    import inspect

    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    # ensure_command_executed(cmd=rf'taskkill /f /im "PotPlayer64.exe" ', debug_mode=True)

    # 보던 거 재생
    # 바탕화면에 있는 PotPlayer64.dpl 를 task_orchestrator_cli_video에 복사
    ensure_pnx_made(pnx=F_VIDEO_POTPLAYER64_DPL, mode='f')
    ensure_command_executed(cmd=rf'explorer "{F_VIDEO_POTPLAYER64_DPL}" ')

    # 보지않은 거 틀기
    # classifying 안의 비디오들 재생
    pass
