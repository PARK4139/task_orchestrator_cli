from pkg_py.functions_split.get_list_from_f import get_list_from_f
from pkg_py.system_object.etc import PK_UNDERLINE


def ensure_memo_titles_printed(f):
    # todo
    from pkg_py.functions_split.get_line_list_to_include_search_keyword import get_line_list_to_include_search_keyword
    from pkg_py.functions_split.get_list_removed_element_startswith_str import get_list_removed_element_startswith_str
    from pkg_py.functions_split.get_str_from_list import get_str_from_list
    from pkg_py.functions_split.print_highlighted import print_highlighted
    from pkg_py.system_object.local_test_activate import LTA

    # lines_list = get_line_list_to_include_search_keyword(f=f, search_keywords=["[todo]"])
    # lines_list = get_list_removed_element_startswith_str(working_list=lines_list, string="#")
    # liens_str = get_str_from_list(working_list=lines_list, item_connector='')

    lines_list = get_list_from_f(f=f)
    lines_list = get_list_removed_element_startswith_str(working_list=lines_list, string=rf"{PK_UNDERLINE}")

    highlight_config_dict = {
        "bright_red": [
            f'{' %%%FOO%%% ' if LTA else ''}',
        ],
        "white": [
            rf"{PK_UNDERLINE}",
        ],
    }
    for line in lines_list:
        print_highlighted(txt_whole=line, highlight_config_dict=highlight_config_dict)
