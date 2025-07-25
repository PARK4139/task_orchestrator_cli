def get_value_via_fzf_or_history_routine(key_name, file_id, editable, init_options=[]):
    from pkg_py.functions_split.get_f_historical import get_history_file
    from pkg_py.functions_split.get_list_calculated import get_list_calculated
    from pkg_py.functions_split.get_value_via_fzf_or_history import get_value_via_fzf_or_history
    from pkg_py.functions_split.get_values_from_historical_file import get_values_from_history_file
    from pkg_py.functions_split.print import pk_print
    from pkg_py.functions_split.set_values_to_historical_file import set_values_to_historical_file
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025

    # first call 에서 options에 값을 넣고, 이후 호출부터는 init_options = [] 로 해야함, 계속 값이 더해짐
    f_historical = get_history_file(file_id=file_id)
    historical_values = get_values_from_history_file(f_historical=f_historical)
    init_options = get_list_calculated(origin_list=init_options, plus_list=historical_values)
    pk_print(f'''[{PkMessages2025.DATA}] options={init_options} {'%%%FOO%%%' if LTA else ''}''')
    init_options = get_list_calculated(origin_list=init_options, dedup=True)
    selected = get_value_via_fzf_or_history(key_name=key_name, file_id=file_id, options=init_options, editable=editable)
    selected = selected.strip()
    init_options = get_list_calculated(origin_list=[selected], plus_list=init_options)  # 선택값을 맨 앞으로 정렬
    init_options = get_list_calculated(origin_list=init_options, dedup=True)
    set_values_to_historical_file(f_historical=f_historical, values=init_options)
    return selected
