from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.files import F_PKG_SOUND_POTPLAYER64_DPL


def play_my_sound_track():
    import inspect

    func_n = inspect.currentframe().f_code.co_name

    # cmd_to_os(cmd=rf'taskkill /f /im "alsong.exe" ', debug_mode=True)

    cmd_to_os(cmd=rf'explorer "{F_PKG_SOUND_POTPLAYER64_DPL}" ')
