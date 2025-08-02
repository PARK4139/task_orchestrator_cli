def ensure_pk_system_processes_killed():
    import inspect
    import psutil
    import os
    import win32gui
    import win32con
    
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_sorted_pk_file_list import get_excutable_pk_system_processes
    from pkg_py.system_object.local_test_activate import LTA
    
    func_n = inspect.currentframe().f_code.co_name
    pk_files = get_excutable_pk_system_processes()
    
    # 통계 변수들
    total_attempted = 0
    window_killed = 0
    process_killed = 0
    not_found = 0
    
    ensure_printed(f" 총 {len(pk_files)}개 pk_* 파일 검사 시작", print_color='cyan')

    # 한번에 모든 python 프로세스 정보 수집 (성능 최적화)
    python_processes = {}
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'] == 'python.exe' and proc.info['cmdline']:
                    cmdline = ' '.join(proc.info['cmdline'])
                    python_processes[proc.pid] = (proc, cmdline)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
    except Exception as e:
        if LTA:
            ensure_printed(f"⚠️ 프로세스 목록 수집 중 오류: {e}", print_color='yellow')

    for pk_file in pk_files:
        try:
            process_name = get_nx(pk_file)  # 파일명만 추출 (확장자 제외)

            total_attempted += 1
            
            # 1단계: 창 제목으로 찾아서 모든 창 종료
            window_found = False
            try:
                from pkg_py.functions_split.get_window_titles_matches import get_window_titles_matches
                window_matches = get_window_titles_matches(window_title=process_name)
                
                if window_matches:
                    # 로그 최소화: 창 개수만 표시
                    ensure_printed(f"🎯 {process_name}: {len(window_matches)}개 창 종료", print_color='green')
                    # 모든 창을 한번에 종료
                    for hwnd, title, similarity in window_matches:
                        try:
                            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                            window_killed += 1
                        except Exception as e:
                            if LTA:
                                ensure_printed(f"    ❌ 창 종료 실패 HWND={hwnd}: {e}", print_color='red')
                    window_found = True
                    
            except Exception as e:
                if LTA:
                    ensure_printed(f"  ⚠️ 창 검색 중 오류: {e}", print_color='yellow')
            
            # 2단계: 창을 찾지 못했다면 미리 수집한 프로세스 목록에서 검색
            if not window_found:
                matching_processes = []
                for pid, (proc, cmdline) in python_processes.items():
                    if process_name in cmdline:
                        matching_processes.append(proc)
                
                if matching_processes:
                    ensure_printed(f"🎯 {process_name}: {len(matching_processes)}개 프로세스 직접 종료", print_color='red')
                    for proc in matching_processes:
                        try:
                            proc.kill()
                            process_killed += 1
                        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                            if LTA:
                                ensure_printed(f"    ❌ 프로세스 종료 실패 PID={proc.pid}: {e}", print_color='red')
                else:
                    not_found += 1

        except Exception as e:
            if LTA:
                ensure_printed(f"❌ {process_name} 처리 중 오류: {e}", print_color='red')
            not_found += 1

    # 최종 통계 출력
    ensure_printed(f"📊 종료 통계:", print_color='cyan')
    ensure_printed(f"  • 총 검사: {total_attempted}개", print_color='white')
    ensure_printed(f"  • 창으로 종료: {window_killed}개", print_color='green')
    ensure_printed(f"  • 프로세스 직접 종료: {process_killed}개", print_color='red')
    ensure_printed(f"  • 실행 중이지 않음: {not_found}개", print_color='gray')
    ensure_printed(f"✅ 총 {window_killed + process_killed}개 프로세스 종료 완료", print_color='green')

