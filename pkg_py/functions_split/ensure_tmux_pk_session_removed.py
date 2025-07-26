

def ensure_tmux_pk_session_removed(tmux_pk_session):
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.ensure_printed import ensure_printed

    if LTA:
        ensure_printed(f'''pk_session_n={tmux_pk_session} {'%%%FOO%%%' if LTA else ''}''')
    for std_str in ensure_command_excuted_to_os(f'tmux ls'):
        if tmux_pk_session in std_str:
            ensure_command_excuted_to_os(f'tmux kill-session -t {tmux_pk_session}')
