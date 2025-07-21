def get_str_from_txt_f(pnx):
    prompt = ""
    lines = get_list_from_f(f=pnx)
    lines = get_list_without_none(working_list=lines)
    for line in lines:
        prompt = prompt + line + "\n"
    return prompt
