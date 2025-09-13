from functions.get_project_name import get_project_name
from dotenv import load_dotenv

if __name__ == '__main__':
    import sys
    import traceback
    from pathlib import Path

    from sources.functions.ensure_task_orchestrator_cli_wrapper_window_title_replaced import ensure_task_orchestrator_cli_wrapper_window_title_replaced
    from sources.objects.pk_local_test_activate import LTA
    from sources.functions.ensure_venv_python_path import ensure_venv_python_executed

    from sources.functions.ensure_task_orchestrator_cli_colorama_initialized_once import ensure_task_orchestrator_cli_colorama_initialized_once
    from sources.functions.ensure_task_orchestrator_cli_wrapper_window_title_replaced import ensure_task_orchestrator_cli_wrapper_window_title_replaced

    from sources.functions.ensure_task_orchestrator_cli_started import ensure_task_orchestrator_cli_started
    from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided

    # PYTHONPATH     
    current_script = Path(__file__)
    task_orchestrator_cli_root = current_script.parent.parent
    if str(task_orchestrator_cli_root) not in sys.path:
        sys.path.insert(0, str(task_orchestrator_cli_root))
    try:
        # OS별 virtual environment Python 경로 설정 및 virtual environment 실행
        ensure_venv_python_executed()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

    # pk_option
    ensure_task_orchestrator_cli_colorama_initialized_once()
    # ensure_task_orchestrator_cli_starting_routine_done(__file__=__file__, traceback=traceback)
    # ensure_task_orchestrator_cli_wrapper_suicided(__file__) # : 사용목표 : 인스턴스 1개만 유지,  속도개선 목표 시 :  코드 제거 하여, 속도 개선 가능.
    if LTA:
        # ensure_task_orchestrator_cli_log_initialized(__file__) # code for pk_ensure_task_orchestrator_cli_started.py debugging, should be annotated for operation mode
        pass
    if LTA:
        ensure_task_orchestrator_cli_wrapper_suicided(__file__)
        ensure_task_orchestrator_cli_wrapper_window_title_replaced(__file__)
    else:
        ensure_task_orchestrator_cli_wrapper_suicided(f"{get_project_name()}_lanucher")
        ensure_task_orchestrator_cli_wrapper_window_title_replaced(f"{get_project_name()}_lanucher")

    try:
        ensure_task_orchestrator_cli_started()  # slow # good             # 개선목표 :  venv 활성화 시간,  uv python 실행시간  감소 (원인분석결과 시간성능저하 주원인)
        # ensure_hotkey_monitor_as_service(__file__)          # 개선목표 :  venv 활성화 시간(초기 1회 번만),  uv python 실행시간(초기 1회로 제한)
        # todo       end -> minimize    and    move to front, monitor loop 에 ensure_slept 추가
        #  skim/fzy 으로 전환 성능비교테스트
    except:
        traceback.print_exc()
