def pk_get_colorful_str_working_with_stamp_enviromnet(func_n, ment=""):
    highlight_config_dict = {
        "blue": [
            STAMP_PK_ENVIRONMENT_WITHOUT_BRAKET
        ],
        "green": [
            func_n
        ],
        "white": [
            ment
        ],
    }
    return get_txt_highlighted(txt_whole=rf'({STAMP_PK_ENVIRONMENT_WITHOUT_BRAKET}) ({func_n}) {ment}',
                               config_highlight_dict=highlight_config_dict)
