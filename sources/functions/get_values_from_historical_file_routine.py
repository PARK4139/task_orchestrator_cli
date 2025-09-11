def get_values_from_historical_file_routine(file_id: str, key_hint: str, options_default=[], editable=False) -> str:
    from sources.functions import is_pnx_existing
    from sources.functions.is_window_opened import is_window_opened

    from sources.functions.get_f_historical import ensure_history_file_pnx_return
    from sources.functions.get_nx import get_nx
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    from sources.objects.pk_local_test_activate import LTA
    from sources.functions.ensure_pnx_made import ensure_pnx_made
    from sources.functions.ensure_value_completed import ensure_value_completed
    from sources.functions.get_list_calculated import get_list_calculated
    import logging
    from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
    from sources.functions.set_values_to_historical_file import set_values_to_historical_file
    from sources.functions.get_values_from_historical_file import get_values_from_history_file
    history_file = ensure_history_file_pnx_return(file_id=file_id)
    if LTA:
        logging.debug(f'''history_file={history_file} {'%%%FOO%%%' if LTA else ''}''')
    if not is_pnx_existing(history_file):
        ensure_pnx_made(pnx=history_file, mode='f')

    if editable == True:
        if not is_window_opened(window_title_seg=history_file):
            ensure_pnx_opened_by_ext(pnx=history_file)
            ensure_window_to_front(get_nx(history_file))
    options = get_list_calculated(origin_list=options_default, plus_list=get_values_from_history_file(f_historical=history_file))
    selected = ensure_value_completed(key_hint=key_hint, options=options)
    options = get_list_calculated(origin_list=[selected], plus_list=options)
    set_values_to_historical_file(f_historical=history_file, values=options)
    return selected
