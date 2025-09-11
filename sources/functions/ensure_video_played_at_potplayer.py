from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_video_played_at_potplayer(video_player=None, loop_cnt=0):
    from sources.objects.task_orchestrator_cli_files import F_POT_PLAYER
    from sources.objects.pk_video_player import PkVideoPlayer

    # initialize video_player
    if video_player is None:
        video_player = PkVideoPlayer(f_video_player=F_POT_PLAYER)

    #  aleardy loaded
    if video_player.is_video_loaded_already(loop_cnt):
        return False
    # rerun program
    # video_player.ensure_video_player_reopened()    # pot player 는 multiple instance program 이기 때문에 불필요

    # load video
    if not video_player.ensure_video_file_loaded_on_video_player(video_to_play=video_player.f_video_to_load):
        return False

    # play video
    # video_player.ensure_video_player_play_button_pressed() # pot player 로드 시 자동 재생.

    # maximize program
    if not video_player.ensure_video_player_screen_maximized():
        return False

    # idle window title monitored
    # video_player.ensure_video_player_idle_window_title_monitored()

    # export window title monitored
    # while 1:
    #     logging.debug(f'''video_player.window_title_next={video_player.window_title_next} {'%%%FOO%%%' if LTA else ''}''')

    return True
