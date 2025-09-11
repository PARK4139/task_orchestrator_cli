def ensure_sound_track_played():
    import logging
    from objects.task_orchestrator_cli_files import F_SOUND_POTPLAYER64_DPL
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.ensure_potplayer_killed import ensure_potplayer_killed
    from sources.functions.is_os_linux import is_os_linux
    from sources.functions.is_os_windows import is_os_windows

    ensure_potplayer_killed()  # task_orchestrator_cli_option

    if is_os_windows():
        ensure_command_executed(cmd=rf'explorer "{F_SOUND_POTPLAYER64_DPL}" ')

        # video_player = PkVideoPlayer(f_video_player=F_POT_PLAYER)
        # ensure_video_played_at_potplayer(video_player)

    elif is_os_linux():
        # Linux에서는 기본 오디오 플레이어 사용
        try:
            # 다양한 오디오 플레이어 시도
            players = ['vlc', 'mpv', 'mplayer', 'ffplay']
            for player in players:
                try:
                    ensure_command_executed(cmd=f'{player} --help')
                    logging.debug(f"{player}로 오디오 재생을 시도합니다.")
                    # 여기서 실제 오디오 파일 경로를 지정해야 함
                    # ensure_command_executed(cmd=f'{player} /path/to/audio/file.mp3')
                    break
                except:
                    continue
            else:
                logging.debug("️ 사용 가능한 오디오 플레이어를 찾을 수 없습니다.")
        except Exception as e:
            logging.debug(f"오디오 재생 실패: {e}")
    else:
        # macOS에서는 afplay 사용
        try:
            ensure_command_executed(cmd='afplay --help')
            # ensure_command_executed(cmd='afplay /path/to/audio/file.mp3')
        except Exception as e:
            logging.debug(f"오디오 재생 실패: {e}")
