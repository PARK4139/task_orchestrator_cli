from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_pk_scheduler_reloaded_at_windows_startup_directory():
    from pathlib import Path

    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI
    from sources.objects.task_orchestrator_cli_files import F_VENV_ACTIVATE_BAT, F_PK_ENSURE_STARTUP_ROUTINE_ENABLED_PY

    from sources.objects.pk_local_test_activate import LTA
    from sources.functions.ensure_command_executed import ensure_command_executed
    import logging
    from sources.functions.get_list_converted_from_byte_list_to_str_list import \
        get_list_converted_from_byte_list_to_str_list
    from sources.objects.task_orchestrator_cli_directories import D_PK_RECYCLE_BIN
    import os
    import textwrap

    logging.debug(f"add task_orchestrator_cli to shell:startup")

    startup_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu",
                                  "Programs", "Startup")

    # 바로가기 파일명
    shortcut_name = "PK_System_Startup.lnk"
    shortcut_path = os.path.join(startup_folder, shortcut_name)

    # 실행할 명령어 (virtual environment 직접 활성화로 수정)

    command = rf'cmd.exe /c "cd /d "{D_TASK_ORCHESTRATOR_CLI}" && {F_VENV_ACTIVATE_BAT} && python {F_PK_ENSURE_STARTUP_ROUTINE_ENABLED_PY}"'

    logging.debug(f'Windows 시작 프로그램 폴더에 바로가기를 생성합니다 {"%%%FOO%%%" if LTA else ""}')
    logging.debug(f'시작 프로그램 폴더: {startup_folder} {"%%%FOO%%%" if LTA else ""}')
    logging.debug(f'바로가기 파일: {shortcut_path} {"%%%FOO%%%" if LTA else ""}')
    logging.debug(f'실행 명령어: {command} {"%%%FOO%%%" if LTA else ""}')

    try:
        # 시작 프로그램 폴더가 없으면 생성
        if not os.path.exists(startup_folder):
            os.makedirs(startup_folder)
            logging.debug(f'시작 프로그램 폴더를 생성했습니다 {"%%%FOO%%%" if LTA else ""}')

        # PowerShell을 사용하여 바로가기 생성
        ps_script = textwrap.dedent(rf"""
            $WshShell = New-Object -comObject WScript.Shell
            $Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
            $Shortcut.TargetPath = "cmd.exe"
            $Shortcut.Arguments = '/c "cd /d "{D_TASK_ORCHESTRATOR_CLI}" && {F_VENV_ACTIVATE_BAT} && python {F_PK_ENSURE_STARTUP_ROUTINE_ENABLED_PY}"'
            $Shortcut.WorkingDirectory = "{D_TASK_ORCHESTRATOR_CLI}"
            $Shortcut.Save()
        """).lstrip()
        temp_ps_file = rf"{D_PK_RECYCLE_BIN}\temp_create_shortcut.ps1"
        with open(temp_ps_file, 'w', encoding='utf-8') as f:
            f.write(ps_script)
        logging.debug(f'임시 PowerShell 스크립트 생성: {temp_ps_file} {"%%%FOO%%%" if LTA else ""}')

        # PowerShell 실행
        ps_cmd = rf'powershell.exe -ExecutionPolicy Bypass -File "{temp_ps_file}"'
        std_list = ensure_command_executed(cmd=ps_cmd)

        # 이미 문자열 리스트인지 확인하고 변환
        if not (std_list and isinstance(std_list[0], str)):
            std_list = get_list_converted_from_byte_list_to_str_list(std_list)

        # 결과 출력
        for std_str in std_list:
            logging.debug(f'[STD_OUT] {std_str} {"%%%FOO%%%" if LTA else ""}')

        # 임시 파일 삭제
        if os.path.exists(temp_ps_file):
            os.remove(temp_ps_file)
            logging.debug(f'임시 파일 삭제 완료: {temp_ps_file} {"%%%FOO%%%" if LTA else ""}')

        # 바로가기 파일 존재 확인
        if os.path.exists(shortcut_path):
            logging.debug(f'시작 프로그램에 성공적으로 등록되었습니다 {"%%%FOO%%%" if LTA else ""}')
            logging.debug(f'바로가기 위치: {shortcut_path} {"%%%FOO%%%" if LTA else ""}')
        else:
            logging.debug(f'바로가기 생성에 실패했습니다 {"%%%FOO%%%" if LTA else ""}')

    except Exception as e:
        logging.debug(f'시작 프로그램 등록 중 오류가 발생했습니다: {str(e)} {"%%%FOO%%%" if LTA else ""}')
        raise

    # 추가 정보 출력
    logging.debug(f'시작 프로그램 관리 방법: {"%%%FOO%%%" if LTA else ""}')
    logging.debug(f'시작 프로그램 폴더 열기: shell:startup {"%%%FOO%%%" if LTA else ""}')
    logging.debug(f'바로가기 삭제: {shortcut_path} 파일 삭제 {"%%%FOO%%%" if LTA else ""}')
    logging.debug(f'수동 실행: {command} {"%%%FOO%%%" if LTA else ""}')
