def pk_speak(str_working, after_delay=1.00, delimiter=None):
    from pkg_py.functions_split.is_internet_connected import is_internet_connected
    from pkg_py.functions_split.speak_v3 import pk_speak_v3
    if not is_internet_connected():
        return
    # pk_speak_v1(str_working=str_working, after_delay=after_delay, delimiter=delimiter)
    # pk_speak_v2(str_working=str_working, comma_delay=after_delay)
    pk_speak_v3(str_working=str_working, segment_delay=after_delay)
    # ensure_this_code_operated(ipdb)
