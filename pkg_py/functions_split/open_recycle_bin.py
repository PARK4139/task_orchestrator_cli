import requests
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.directories_reuseable import D_PROJECT

from collections import Counter
from pkg_py.functions_split.ensure_video_loaded_at_losslesscut import ensure_video_loaded_at_losslesscut


def open_recycle_bin():
    ensure_command_excuted_to_os(cmd='explorer.exe shell:RecycleBinFolder')
