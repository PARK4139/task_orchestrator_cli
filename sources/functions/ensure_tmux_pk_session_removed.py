

def ensure_tmux_pk_session_removed(tmux_pk_session):
    from sources.objects.pk_local_test_activate import LTA
    from sources.functions.ensure_command_executed import ensure_command_executed
    import logging

    if LTA:
        logging.debug(f'''pk_session_n={tmux_pk_session} {'%%%FOO%%%' if LTA else ''}''')
    for std_str in ensure_command_executed(f'tmux ls'):
        if tmux_pk_session in std_str:
            ensure_command_executed(f'tmux kill-session -t {tmux_pk_session}')
