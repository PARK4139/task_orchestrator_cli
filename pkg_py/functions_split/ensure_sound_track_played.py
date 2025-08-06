from pkg_py.system_object.local_test_activate import LTA


def ensure_sound_track_played():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_p import get_p
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.system_object.files import F_PKG_IMAGE_AND_VIDEO_AND_SOUND_POTPLAYER64_DPL
    from pkg_py.functions_split.ensure_printed import ensure_printed

    import inspect
    func_n = inspect.currentframe().f_code.co_name
    
    if is_os_windows():
        # Windows에서는 PotPlayer 사용
        F_PKG_IMAGE_AND_VIDEO_AND_SOUND_POTPLAYER64_DPL = get_pnx_os_style(F_PKG_IMAGE_AND_VIDEO_AND_SOUND_POTPLAYER64_DPL)
        if not LTA:
            ensure_command_excuted_to_os(cmd=rf'explorer "{get_p(F_PKG_IMAGE_AND_VIDEO_AND_SOUND_POTPLAYER64_DPL)}" ') # pk_option
        ensure_command_excuted_to_os(cmd=rf'explorer "{F_PKG_IMAGE_AND_VIDEO_AND_SOUND_POTPLAYER64_DPL}" ')
    elif is_os_linux():
        # Linux에서는 기본 오디오 플레이어 사용
        try:
            # 다양한 오디오 플레이어 시도
            players = ['vlc', 'mpv', 'mplayer', 'ffplay']
            for player in players:
                try:
                    ensure_command_excuted_to_os(cmd=f'{player} --help', mode='sync')
                    ensure_printed(f" {player}로 오디오 재생을 시도합니다.")
                    # 여기서 실제 오디오 파일 경로를 지정해야 함
                    # ensure_command_excuted_to_os(cmd=f'{player} /path/to/audio/file.mp3')
                    break
                except:
                    continue
            else:
                ensure_printed("️ 사용 가능한 오디오 플레이어를 찾을 수 없습니다.")
        except Exception as e:
            ensure_printed(f" 오디오 재생 실패: {e}")
    else:
        # macOS에서는 afplay 사용
        try:
            ensure_command_excuted_to_os(cmd='afplay --help', mode='sync')
            # ensure_command_excuted_to_os(cmd='afplay /path/to/audio/file.mp3')
        except Exception as e:
            ensure_printed(f" 오디오 재생 실패: {e}")
