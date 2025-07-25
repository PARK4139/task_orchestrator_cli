
#     organize_f_list_by_nx_delimiter(nx_delimiter=str(nx_delimiter), d_working=d_working)
# for nx_delimiter in range(2000,2024):
d_working = get_value_completed(key_hint='d_working=', values=option_values)
def pk_assist_to_ensure_f_list_organized_by_nx_delimiter():
from colorama import init as pk_colorama_init
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
nx_delimiter = get_value_completed(key_hint='nx_delimiter=', values=word_list)
option_values = [D_WORKING, D_PROJECT, D_DOWNLOADS]
option_values = get_list_deduplicated(working_list=option_values)
option_values.append(d_working)
pk_colorama_init_once()
pk_organize_f_list_by_nx_delimiter(nx_delimiter=nx_delimiter, d_working=d_working)
while 1:
word_list = get_list_from_set(working_set=word_set)
word_list = get_list_sorted(working_list=word_list)
word_list = get_list_unioned(list_a=word_list, list_b=['seg', 'SEG'])
word_set = get_word_set_from_f_list(d_working=d_working)
