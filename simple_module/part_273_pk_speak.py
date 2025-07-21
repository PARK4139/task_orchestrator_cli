def pk_speak(working_str, after_delay=1.00, delimiter=None):
    from pkg_py.simple_module.part_002_is_internet_connected import is_internet_connected
    from pkg_py.simple_module.part_272_pk_speak_v2 import pk_speak_v2
    if is_internet_connected():
        # pk_speak_v1(working_str=working_str, after_delay=after_delay, delimiter=delimiter)
        pk_speak_v2(working_str=working_str, comma_delay=after_delay)
