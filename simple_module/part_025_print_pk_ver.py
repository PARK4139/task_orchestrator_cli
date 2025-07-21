

def print_pk_ver():
    from pkg_py.pk_system_layer_100_Local_test_activate import LTA
    from pkg_py.simple_module.part_014_pk_print import pk_print

    if LTA:
        pk_print(f'''{'%%%FOO%%%' if LTA else ''}''')
    print('pk_ver.1.32.12')
