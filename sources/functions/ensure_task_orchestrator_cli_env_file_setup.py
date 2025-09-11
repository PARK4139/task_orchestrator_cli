from pathlib import Path

from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_task_orchestrator_cli_env_file_setup()->Path:
    from dotenv import load_dotenv
    import traceback


    import logging

    from functions.ensure_debug_loged_verbose import ensure_debug_loged_verbose
    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    try:

        # load_dotenv()  # 프로젝트 내부에서 부모까지 self find 한다.

        # 명시적인 방식
        dotenv_path = D_TASK_ORCHESTRATOR_CLI.parent / ".env"
        load_dotenv(dotenv_path=dotenv_path)
        logging.debug(f'env file is used ({dotenv_path})')
        return dotenv_path
    except:
        ensure_debug_loged_verbose(traceback)
    finally:
        pass
