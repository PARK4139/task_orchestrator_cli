def ensure_do_exception_routine(traceback, exception):
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.pk_system_object.etc import PK_UNDERLINE
    from pkg_py.functions_split.ensure_console_debuggable import ensure_console_debuggable
    from pkg_py.functions_split.print_red import print_red
    print_red(PK_UNDERLINE)
    print_red(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''')
    if LTA:
        ensure_console_debuggable()
