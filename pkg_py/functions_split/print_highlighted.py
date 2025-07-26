

def print_highlighted(txt_whole, highlight_config_dict):
    from colorama import init as pk_colorama_init
    colorama_init_once()
    print(get_txt_highlighted(txt_whole, highlight_config_dict))
