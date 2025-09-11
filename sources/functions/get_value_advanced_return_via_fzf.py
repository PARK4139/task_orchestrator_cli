def get_value_advanced_return_via_fzf(file_id, options, editable=False, query=""):
    from sources.functions.get_value_from_fzf_routine import get_value_from_fzf_routine

    selected_value = get_value_from_fzf_routine(file_id=file_id, options=options, editable=editable, query=query)
    return selected_value
