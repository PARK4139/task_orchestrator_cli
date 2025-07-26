def test_get_value_with_tab_v90():
    from pkg_py.functions_split.get_file_id import get_file_id
    # user input history, autocomplete, fzf, history file
    key_name = 'f_working'
    func_n = inspect.currentframe().f_code.co_name
    file_id = get_file_id(key_name, func_n)
    # editable = False
    editable = True
    init_options = [F_PK_WORKSPACE_PY]
    value = get_value_via_fzf_or_history_routine(key_name=key_name, file_id=file_id, init_options=init_options, editable=editable)
    f_working = value
    ensure_printed(f'''f_working={f_working} {'%%%FOO%%%' if LTA else ''}''')


