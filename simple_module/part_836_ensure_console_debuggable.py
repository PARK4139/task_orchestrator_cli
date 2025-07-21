from pkg_py.simple_module.part_004_print_red import print_red
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep


def ensure_console_debuggable():
    print_red(f"[ PK DEBUGER WORKED ]")
    pk_sleep(hours=1, mode_countdown=0)
