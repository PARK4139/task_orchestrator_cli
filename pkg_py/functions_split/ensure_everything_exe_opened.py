def ensure_everything_exe_opened():
    from pkg_py.system_object.files import F_EVERYTHING_EXE
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.is_os_linux import is_os_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.ensure_printed import ensure_printed

    if is_os_windows():
        # Windows에서는 Everything 사용
        if F_EVERYTHING_EXE:
            ensure_command_excuted_to_os(cmd=fr"explorer.exe {F_EVERYTHING_EXE}")
        else:
            ensure_printed("⚠️ Everything이 설치되지 않았습니다.")
    elif is_os_linux():
        # Linux에서는 다양한 파일 검색 도구 사용
        search_tools = [
            ('fzf', 'fzf'),  # Fuzzy finder
            ('locate', 'locate'),  # 파일 위치 검색
            ('find', 'find . -name "*" | head -20'),  # find 명령어
            ('fd', 'fd'),  # fd (find 대안)
        ]
        
        for tool_name, command in search_tools:
            try:
                ensure_command_excuted_to_os(cmd=f'{command} --version', mode='sync')
                ensure_printed(f"🔍 {tool_name}를 사용하여 파일 검색을 시작합니다.")
                # 실제 검색은 사용자가 입력해야 함
                # ensure_command_excuted_to_os(cmd=f'{command} [검색어]')
                break
            except:
                continue
        else:
            ensure_printed("⚠️ 사용 가능한 파일 검색 도구를 찾을 수 없습니다.")
    else:
        # macOS에서는 Spotlight 사용
        try:
            ensure_command_excuted_to_os(cmd='open -a "Spotlight"', mode='sync')
            ensure_printed("🔍 Spotlight를 사용하여 파일 검색을 시작합니다.")
        except Exception as e:
            ensure_printed(f"❌ 파일 검색 도구 실행 실패: {e}")
