import requests
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT

from collections import Counter
from pkg_py.simple_module.part_482_assist_to_load_video_at_losslesscut import pk_ensure_video_loaded_at_losslesscut


def open_recycle_bin():
    cmd_to_os(cmd='explorer.exe shell:RecycleBinFolder')
