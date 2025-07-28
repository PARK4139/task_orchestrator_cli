def ensure_sound_track_played():
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.system_object.files import F_PKG_SOUND_POTPLAYER64_DPL

    import inspect
    func_n = inspect.currentframe().f_code.co_name
    # ensure_command_excuted_to_os(cmd=rf'taskkill /f /im "alsong.exe" ', debug_mode=True)
    F_PKG_SOUND_POTPLAYER64_DPL = get_pnx_os_style(F_PKG_SOUND_POTPLAYER64_DPL)
    ensure_command_excuted_to_os(cmd=rf'explorer "{F_PKG_SOUND_POTPLAYER64_DPL}" ')
