

def print_pk_ver():
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.pk_print import pk_print

    if LTA:
        pk_print(f'''{'%%%FOO%%%' if LTA else ''}''')
    print('pk_ver.1.32.12')
