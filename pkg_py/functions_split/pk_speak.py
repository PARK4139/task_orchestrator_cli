import ipdb

from pkg_py.functions_split.is_internet_connected import is_internet_connected
from pkg_py.workspace.pk_workspace import pk_speak_v3, ensure_this_code_operated


def pk_speak(working_str, after_delay=1.00, delimiter=None):
    if not is_internet_connected():
        return
    # pk_speak_v1(working_str=working_str, after_delay=after_delay, delimiter=delimiter)
    # pk_speak_v2(working_str=working_str, comma_delay=after_delay)
    pk_speak_v3(working_str=working_str, segment_delay=after_delay)
    # ensure_this_code_operated(ipdb)
