# return pk_press_v1(*presses, interval=interval)
def press(*presses: str, interval=0.0):
    from pkg_py.functions_split.press_v2 import press_v2
    return pk_press_v2(*presses, interval=interval)
