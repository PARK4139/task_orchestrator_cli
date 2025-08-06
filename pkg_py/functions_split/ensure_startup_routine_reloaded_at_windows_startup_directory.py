from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_startup_routine_reloaded_at_windows_startup_directory():
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_list_converted_from_byte_list_to_str_list import get_list_converted_from_byte_list_to_str_list
    from pkg_py.system_object.directories import D_PK_RECYCLE_BIN
    import os
    import subprocess

    # Windows 시작 프로그램 폴더 경로
    startup_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    
    # 바로가기 파일명
    shortcut_name = "PK_System_Startup.lnk"
    shortcut_path = os.path.join(startup_folder, shortcut_name)
    
    # 실행할 명령어 (cmd.exe를 통해 실행)
    target_script = "pkg_py/pk_ensure_startup_routine_enabled.py"
    command = f'cmd.exe /c "cd /d "%D_PK_SYSTEM%" && uv run {target_script}"'
    
    ensure_printed(f'Windows 시작 프로그램 폴더에 바로가기를 생성합니다 {"%%%FOO%%%" if LTA else ""}', print_color="blue")
    ensure_printed(f'시작 프로그램 폴더: {startup_folder} {"%%%FOO%%%" if LTA else ""}', print_color="blue")
    ensure_printed(f'바로가기 파일: {shortcut_path} {"%%%FOO%%%" if LTA else ""}', print_color="blue")
    ensure_printed(f'실행 명령어: {command} {"%%%FOO%%%" if LTA else ""}', print_color="blue")

    try:
        # 시작 프로그램 폴더가 없으면 생성
        if not os.path.exists(startup_folder):
            os.makedirs(startup_folder)
            ensure_printed(f' 시작 프로그램 폴더를 생성했습니다 {"%%%FOO%%%" if LTA else ""}', print_color="green")
        
        # PowerShell을 사용하여 바로가기 생성
        ps_script = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
$Shortcut.TargetPath = "cmd.exe"
$Shortcut.Arguments = '/c "cd /d "%D_PK_SYSTEM%" && uv run {target_script}"'
$Shortcut.WorkingDirectory = "%D_PK_SYSTEM%"
$Shortcut.Save()
'''
        
        # PowerShell 스크립트를 D_PK_RECYCLE_BIN에 임시 파일로 저장
        temp_ps_file = os.path.join(D_PK_RECYCLE_BIN, "temp_create_shortcut.ps1")
        with open(temp_ps_file, 'w', encoding='utf-8') as f:
            f.write(ps_script)
        
        ensure_printed(f' 임시 PowerShell 스크립트 생성: {temp_ps_file} {"%%%FOO%%%" if LTA else ""}', print_color="blue")
        
        # PowerShell 실행
        ps_cmd = f'powershell.exe -ExecutionPolicy Bypass -File "{temp_ps_file}"'
        std_list = ensure_command_excuted_to_os(cmd=ps_cmd)
        
        # 이미 문자열 리스트인지 확인하고 변환
        if std_list and len(std_list) > 0 and isinstance(std_list[0], str):
            pass
        else:
            std_list = get_list_converted_from_byte_list_to_str_list(std_list)

        # 결과 출력
        for std_str in std_list:
            ensure_printed(f'[STD_OUT] {std_str} {"%%%FOO%%%" if LTA else ""}', print_color="green")

        # 임시 파일 삭제
        if os.path.exists(temp_ps_file):
            os.remove(temp_ps_file)
            ensure_printed(f'️ 임시 파일 삭제 완료: {temp_ps_file} {"%%%FOO%%%" if LTA else ""}', print_color="green")

        # 바로가기 파일 존재 확인
        if os.path.exists(shortcut_path):
            ensure_printed(f' 시작 프로그램에 성공적으로 등록되었습니다 {"%%%FOO%%%" if LTA else ""}', print_color="green")
            ensure_printed(f' 바로가기 위치: {shortcut_path} {"%%%FOO%%%" if LTA else ""}', print_color="blue")
        else:
            ensure_printed(f' 바로가기 생성에 실패했습니다 {"%%%FOO%%%" if LTA else ""}', print_color="red")

    except Exception as e:
        ensure_printed(f' 시작 프로그램 등록 중 오류가 발생했습니다: {str(e)} {"%%%FOO%%%" if LTA else ""}', print_color="red")
        raise

    # 추가 정보 출력
    ensure_printed(f' 시작 프로그램 관리 방법: {"%%%FOO%%%" if LTA else ""}', print_color="blue")
    ensure_printed(f'   시작 프로그램 폴더 열기: shell:startup {"%%%FOO%%%" if LTA else ""}', print_color="blue")
    ensure_printed(f'   바로가기 삭제: {shortcut_path} 파일 삭제 {"%%%FOO%%%" if LTA else ""}', print_color="blue")
    ensure_printed(f'   수동 실행: {command} {"%%%FOO%%%" if LTA else ""}', print_color="blue")