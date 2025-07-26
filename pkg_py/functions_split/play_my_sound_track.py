from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.files import F_PKG_SOUND_POTPLAYER64_DPL


def play_my_sound_track():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    # ensure_command_excuted_to_os(cmd=rf'taskkill /f /im "alsong.exe" ', debug_mode=True)
    ensure_command_excuted_to_os(cmd=rf'explorer "{F_PKG_SOUND_POTPLAYER64_DPL}" ')
