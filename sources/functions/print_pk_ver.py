

def print_pk_ver():
    from sources.objects.pk_local_test_activate import LTA
    import logging

    if LTA:
        logging.debug(f'''{'%%%FOO%%%' if LTA else ''}''')
    print('pk_ver.1.32.12')
