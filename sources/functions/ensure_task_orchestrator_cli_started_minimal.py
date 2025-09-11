"""
즉시 실행을 위한 최적화된 task_orchestrator_cli 시작 함수
백그라운드 모니터링에서 호출될 때 사용
"""


def ensure_task_orchestrator_cli_started_minimal(test_mode=False):
    import logging
    import subprocess
    import time
    from pathlib import Path

    from functions.ensure_task_orchestrator_cli_started import ensure_value_completed_return_core
    from sources.objects.pk_map_texts import PkTexts

    """
    최소한의 초기화로 실행 (가장 빠름)
    """
    start_time = time.time()
    messages = PkTexts()

    try:
        # 기본적인 파일 목록만 가져와서 실행
        from sources.functions.get_sorted_pk_file_list import get_excutable_wrappers
        from sources.objects.pk_etc import pk_

        # 파일 목록 가져오기
        pk_file_list = get_excutable_wrappers()

        if not pk_file_list:
            logging.debug(messages.FILE_NOT_FOUND)
            return False

        # 간단한 선택 UI
        display_names = [Path(p).name.removeprefix(pk_) for p in pk_file_list]

        selected_name = ensure_value_completed_return_core(
            message=f"{messages.PROCESS} ({messages.TOTAL}: {len(display_names)})",
            options=display_names,
            test_mode=test_mode,
        )

        if not selected_name:
            logging.debug(messages.USER_CANCELLED_EMPTY_COMMIT)
            return False

        # 파일 실행
        selected_file = next(
            (Path(p) for p in pk_file_list if Path(p).name == f"{pk_}{selected_name}"),
            None
        )

        if selected_file and selected_file.exists():
            # 백그라운드에서 실행
            cmd = f'start "" cmd.exe /k "python "{selected_file}""'
            subprocess.Popen(cmd, shell=True)

            execution_time = time.time() - start_time
            logging.debug(f"{messages.COMPLETE} ({messages.TOTAL_EXECUTION_TIME}: {execution_time:.3f}{messages.SECONDS})")
            return True
        else:
            logging.debug(messages.FILE_NOT_FOUND)
            return False

    except Exception as e:
        logging.debug(f"{messages.ERROR}: {e}")
        return False


if __name__ == '__main__':
    ensure_task_orchestrator_cli_started_minimal(test_mode=True)
