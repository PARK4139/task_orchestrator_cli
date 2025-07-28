def print_highlighted(txt_whole, highlight_config_dict):
    from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
    from pkg_py.functions_split.get_txt_highlighted import get_txt_highlighted
    ensure_colorama_initialized_once()
    print(get_txt_highlighted(txt_whole, highlight_config_dict))
