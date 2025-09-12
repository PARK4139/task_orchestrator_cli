from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_value_completed_advanced(key_name, func_n, editable=False, options=None):
    import logging

    from functions.ensure_spoken import ensure_spoken
    from functions.get_easy_speakable_text import get_easy_speakable_text
    from functions.get_prompt_label import get_prompt_label
    from functions.get_prompt_label_guide_text import get_prompt_label_guide_text
    from sources.functions.get_f_historical import ensure_history_file_pnx_return
    from sources.functions.get_file_id import get_file_id
    from sources.functions.get_last_selected import get_last_selected
    from sources.functions.get_list_calculated import get_list_calculated
    from sources.functions.get_numbered_items import get_numbered_items
    from sources.functions.get_remove_numbered_item import get_remove_numbered_item
    from sources.functions.get_value_advanced_return_via_fzf import get_value_advanced_return_via_fzf
    from sources.functions.get_values_from_historical_file import get_values_from_history_file
    from sources.functions.set_values_to_historical_file import set_values_to_historical_file
    from sources.objects.pk_local_test_activate import LTA
    file_id = get_file_id(key_name, func_n)

    prompt_label = get_prompt_label(file_id)
    prompt_label_guide_ment = get_prompt_label_guide_text(prompt_label)
    easy_speakable_prompt_label = get_easy_speakable_text(prompt_label_guide_ment)
    # ensure_spoken(easy_speakable_prompt_label, verbose=False)

    options = options or []
    if options == [""]:
        options = []

    f_historical = ensure_history_file_pnx_return(file_id=file_id)
    historical_values = get_values_from_history_file(f_historical=f_historical)
    options = get_list_calculated(origin_list=options, plus_list=historical_values)
    logging.debug(f'''file_id={file_id} {'''%%%FOO%%% ''' if LTA else ''}''')

    options = get_list_calculated(origin_list=options, dedup=True)

    last_selected = get_last_selected(f_historical)
    logging.debug(f'''last_selected={last_selected} {'''%%%FOO%%% ''' if LTA else ''}''')

    if last_selected.strip() != "":
        options = get_list_calculated(origin_list=[last_selected], plus_list=options)

    numbered_options = get_numbered_items(options)
    numbered_selected = get_value_advanced_return_via_fzf(
        file_id=file_id,
        options=numbered_options,
        editable=editable,
        query=last_selected
    )

    selected = get_remove_numbered_item(numbered_selected)
    selected = selected.strip()
    logging.debug(f'''selected={selected}''')

    if selected:  # Add this conditional check
        options = get_list_calculated(origin_list=[selected], plus_list=options)
    options = get_list_calculated(origin_list=options, dedup=True)
    logging.debug(f'''len(options)={len(options)} {'''%%%FOO%%% ''' if LTA else ''}''')

    set_values_to_historical_file(f_historical=f_historical, values=options)
    return selected
