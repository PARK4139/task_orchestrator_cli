

def pk_ensure_loop_delayed_at_loop_foot(loop_cnt, mode_level, miliseconds_limit=10000):
    from pkg_py.pk_system_object.map_massages import PkMessages2025
    
    from pkg_py.pk_system_object.local_test_activate import LTA
    if mode_level == 1:  # strict level
        if LTA:
            input(PkMessages2025.IF_YOU_WANT_MORE_PRESS_ENTER)
    if mode_level == 2:
        print(rf"[{PkMessages2025.WAITING}] {miliseconds_limit}{PkMessages2025.MILLISECONDS}")
        pk_sleep(milliseconds=miliseconds_limit)
    if mode_level == 3:  # natural operation
        if loop_cnt == 1:
            input(PkMessages2025.IF_YOU_WANT_MORE_PRESS_ENTER)


