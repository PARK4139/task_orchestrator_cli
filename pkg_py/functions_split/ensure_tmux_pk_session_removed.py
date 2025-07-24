

def ensure_tmux_pk_session_removed(tmux_pk_session):
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.cmd_to_os import cmd_to_os
    from pkg_py.functions_split.pk_print import pk_print

    if LTA:
        pk_print(f'''pk_session_n={tmux_pk_session} {'%%%FOO%%%' if LTA else ''}''')
    for std_str in cmd_to_os(f'tmux ls'):
        if tmux_pk_session in std_str:
            cmd_to_os(f'tmux kill-session -t {tmux_pk_session}')
