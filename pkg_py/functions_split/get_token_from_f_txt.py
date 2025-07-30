def get_token_from_f_txt(f_token, initial_str):
    from pkg_py.functions_split.generate_token_f import generate_token_f
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_str_from_txt_f import get_str_from_txt_f
    f_token = get_pnx_os_style(f_token)
    generate_token_f(f=f_token, initial_str=initial_str)
    token = get_str_from_txt_f(pnx=f_token)
    token = token.replace("\n", "")
    return token
