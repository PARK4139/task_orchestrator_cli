from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_etc import PK_UNDERLINE
from pkg_py.simple_module.part_004_print_red import print_red
from pkg_py.simple_module.part_836_ensure_console_debuggable import ensure_console_debuggable


def ensure_do_exception_routine(traceback, exception):
    # from pkg_py.pk_system_layer_800_print_util import print_red
    #
    print_red(PK_UNDERLINE)
    # for line in traceback.format_exception_only(type(exception), exception):
    #     print_red(f"{STAMP_UNIT_TEST_EXCEPTION_DISCOVERED} {line.strip()}")
    print_red(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''')
    if LTA:
        ensure_console_debuggable()
