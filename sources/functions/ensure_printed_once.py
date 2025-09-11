

def ensure_printed_once(msg):
    import os.path

    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
    from sources.functions.load_logged_set import load_logged_set
    from sources.functions.save_logged_set import save_logged_set
    import logging

    # 프로그램초기실행완료여부 pickle 에 저장  -> 프로그램초기실행완료여부==False 면 출력
    # 프로그램초기 1회 만 동작
    file_id = "state_about_ensure_printed_once"
    f_pkl = os.path.join(D_TASK_ORCHESTRATOR_CLI_SENSITIVE, f'{file_id}.pkl')
    logged_set = load_logged_set(f_pkl)
    if msg in logged_set:
        return
    logging.debug(msg)
    logged_set.add(msg)
    save_logged_set(logged_set, f_pkl)
