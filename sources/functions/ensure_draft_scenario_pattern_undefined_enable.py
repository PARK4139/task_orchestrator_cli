import logging
import traceback
from pathlib import Path

from functions.ensure_env_var_completed_advanced import ensure_env_var_completed_advanced
from functions.ensure_gemini_cli_installed_as_latest_version import ensure_gemini_cli_installed_as_latest_version
from functions.ensure_spoken import ensure_spoken
from functions.alert_as_gui import alert_as_gui
from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
from functions.get_caller_n import get_caller_n
from objects.pk_etc import PK_UNDERLINE
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.functions.ensure_debug_log_seperated import ensure_log_seperated_by_pk_debug_line
from sources.functions.get_execute_cmd_with_brakets import get_cmd_chains
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_FUNCTIONS
from sources.objects.task_orchestrator_cli_files import F_VENV_PYTHON_EXE


def _execute_sample1():
    file_sample1 = Path(D_TASK_ORCHESTRATOR_CLI_FUNCTIONS) / "ensure_task_orchestrator_cli_started_minimal.py"
    cmd = get_cmd_chains(F_VENV_PYTHON_EXE, file_sample1)
    ensure_command_executed(cmd)


def _execute_sample2():
    file_sample2 = Path(D_TASK_ORCHESTRATOR_CLI_FUNCTIONS) / "ensure_task_orchestrator_cli_started.py"
    cmd = get_cmd_chains(F_VENV_PYTHON_EXE, file_sample2)
    ensure_command_executed(cmd)


