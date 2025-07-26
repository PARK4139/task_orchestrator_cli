

def print_pk_ver():
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_printed import ensure_printed

    if LTA:
        ensure_printed(f'''{'%%%FOO%%%' if LTA else ''}''')
    print('pk_ver.1.32.12')
