def ensure_spoken(str_working, after_delay=1.00, delimiter=None):
    from pkg_py.functions_split.is_internet_connected import is_internet_connected
    from pkg_py.functions_split.speak_v3 import speak_v3
    if not is_internet_connected():
        return
    # ensure_spoken_v1(str_working=str_working, after_delay=after_delay, delimiter=delimiter)
    # ensure_spoken_v2(str_working=str_working, comma_delay=after_delay)
    ensure_spoken_v3(str_working=str_working, segment_delay=after_delay)
    # ensure_this_code_operated(ipdb)
