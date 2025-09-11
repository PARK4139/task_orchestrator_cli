from functions.ensure_seconds_measured import ensure_seconds_measured
from objects.pk_target_manager import SetupOps


@ensure_seconds_measured
def ensure_routine_startup_enabled():
    from functions.ensure_guided_not_prepared_yet import ensure_not_prepared_yet_guided
    from functions.is_pc_asus import is_pc_asus
    from functions.is_pc_renova import is_pc_renova
    from objects.device_identifiers import PkDeviceIdentifiers
    from objects.pk_target_manager import PkTargetManager
    from sources.functions import ensure_slept
    from sources.functions.ensure_chatgpt_opened import ensure_chatgpt_opened
    from sources.functions.ensure_cursor_enabled import ensure_cursor_enabled
    from sources.functions.ensure_memo_editable import ensure_memo_editable
    from sources.functions.ensure_pycharm_opened import ensure_pycharm_opened
    from sources.functions.ensure_remote_pc_controllable_via_chrome_remote_desktop import ensure_remote_pc_controllable_via_chrome_remote_desktop
    from sources.functions.ensure_sound_track_played import ensure_sound_track_played
    from sources.functions.ensure_vscode_enabled import ensure_vscode_enabled
    from sources.functions.ensure_windows_minimized import ensure_windows_minimized

    pk_tm = PkTargetManager(identifier=PkDeviceIdentifiers.device_asus_desktop, setup_ops=SetupOps.WSL)

    if is_pc_renova():
        ensure_memo_editable()
        ensure_remote_pc_controllable_via_chrome_remote_desktop()

    elif is_pc_asus():
        ensure_sound_track_played()  # work with music
        pk_tm.ensure_wsl_distros_enabled()
        ensure_memo_editable()
        ensure_cursor_enabled()
        ensure_vscode_enabled()
        ensure_chatgpt_opened()
        # ensure_chrome_opened()
        ensure_pycharm_opened()
        ensure_slept(milliseconds=80)

        # ensure_pk_scheduler_enabled_py_as_not_child_process()  # ensure_routine_startup_enabled() 내에서 pk_scheduler 실행 금지, circuler calling
        # ensure_task_orchestrator_cli_log_editable()
        # ensure_gemini_cli_enabled()
        ensure_windows_minimized()
        # ensure_task_orchestrator_cli_started_py_as_not_child_process()  # TBD : task_orchestrator_cli 을 백그라운드에서 단축키를 탐지하여 열도록 수정. 더 빨리 동작하게 하기 위함.

        # TODO ensure_process_control
        #   process수집 monitor and kill, play 기능
        #   등록된 프로세스이면서 죽은 프로세스는 색상이 회색으로 프로세스명 표현.
        #   등록된 프로세스이면서 살아있는 프로세스는 색상을 그린으로  프로세스명 표현.
        #   process를 번호 선택 옵션 -> selected -> kill 기능
        #   불필요한 프로그램 조사해서 여기에 등록하여 관리.
    else:
        ensure_not_prepared_yet_guided()
