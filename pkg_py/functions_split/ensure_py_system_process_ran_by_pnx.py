def ensure_py_system_process_ran_by_pnx(file_to_excute, file_title):
    # OS별 실행
    import subprocess

    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

    if is_os_windows():
        # title 명령어로 창 제목 지정 (pk_ 접두사 제거된 제목)
        file_title = file_title.strip()
        cmd = f'start "" cmd.exe /k "title {file_title}&& python {file_to_excute}"'
        print(f"[실행 중 - Windows] {cmd}")
        ensure_command_excuted_to_os(cmd=cmd, mode='a', mode_with_window=1)
    elif is_os_wsl_linux():
        # WSL 환경
        cmd = f'python3 {file_to_excute}'
        print(f"[실행 중 - WSL] {cmd}")
        ensure_command_excuted_to_os(cmd=cmd)
    else:
        # 기타 리눅스/유닉스
        cmd = f'python3 {file_to_excute}'
        print(f"[실행 중 - Linux/Unix] {cmd}")
        subprocess.run(cmd, shell=True)