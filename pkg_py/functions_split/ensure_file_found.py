

def ensure_file_found():
    """파일 검색 및 열기 함수 - Everything → PowerShell fallback 체인"""
    from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
    import subprocess
    from pkg_py.functions_split.get_drives_connected import get_drives_connected
    import os
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
    from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
    from pkg_py.functions_split.is_window_opened import is_window_opened
    from pkg_py.functions_split.ensure_windows_closed import ensure_windows_closed

    # 검색 제외 경로 하드코딩
    EXCLUDE_PATHS = [
        "C:\\Windows",
        "C:\\Program Files",
        "C:\\Program Files (x86)",
        "C:\\$Recycle.Bin",
        "C:\\System Volume Information",
        "C:\\Users\\All Users",
        "C:\\Users\\Default",
        "C:\\Users\\Public",
        "C:\\Users\\wjdgn\\AppData\\Local\\Temp",
        "C:\\Users\\wjdgn\\AppData\\Local\\Microsoft\\Windows\\INetCache",
        "C:\\Users\\wjdgn\\AppData\\Roaming\\Microsoft\\Windows\\Recent",
        "C:\\Users\\wjdgn\\Downloads\\pk_system\\.venv",
        "C:\\Users\\wjdgn\\Downloads\\pk_system\\pkg_log",
        "C:\\Users\\wjdgn\\Downloads\\pk_system\\pkg_pkl",
        "C:\\Users\\wjdgn\\Downloads\\pk_system\\pkg_sound",
        "C:\\Users\\wjdgn\\Downloads\\pk_system\\pkg_video",
        "C:\\Users\\wjdgn\\Downloads\\pk_system\\pkg_mp4",
        "C:\\Users\\wjdgn\\Downloads\\pk_system\\pkg_zip",
        "C:\\Users\\wjdgn\\Downloads\\pk_system\\pkg_archived",
    ]

    def check_everything_available():
        """Everything이 설치되어 있는지 확인"""
        everything_paths = [
            r"C:\Program Files\Everything\Everything.exe",
            r"C:\Program Files (x86)\Everything\Everything.exe"
        ]
        for path in everything_paths:
            if os.path.exists(path):
                return path
        return None

    @ensure_seconds_measured
    def search_with_everything(search_query):
        """Everything을 사용한 파일 검색 (명령줄 모드)"""
        try:
            everything_exe = check_everything_available()
            if not everything_exe:
                return None

            # Everything 명령줄 옵션으로 파일만 검색 (최적화된 무제한)
            # -s: 검색어
            # -f: 파일만 검색 (폴더 제외)
            # -a: 모든 결과 출력
            # -n: GUI 창 숨기기
            # -startup: 백그라운드로 실행
            # -sort: 정렬 없음 (속도 향상)
            # -no-gui: GUI 완전 비활성화
            # -no-details: 상세 정보 없이 빠른 검색
            if search_query:
                cmd = f'"{everything_exe}" -startup -a -f -sort -no-gui -no-details -s "{search_query}"'
            else:
                # 검색어가 없으면 모든 파일 검색 (제한 없음)
                cmd = f'"{everything_exe}" -startup -a -f -sort -no-gui -no-details'

            # Everything에서 결과를 가져와서 fzf로 전달
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8',  # 한글 인코딩 명시
                timeout=120,  # 무제한 검색을 위해 타임아웃 연장
                creationflags=subprocess.CREATE_NO_WINDOW  # 창 숨기기
            )

            # Everything 검색이 시작된 후 명령줄 옵션 창 닫기
            ensure_windows_closed("Everything 명령 줄 옵션")
            ensure_windows_closed("Everything")

            if result.returncode == 0 and result.stdout.strip():
                # 결과를 임시 파일에 저장
                import tempfile
                with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
                    temp_file.write(result.stdout)
                    temp_file_path = temp_file.name

                # fzf를 대화형으로 실행
                fzf_cmd = [
                    "fzf",
                    "--height", "40%",
                    "--layout", "reverse",
                    "--border",
                    "--preview", "echo {}",
                    "--preview-window", "right:50%",
                    "--bind", "ctrl-o:execute(echo 'OPEN_FILE_PATH')",
                    "--bind", "ctrl-x:execute(echo 'OPEN_FILE')",
                    "--header", "Ctrl+O: 파일 경로 열기 | Ctrl+X: 파일 열기 | Enter: 선택"
                ]

                # 임시 파일에 결과 저장 후 fzf 실행
                import tempfile
                temp_file_path = tempfile.mktemp(suffix='.txt')
                with open(temp_file_path, 'w', encoding='utf-8') as f:
                    f.write(result.stdout)
                
                # PowerShell을 통해 fzf 실행 (대화형) - 한글 인코딩 수정
                ps_cmd = f'''powershell -NoProfile -ExecutionPolicy Bypass -Command "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; [Console]::InputEncoding = [System.Text.Encoding]::UTF8; Get-Content '{temp_file_path}' -Encoding UTF8 | fzf --height 40% --layout reverse --border --preview 'echo {{}}' --preview-window 'right:50%' --bind 'ctrl-o:execute(echo OPEN_FILE_PATH)' --bind 'ctrl-x:execute(echo OPEN_FILE)' --header 'Ctrl+O: 파일 경로 열기 | Ctrl+X: 파일 열기 | Enter: 선택'"'''
                
                # 대화형 터미널에서 fzf 실행
                fzf_process = subprocess.run(
                    ps_cmd,
                    shell=True,
                    text=True,
                    encoding='utf-8'
                )
                
                # 임시 파일 삭제
                try:
                    os.unlink(temp_file_path)
                except:
                    pass

                if fzf_process.returncode == 0 and fzf_process.stdout.strip():
                    return fzf_process.stdout.strip()
                else:
                    ensure_printed("Everything에서 검색 결과가 없습니다.", print_color='yellow')
                    return None
            else:
                ensure_printed("Everything에서 검색 결과가 없습니다.", print_color='yellow')
                return None

        except subprocess.TimeoutExpired:
            ensure_printed("Everything 검색 시간 초과", print_color='red')
            return None
        except Exception as e:
            ensure_printed(f"Everything 검색 중 오류: {e}", print_color='red')
            return None

    @ensure_seconds_measured
    def search_with_custom(search_path, drives):
        """자체 검색 구현 (PowerShell 사용) - 최적화된 버전"""
        try:
            # PowerShell 명령어 구성 - 최적화된 버전
            exclude_conditions = []
            for exclude_path in EXCLUDE_PATHS:
                if os.path.exists(exclude_path):
                    exclude_conditions.append(f"$_.FullName -notlike '{exclude_path}*'")

            exclude_filter = " -and ".join(exclude_conditions) if exclude_conditions else "1"

            # 최적화된 PowerShell 명령어 (무제한 검색)
            if search_path:
                ps_cmd = f'''powershell -NoProfile -ExecutionPolicy Bypass -Command "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; Get-ChildItem -Path '{search_path}' -Recurse -File -ErrorAction SilentlyContinue | Where-Object {{ {exclude_filter} }} | Select-Object -ExpandProperty FullName"'''
            else:
                drives_list = "','".join([d.replace("\\", "") for d in drives])
                ps_cmd = f'''powershell -NoProfile -ExecutionPolicy Bypass -Command "[Console]::OutputEncoding = [System.Text.Encoding]::UTF8; Get-ChildItem -Path '{drives_list}' -Recurse -File -ErrorAction SilentlyContinue | Where-Object {{ {exclude_filter} }} | Select-Object -ExpandProperty FullName"'''

            # fzf와 함께 사용
            fzf_cmd = [
                "fzf",
                "--height", "40%",
                "--layout", "reverse",
                "--border",
                "--preview", "echo {}",
                "--preview-window", "right:50%",
                "--bind", "ctrl-o:execute(echo 'OPEN_FILE_PATH')",
                "--bind", "ctrl-x:execute(echo 'OPEN_FILE')",
                "--header", "Ctrl+O: 파일 경로 열기 | Ctrl+X: 파일 열기 | Enter: 선택"
            ]

            # 타임아웃 설정 (1시간)
            timeout_seconds = 3600
            
            ps_process = subprocess.Popen(
                ps_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',  # 한글 인코딩 명시
                shell=True
            )
            
            fzf_process = subprocess.Popen(
                fzf_cmd,
                stdin=ps_process.stdout,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8'  # 한글 인코딩 명시
            )

            try:
                selected_file, stderr = fzf_process.communicate(timeout=timeout_seconds)
                ps_process.wait(timeout=timeout_seconds)
                
                if fzf_process.returncode == 0 and selected_file.strip():
                    ensure_printed(f"파일 선택됨: {selected_file.strip()}", print_color='green')
                    return selected_file.strip()
                elif fzf_process.returncode == 130:  # Ctrl+C로 취소
                    ensure_printed("파일 선택이 취소되었습니다.", print_color='yellow')
                    return None
                else:
                    ensure_printed("파일이 선택되지 않았습니다.", print_color='yellow')
                    return None
                    
            except subprocess.TimeoutExpired:
                ensure_printed("PowerShell 검색 시간 초과", print_color='red')
                ps_process.kill()
                fzf_process.kill()
                return None

        except Exception as e:
            ensure_printed(f"자체 검색 중 오류: {e}", print_color='red')
            return None

    # 드라이브 선택 (모든 드라이브 옵션 포함)
    drives = get_drives_connected()
    drives.reverse()  # 드라이브 목록을 reverse
    
    # 모든 드라이브에서 검색 옵션 추가
    search_options = ["모든 드라이브에서 검색"] + drives
    
    selected_drive = get_value_completed("드라이브 선택: ", search_options)
    if selected_drive is None:
        print("드라이브 선택이 취소되었습니다.")
        return
    
    # 검색 경로 설정
    if selected_drive == "모든 드라이브에서 검색":
        search_path = ""
    else:
        search_path = selected_drive

    # 검색어 입력
    # search_query = input("검색어를 입력하세요 (Enter: 모든 파일): ").strip() # pk_option
    search_query = "" # pk_option

    # Fallback 체인 실행 (Everything → PowerShell)
    selected_file = None

    # 1. Everything 우선 시도 (가장 빠름)
    if check_everything_available():
        ensure_printed("Everything으로 검색 중... (최고 속도)", print_color='cyan')
        
        # Everything DB 최적화 확인
        try:
            from pkg_py.functions_split.ensure_everything_db_optimized import ensure_everything_db_optimized
            ensure_everything_db_optimized()
        except ImportError:
            ensure_printed("Everything DB 최적화 함수를 찾을 수 없습니다.", print_color='yellow')
        
        # Everything SSD 최적화 확인
        try:
            from pkg_py.functions_split.ensure_everything_ssd_optimized import ensure_everything_ssd_optimized
            ensure_everything_ssd_optimized()
        except ImportError:
            ensure_printed("Everything SSD 최적화 함수를 찾을 수 없습니다.", print_color='yellow')
        
        # Everything 빠른 검색 최적화
        try:
            from pkg_py.functions_split.ensure_everything_fast_search import ensure_everything_fast_search
            ensure_everything_fast_search()
        except ImportError:
            ensure_printed("Everything 빠른 검색 최적화 함수를 찾을 수 없습니다.", print_color='yellow')
        
        # Everything 검색 시도
        try:
            everything_exe = check_everything_available()
            if everything_exe:
                selected_file = search_with_everything(search_query)
                if selected_file:
                    ensure_printed("Everything 검색 완료", print_color='green')
                else:
                    ensure_printed("Everything 검색 실패, PowerShell 시도...", print_color='yellow')
            else:
                ensure_printed("Everything을 찾을 수 없습니다.", print_color='yellow')
                ensure_printed("PowerShell 시도...", print_color='yellow')
                
        except Exception as e:
            ensure_printed(f"Everything 검색 오류: {e}", print_color='red')
            ensure_printed("PowerShell 시도...", print_color='yellow')
    else:
        ensure_printed("Everything을 찾을 수 없습니다.", print_color='yellow')
        ensure_printed("PowerShell 시도...", print_color='yellow')

    # 2. PowerShell 시도 (Everything 실패 시)
    if not selected_file:
        ensure_printed("PowerShell 자체 검색 중... (느림)", print_color='cyan')
        selected_file = search_with_custom(search_path, drives)
        if selected_file:
            ensure_printed("PowerShell 검색 완료", print_color='green')
        else:
            ensure_printed("모든 검색 방법 실패", print_color='red')

    # 최종 결과 확인
    if not selected_file:
        ensure_printed("모든 검색 방법 실패", print_color='red')

    # 파일 처리
    if selected_file:
        ensure_printed(f"선택된 파일: {selected_file}", print_color='cyan')
        
        # 모드 선택 (tab 자동완성)
        open_modes = [
            "파일 경로 열기",
            "파일 열기"
        ]

        # selected_open_mode = get_value_completed("열기 모드 선택: ", open_modes) # pk_option
        selected_open_mode = "파일 열기"
        if selected_open_mode is None:
            ensure_printed("모드 선택이 취소되었습니다.", print_color='yellow')
            return

        try:
            if selected_open_mode == "파일 경로 열기":
                # open file path 모드
                parent_dir = os.path.dirname(selected_file)
                cmd = f'explorer.exe /select,"{selected_file}"'
                ensure_printed(f"파일 경로 열기: {selected_file}", print_color='blue')
                subprocess.run(cmd, shell=True)
            elif selected_open_mode == "파일 열기":
                # open file 모드
                try:
                    # ensure_opened_by_ext 함수 호출
                    from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
                    ensure_printed(f"파일 열기: {selected_file}", print_color='blue')
                    ensure_pnx_opened_by_ext(selected_file)
                except ImportError:
                    ensure_printed("ensure_opened_by_ext 함수를 찾을 수 없습니다.", print_color='red')
                    os.startfile(selected_file)
        except Exception as e:
            ensure_printed(f"파일 열기 중 오류: {e}", print_color='red')
    elif not selected_file:
        ensure_printed("파일이 선택되지 않았습니다.", print_color='yellow')