@ensure_log_seperated_by_pk_debug_line
def ensure_draft_scenario_sample1_and_smaple2_performance_compared(__file__):
    # todo : fix
    import logging
    from sources.objects.pk_etc import PK_UNDERLINE

    from sources.functions.print_samples_ranking import log_samples_ranking

    from sources.functions.analyze_samples_results import analyze_samples_results
    from sources.functions.clear_benchmark_data import clear_benchmark_data

    # mode = "cumulative" # pk_option
    mode = "non_cumulative"  # pk_option
    iterations = 10

    try:
        if mode == "cumulative":
            logging.debug("[모드] Cumulative 모드로 실행합니다. 기존 데이터를 보존합니다.")
        else:
            logging.debug("[모드] Non-cumulative 모드로 실행합니다. 기존 데이터를 초기화하고 새로 시작합니다.")
            clear_benchmark_data()

        logging.debug(f"\n[자동] {mode} 모드로 모든 테스트를 순차적으로 실행합니다...")
        logging.debug(PK_UNDERLINE)

        # n. 성능 테스트 실행
        logging.debug(PK_UNDERLINE)
        logging.debug("[1단계] 성능 테스트 실행 (10회)")
        logging.debug(f"[테스트] 성능 테스트 실행 ({iterations}회)")
        logging.debug(PK_UNDERLINE)

        for i in range(iterations):
            logging.debug(PK_UNDERLINE)
            logging.debug(f"실행 {i + 1}/{iterations}...")
            _execute_sample1()

        for i in range(iterations):
            logging.debug(PK_UNDERLINE)
            logging.debug(f"실행 {i + 1}/{iterations}...")
            _execute_sample2()

        # n. 결과 분석
        logging.debug(PK_UNDERLINE)
        logging.debug("[2단계] 결과 분석")
        analyze_samples_results()
        logging.debug(PK_UNDERLINE)

        # n. 성능 순위
        logging.debug(PK_UNDERLINE)
        logging.debug("[3단계] 성능 순위")
        log_samples_ranking()
        logging.debug(PK_UNDERLINE)

        # 모드별 추가 정보
        if mode == "non_cumulative":
            logging.debug(f"\n[정보] Non-cumulative 모드: 이번 테스트에서 생성된 샘플만 포함 (기존 데이터 무시)")
        else:
            logging.debug(f"\n[정보] Cumulative 모드: 전체 누적 샘플 포함 (트렌드 분석 가능)")

        logging.debug("[완료] 모든 테스트가 성공적으로 완료되었습니다!")

    except KeyboardInterrupt:
        logging.debug("\n[중단] 사용자에 의해 중단되었습니다.")
    except Exception as e:
        logging.debug(f"\n[오류] 테스트 실행 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()


def _execute_sample1():
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.get_execute_cmd_with_brakets import get_cmd_chains
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_FUNCTIONS
    from sources.objects.task_orchestrator_cli_files import F_VENV_PYTHON_EXE
    # pk_option
    file_sample = D_TASK_ORCHESTRATOR_CLI_FUNCTIONS / "ensure_task_orchestrator_cli_started.py"
    cmd = get_cmd_chains(F_VENV_PYTHON_EXE, file_sample)
    ensure_command_executed(cmd)

    # pk_option
    # ensure_python_file_executed_advanced(file_sample)

    # target_file = D_TASK_ORCHESTRATOR_CLI_WRAPPERS  / "pk_ensure_pnx_backed_up.py"
    # ensure_task_orchestrator_cli_python_file_executed_in_uv_venv_windows(target_file)


def _execute_sample2():
    from sources.functions.ensure_task_orchestrator_cli_wrapper_restarted_self_as_not_child_process import ensure_python_file_executed_advanced
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_FUNCTIONS
    file_sample = D_TASK_ORCHESTRATOR_CLI_FUNCTIONS / "ensure_task_orchestrator_cli_started.py"
    ensure_python_file_executed_advanced(file_sample)


def _ensure_draft_scenario_executed_ver_pattern(__file__):
    # TODO : fix
    # test flow :
    # without refresh 에서 실행 한 로그에서 특정부분 수집
    # 파싱 elapsed_seconds
    # 통계
    for i in range(10):
        _execute_sample2()

    for i in range(10):
        _execute_sample1()


@ensure_log_seperated_by_pk_debug_line
def ensure_draft_scenario_executed(__file__):
    try:
        # alert_as_gui(title_="title_", ment="ment", auto_click_positive_btn_after_seconds=5, input_text_default="input_text_default")

        # ensure_gemini_cli_installed_as_latest_version(__file__)
        return

        # pk_* : 모든 테스트 시나리오 테스트
        ensure_test_scenarios_executed()

        # pk_* : SENSITIVE PAUSE
        ensure_console_paused("next is sensitive process 'copy tree'")

        # pk_* : 삽입형 테스트 코드(환경변수)
        from task_orchestrator_cli_tests.test_ensure_pnx_backed_up import test_scenario_ensure_pnx_backed_up
        test_scenario_ensure_pnx_backed_up()

        # pk_* : 삽입형 테스트 코드(환경변수)
        # PYTHONPATH = os.getenv("PYTHONPATH")
        # logging.debug(rf'PYTHONPATH = "{PYTHONPATH}"')

        # pk_* : 삽입형 테스트 코드(트리)
        ensure_console_cleared()
        ensure_police_block_printed("삽입형 테스트 코드 start")
        ensure_tree_printed(d_checkout, max_depth=2)
        ensure_police_block_printed("삽입형 테스트 코드 end")
        ensure_console_paused()

        # pk_* : 삽입형 테스트 코드(파일존재여부)
        ensure_console_cleared()
        ensure_police_block_printed("삽입형 테스트 코드 start")
        test_file = f_git_auto_push_script_to_publish
        if test_file.exists():
            logging.debug(f'삽입형 테스트 성공')
        else:
            logging.debug(f'삽입형 테스트 실패')
        ensure_police_block_printed("삽입형 테스트 코드 end")
        ensure_console_paused()
        pass

        # pk_* :  사용자 응답확인
        question = f'깃 허브로 퍼블리싱을 진행할까요?'
        ensure_spoken(get_easy_speakable_text(question))
        ok = ensure_value_completed(key_hint=question, options=[PkTexts.YES, PkTexts.NO])
        if ok != PkTexts.YES:
            ensure_task_orchestrator_cli_wrapper_suicided(__file__)



        # f 찾기 #재귀적으로
        # sudo find -type f -name "flash.sh"
        # sudo find . -type f -name "flash.sh"


    except Exception as e:
        logging.debug(PK_UNDERLINE)
        # ensure_debug_loged_simple(e)
        ensure_debug_loged_verbose(traceback)
        logging.debug(PK_UNDERLINE)
    finally:
        ensure_spoken(wait=True)
