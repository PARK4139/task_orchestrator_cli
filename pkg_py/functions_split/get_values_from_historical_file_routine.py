from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
from pkg_py.functions_split.get_f_historical import get_f_historical


def get_values_from_historical_file_routine(file_id: str, key_hint: str, values_default=[], editable=False) -> str:
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.functions_split.get_list_calculated import get_list_calculated
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
    from pkg_py.functions_split.set_values_to_historical_file import set_values_to_historical_file
    from pkg_py.functions_split.get_values_from_historical_file import get_values_from_historical_file
    f_historical = get_f_historical(file_id=file_id)
    if LTA:
        pk_print(f'''f_historical={f_historical} {'%%%FOO%%%' if LTA else ''}''')
    ensure_pnx_made(pnx=f_historical, mode='f')
    if editable == True:
        ensure_pnx_opened_by_ext(pnx=f_historical)
        ensure_window_to_front(window_title_seg=get_nx(f_historical))
    values_optional = get_list_calculated(origin_list=values_default,plus_list=get_values_from_historical_file(f_historical=f_historical))
    value_selected = get_value_completed(key_hint=key_hint, values=values_optional)
    values_optional = get_list_calculated(origin_list=values_optional, plus_list=[value_selected])
    set_values_to_historical_file(f_historical=f_historical, values=values_optional)
    return value_selected
