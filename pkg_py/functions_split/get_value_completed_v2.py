

def get_value_completed_v2(message, option_values):
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    if message.strip() == "x":
        ensure_spoken(f"{func_n}() exited(intended)")

    seen = set()
    if is_os_wsl_linux():

        # cmd_to_run = None
        # cmd = None
        # if pk_arg_list is None:
        #     pk_arg_list = []
        # available_pk_python_program_pnx = get_available_pk_python_program_pnx(pk_idx)
        # cmd_to_run = 'uv run python'
        # cmd_to_run = 'python'
        # tmux_session = get_nx(available_pk_python_program_pnx).replace(".", "_")
        # ensure_tmux_pk_session_removed(tmux_session)

        # if os.environ.get("TMUX"):
        #     # 수직 분할: -v, 수평 분할: -h 로 바꿀 수 있음
        #     split_flag = "-v"
        #     # LTA 모드라면 끝에 sleep 추가
        #     sleep_cmd = "; sleep 99999" if LTA else ""
        #     ensure_command_excuted_to_os(cmd=(
        #         f"tmux split-window {split_flag} "
        #         f"'clear && {cmd_to_run} {available_pk_python_program_pnx}{sleep_cmd}'"
        #     ))
        #     return

        # tmux_session = get_nx(available_pk_python_program_pnx).replace(".", "_")
        # ensure_tmux_pk_session_removed(tmux_session)

        # ensure_command_excuted_to_os(cmd=(
        #     f"tmux new-session -s {tmux_session} -d "
        #     f"'clear && {cmd_to_run} {available_pk_python_program_pnx}'"
        # ))
        # ensure_command_excuted_to_os(cmd=(
        #     f"tmux split-window -v -t {tmux_session} "
        #     f"'clear && {cmd_to_run} {available_pk_python_program_pnx}'"
        # ))
        # ensure_command_excuted_to_os(cmd=f"tmux attach-session -t {tmux_session}")

        # deduped = ensure_command_excuted_to_os('fzf') + []
        deduped = []
    else:
        deduped = []

    # 1) get_pnx_os_style 적용 + 중복 제거 (원본 순서 유지)
    for item in option_values:
        styled = item
        if isinstance(item, str):
            if is_path_like(item):
                styled = get_pnx_os_style(item)
        if styled not in seen:
            seen.add(styled)
            deduped.append(styled)

    # 2) 필요하면 정렬
    # deduped = get_list_sorted(working_list=deduped, mode_asc=1)

    # 3) WordCompleter에 넘겨서 프롬프트 실행
    completer = WordCompleter(deduped)
    return prompt(message, completer=completer)





