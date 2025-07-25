
# editable = False
# user input history, autocomplete, fzf, history file
def pk_test_get_value_with_tab_v90():
editable = True
f_working = value
file_id = get_file_id(key_name, func_n)
from pkg_py.functions_split.get_file_id import get_file_id
func_n = inspect.currentframe().f_code.co_name
init_options = [F_PK_WORKSPACE_PY]
key_name = 'f_working'
pk_print(f'''f_working={f_working} {'%%%FOO%%%' if LTA else ''}''')
value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
