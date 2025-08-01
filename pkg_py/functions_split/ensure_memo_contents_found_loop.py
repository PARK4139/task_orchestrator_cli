def ensure_memo_contents_found_loop():
    from pkg_py.functions_split.common_imports import ensure_console_cleared, ensure_memo_contents_found, ensure_pk_system_exit_silent, ensure_printed
    loop_cnt = 1
    user_input = None
    while True:
        if loop_cnt == 1:
            loop_cnt += 1
        else:
            user_input = input("\n계속 검색하려면 Enter, 종료하려면 'x' 입력: ").strip().lower()
            loop_cnt += 1
        if user_input in ("q", "quit", "exit", "x"):
            ensure_printed("검색 반복을 종료합니다.", print_color="yellow")
            ensure_pk_system_exit_silent()
            break
        try:
            ensure_console_cleared()
            ensure_memo_contents_found()
        except Exception as e:
            ensure_printed(f"검색 중 오류 발생: {e}", print_color="red")
