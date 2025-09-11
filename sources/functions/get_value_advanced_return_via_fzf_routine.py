def get_value_advanced_return_via_fzf_routine(file_id, editable, options=[]):
    import logging

    from sources.functions.get_f_historical import ensure_history_file_pnx_return
    from sources.functions.get_list_calculated import get_list_calculated
    from sources.functions.get_value_advanced_return_via_fzf import get_value_advanced_return_via_fzf
    from sources.functions.get_values_from_historical_file import get_values_from_history_file
    from sources.functions.set_values_to_historical_file import set_values_to_historical_file
    from sources.objects.pk_local_test_activate import LTA

    if options == [""]:
        options = []
    # first call 에서 options에 값을 넣고, 이후 호출부터는 init_options = [] 로 해야함, 계속 값이 더해짐
    f_historical = ensure_history_file_pnx_return(file_id=file_id)
    historical_values = get_values_from_history_file(f_historical=f_historical)
    options = get_list_calculated(origin_list=options, plus_list=historical_values)
    logging.debug(f'''options={options} {'%%%FOO%%%' if LTA else ''}''')
    options = get_list_calculated(origin_list=options, dedup=True)

    # prompt_label = get_prompt_label(file_id)
    # prompt_label_guide_ment = get_prompt_label_guide_ment(prompt_label)
    # easy_speakable_prompt_label = get_easy_speakable_text(prompt_label_guide_ment)
    # ensure_spoken(easy_speakable_prompt_label, verbose=False)

    selected = get_value_advanced_return_via_fzf(file_id=file_id, options=options, editable=editable)

    logging.debug(f'''selected={selected} {'%%%FOO%%%' if LTA else ''}''')
    selected = selected.strip()
    options = get_list_calculated(origin_list=[selected], plus_list=options)  # 선택값을 맨 앞으로 정렬
    options = get_list_calculated(origin_list=options, dedup=True)
    set_values_to_historical_file(f_historical=f_historical, values=options)
    return selected
