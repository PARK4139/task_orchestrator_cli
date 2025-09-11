

def ensure_applications_killed(task_orchestrator_cli_application_killing_mode = True):
    from sources.functions.ensure_gemini_cli_killed import ensure_gemini_cli_killed
    from sources.functions.ensure_losslescut_killed import ensure_losslescut_killed
    from sources.functions.ensure_windows_killed_like_human import ensure_windows_killed_like_human

    from sources.objects.pk_local_test_activate import LTA

    from sources.functions.ensure_cmd_exe_killed import ensure_cmd_exe_killed
    from sources.functions.ensure_wrappers_killed import ensure_wrappers_killed
    from sources.functions.ensure_potplayer_killed import ensure_potplayer_killed
    from sources.functions.ensure_windows_deduplicated import \
        ensure_windows_deduplicated
    from sources.functions.ensure_process_killed_by_image_name import ensure_process_killed_by_image_name
    from sources.functions.ensure_windows_printed import ensure_windows_printed

    if LTA:
        ensure_windows_printed()
        # ensure_slept(minutes=1)

    ensure_potplayer_killed()
    ensure_losslescut_killed()
    ensure_process_killed_by_image_name('chrome.exe')
    ensure_process_killed_by_image_name('code.exe')
    ensure_process_killed_by_image_name('cursor.exe')
    ensure_gemini_cli_killed()
    ensure_cmd_exe_killed()
    ensure_windows_deduplicated()

    if task_orchestrator_cli_application_killing_mode:
        ensure_process_killed_by_image_name('pycharm64.exe') # task_orchestrator_cli_optioni
        # ensure_wrappers_killed()  # execute last # 프로세스 자기 자신 죽여서 수행불가 상태로 만듬.
