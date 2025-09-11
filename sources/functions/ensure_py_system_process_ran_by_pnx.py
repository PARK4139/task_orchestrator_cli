from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_py_system_process_ran_by_pnx(file_to_execute, mode=''):
    import logging

    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from sources.objects.task_orchestrator_cli_files import F_VENV_PYTHON_EXE, F_VENV_ACTIVATE_BAT
    import subprocess
    from sources.functions.ensure_command_executed import ensure_command_executed
    from sources.functions.is_os_windows import is_os_windows
    from sources.functions.is_os_wsl_linux import is_os_wsl_linux

    if is_os_windows():
        cmd = rf'start "" cmd.exe /c "cd /d "{D_TASK_ORCHESTRATOR_CLI}" && {F_VENV_ACTIVATE_BAT} && {F_VENV_PYTHON_EXE} "{file_to_execute}"'
        logging.debug(f"[실행 중 - Windows] {cmd}")
        if mode == 'a':
            # 비동기 동작검증 완료
            ensure_command_executed(cmd, mode='a')
        else:
            # 동기 동작검증 완료
            ensure_command_executed(cmd)
    elif is_os_wsl_linux():
        # WSL 환경
        cmd = f'{F_VENV_PYTHON_EXE} {file_to_execute}'
        logging.debug(f"[실행 중 - WSL] {cmd}")
        ensure_command_executed(cmd=cmd)
    else:
        # 기타 리눅스/유닉스
        cmd = f'{F_VENV_PYTHON_EXE} {file_to_execute}'
        logging.debug(f"[실행 중 - Linux/Unix] {cmd}")
        subprocess.run(cmd, shell=True)
