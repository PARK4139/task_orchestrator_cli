

def pk_print_state(state, pk_id, state_header=None):
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.functions_split.pk_print import pk_print
    if state_header is not None:
        pk_print(f'''{state_header} {f'{pk_id}' if LTA else ''}''', print_color='green')
    pk_print(f'''{state} {f'{pk_id}' if LTA else ''}''', print_color='green')
