from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.directories  import D_PROJECT
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_value_completed import get_value_completed


def assist_to_ensure_files_organized_by_nx_delimiter():
    from colorama import init as pk_colorama_init

    ensure_colorama_initialized_once()

    option_values = [D_PK_WORKING, D_PROJECT, D_DOWNLOADS]
    while 1:
        d_working = get_value_completed(key_hint='d_working=', values=option_values)
        option_values.append(d_working)
        option_values = get_list_deduplicated(working_list=option_values)
        word_set = get_word_set_from_f_list(d_working=d_working)
        word_list = get_list_from_set(working_set=word_set)
        word_list = get_list_unioned(list_a=word_list, list_b=['seg', 'SEG'])
        word_list = get_list_sorted(working_list=word_list)
        nx_delimiter = get_value_completed(key_hint='nx_delimiter=', values=word_list)
        # for nx_delimiter in range(2000,2024):
        #     organize_f_list_by_nx_delimiter(nx_delimiter=str(nx_delimiter), d_working=d_working)
        pk_organize_f_list_by_nx_delimiter(nx_delimiter=nx_delimiter, d_working=d_working)
