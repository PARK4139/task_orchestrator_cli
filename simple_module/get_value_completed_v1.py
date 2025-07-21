

def get_value_completed_v1(message, option_values):
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter
    deduplicated_option_values = option_values
    deduplicated_option_values = [get_pnx_os_style(f) for f in deduplicated_option_values]
    deduplicated_option_values = list(set(deduplicated_option_values))
    deduplicated_option_values = get_list_sorted(working_list=deduplicated_option_values, mode_asc=1)
    completer = WordCompleter(deduplicated_option_values)
    pk_input = prompt(message, completer=completer)
    return pk_input


