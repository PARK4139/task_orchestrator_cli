import requests
from pkg_py.functions_split.cmd_to_os import cmd_to_os
from pkg_py.system_object.directories_reuseable import D_PROJECT

from collections import Counter
from pkg_py.functions_split.assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut


def open_recycle_bin():
    cmd_to_os(cmd='explorer.exe shell:RecycleBinFolder')
