
def pk_ensure_loop_delayed_at_loop_foot(loop_cnt, mode_level, miliseconds_limit=10000):
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025
if LTA:
if loop_cnt == 1:
if mode_level == 1:  # strict level
if mode_level == 2:
if mode_level == 3:  # natural operation
input(PkMessages2025.IF_YOU_WANT_MORE_PRESS_ENTER)
pk_sleep(milliseconds=miliseconds_limit)
print(rf"[{PkMessages2025.WAITING}] {miliseconds_limit}{PkMessages2025.MILLISECONDS}")
