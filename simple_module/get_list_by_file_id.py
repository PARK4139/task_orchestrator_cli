def get_list_by_file_id(file_id, editable=False):
    from pkg_py.pk_system_layer_100_Local_test_activate import LTA
    from pkg_py.pk_system_layer_encodings import Encoding
    from pkg_py.simple_module.get_f_historical import get_f_historical
    from pkg_py.simple_module.part_001_ensure_pnx_made import ensure_pnx_made
    from pkg_py.simple_module.part_014_pk_print import pk_print
    from pkg_py.simple_module.part_016_open_pnx_by_ext import ensure_pnx_opened_by_ext
    import os
    import traceback
    f_historical = get_f_historical(file_id)
    f = f_historical
    ensure_pnx_made(pnx=f_historical, mode='f')
    if editable == True:
        ensure_pnx_opened_by_ext(pnx=f_historical)
    pk_print(f'''f={f}''')

    if f is None:
        return []

    try:
        if os.path.exists(f):
            with open(file=f, mode='r', encoding=Encoding.UTF8.value, errors='ignore') as f_obj:
                lines = f_obj.readlines()
                if lines is None:
                    return []
                return lines
    except:
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''', print_color='red')


