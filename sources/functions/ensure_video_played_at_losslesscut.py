import traceback

import logging

from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_video_played_at_losslesscut(video_player=None, loop_cnt=0):
    try:
        from sources.objects.pk_video_player import PkVideoPlayer
        from sources.objects.task_orchestrator_cli_files import F_LOSSLESSCUT_EXE

        # initialize video_player
        if video_player is None:
            video_player = PkVideoPlayer(f_video_player=F_LOSSLESSCUT_EXE)

        #  aleardy loaded
        if video_player.is_video_loaded_already(loop_cnt):
            return False

        # rerun program
        if not video_player.ensure_video_player_reopened():
            return False

        # load video
        if not video_player.ensure_video_file_loaded_on_video_player(video_to_play=video_player.f_video_to_load):
            return False
        # play video
        if not video_player.ensure_video_player_play_button_pressed():
            return False

        # maximize program
        if not video_player.ensure_video_player_screen_maximized():
            return False

        # idle window title monitored # pk_option
        if 1 <= loop_cnt :
            video_player.ensure_video_player_idle_window_title_monitored()

        return True

    except:
        ensure_debug_loged_verbose(traceback)


