from pkg_py.simple_module.pk_press_v2 import pk_press_v2


def pk_press(*presses: str, interval=0.0):
    # return pk_press_v1(*presses, interval=interval)
    return pk_press_v2(*presses, interval=interval)
