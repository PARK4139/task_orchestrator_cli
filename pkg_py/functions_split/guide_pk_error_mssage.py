

from pkg_py.functions_split.pk_measure_seconds import pk_measure_seconds


@pk_measure_seconds
def guide_pk_error_mssage():
    from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.functions_split.pk_print import pk_print
    pk_print(f'''{PkMessages2025.NOT_PREPARED_YET}{'%%%FOO%%%' if LTA else ''}''', print_color='green', mode_verbose=0)
