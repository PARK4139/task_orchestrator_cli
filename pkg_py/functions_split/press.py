
# return pk_press_v1(*presses, interval=interval)
def pk_press(*presses: str, interval=0.0):
from pkg_py.functions_split.press_v2 import pk_press_v2
return pk_press_v2(*presses, interval=interval)
