from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_330_get_d_working import get_d_working


def update_if_changed(prev_cnt):
    d_working = get_d_working()
    import os
    current_cnt = len(os.listdir(d_working))
    delta_cnt = current_cnt - prev_cnt
    if delta_cnt != 0:
        pk_print(f"f_cnt is not stable → update list ({prev_cnt}->{current_cnt}({delta_cnt}))", print_color='blue')
        return True, current_cnt
    pk_print(f"f_cnt is stable")
    return False, prev_cnt
