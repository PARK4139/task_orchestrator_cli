def get_list_by_file_id(file_id, editable=False):
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.encodings import Encoding
    from sources.functions.get_f_historical import ensure_history_file_pnx_return
    from sources.functions.ensure_pnx_made import ensure_pnx_made
    import logging
    from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
    import os
    import traceback
    f_historical = ensure_history_file_pnx_return(file_id)
    f = f_historical
    ensure_pnx_made(pnx=f_historical, mode='f')
    if editable == True:
        ensure_pnx_opened_by_ext(pnx=f_historical)
    logging.debug(f'''f={f}''')

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
        logging.debug(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}" ''')


