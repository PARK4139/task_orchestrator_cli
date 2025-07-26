from pkg_py.functions_split.ensure_printed import ensure_printed


def ensure_state_printed(state, pk_id, state_header=None):
    from pkg_py.system_object.local_test_activate import LTA
    if state_header is not None:
        ensure_printed(f'''{state_header} {f'{pk_id}' if LTA else ''}''', print_color='green')
    ensure_printed(f'''{state} {f'{pk_id}' if LTA else ''}''', print_color='green')
