from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_pwd_moved_to_d_task_orchestrator_cli():
    from os import environ
    from pathlib import Path

    from sources.functions.is_os_windows import is_os_windows
    import logging
    import os

    # F_PK_ENSURE_TASK_ORCHESTRATOR_CLI_STARTED_PY = Path(D_TASK_ORCHESTRATOR_CLI_WRAPPERS) / "pk_ensure_task_orchestrator_cli_started.py"
    # F_PK_ENSURE_TASK_ORCHESTRATOR_CLI_ENABLED_PY = Path(D_TASK_ORCHESTRATOR_CLI_WRAPPERS) / "pk_ensure_task_orchestrator_cli_enabled.py"

    current_dir = os.getcwd()

    project_root = None
    if is_os_windows():
        d_userprofile = environ.get('USERPROFILE')
        project_root = Path(d_userprofile) / "Downloads" / "task_orchestrator_cli"
    else:
        d_home = environ.get('HOME')
        project_root = Path(d_home) / "Downloads" / "task_orchestrator_cli"

    if not project_root.exists():
        logging.debug(f"⚠️ task_orchestrator_cli 루트 디렉토리를 찾을 수 없습니다.")
        logging.debug(f"⚠️ 현재 디렉토리: {current_dir}")
        logging.debug(f"⚠️ 이 스크립트는 task_orchestrator_cli 루트 디렉토리에서 실행되어야 합니다.")
        return False

    os.chdir(project_root)
    logging.debug(f"✅ task_orchestrator_cli 루트 디렉토리로 이동 완료: {os.getcwd()}")
    if str(current_dir) != str(project_root):
        logging.debug(f"project_root={project_root}")
        logging.debug(f"current_dir={current_dir}")
        logging.debug(f"⚠️ current directory is not task_orchestrator_cli root")
        return False

    return True
