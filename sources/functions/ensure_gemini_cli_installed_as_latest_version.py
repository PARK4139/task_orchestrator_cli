from functions.ensure_command_executed_like_human import ensure_command_executed_like_human
from objects.pk_local_test_activate import LTA
from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_gemini_cli_installed_as_latest_version(__file__):
    import os
    import traceback
    from pathlib import Path
    from functions import ensure_spoken, ensure_command_executed, ensure_value_completed
    from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
    from functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
    from functions.ensure_value_completed_advanced import ensure_value_completed_advanced
    from objects.pk_map_texts import PkTexts
    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from functions.get_caller_n import get_caller_n

    try:
        if LTA:
            question = rf"GEMINI 최신버전 설치 계속 진행합니다"
            ensure_spoken(f'{question}')
        else:
            question = rf"GEMINI 최신버전 설치 계속 진행할까요"
            ok = ensure_value_completed(key_hint=question, options=[PkTexts.YES, PkTexts.NO])
            if ok != PkTexts.YES:
                ensure_task_orchestrator_cli_wrapper_suicided(__file__)

        # pk_* : func_n
        func_n = get_caller_n()

        # pk_* : ensure_value_completed_advanced
        key_name = '이동할 pwd 경로' # 이동경로에 GEMINI.md 가 생성
        options = [D_TASK_ORCHESTRATOR_CLI, D_TASK_ORCHESTRATOR_CLI]
        pwd = ensure_value_completed_advanced(key_name=key_name, func_n=func_n, options=options)

        pwd = Path(pwd)
        os.chdir(pwd)
        # ensure_command_executed('npm install -g @google/gemini-cli@latest')
        ensure_command_executed_like_human('npm install -g @google/gemini-cli@latest', __file__)

    # pk_* : except
    except:
        ensure_debug_loged_verbose(traceback)

    # pk_* : finally , ensure_spoken(wait=True)
    finally:
        ensure_spoken(wait=True)
