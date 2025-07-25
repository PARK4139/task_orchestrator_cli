def get_value_via_fzf_or_history(key_name, file_id, options, editable=False):
    from pkg_py.functions_split.get_value_from_fzf_routine import get_value_from_fzf_routine
    from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
    from pkg_py.system_object.map_massages import PkMessages2025
    # decision = get_value_completed(key_hint=rf"{key_name}=", values=[PkMessages2025.VIA_FZF, PkMessages2025.VIA_HISTORICAL_FILE]) # pk_option
    decision = PkMessages2025.VIA_FZF  # pk_option
    if decision == PkMessages2025.VIA_FZF:
        selected_value = get_value_from_fzf_routine(file_id=file_id, options=options, editable=editable)
        return selected_value
    elif decision == PkMessages2025.VIA_HISTORICAL_FILE:
        selected_value = get_values_from_historical_file_routine(file_id=file_id, key_hint=f'{key_name}=', options_default=options, editable=editable)
        return selected_value
    else:
        selected_value = decision
        return selected_value
