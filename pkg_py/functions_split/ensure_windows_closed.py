

def ensure_windows_closed(window_title):
    """특정 창을 닫는 함수
    
    Args:
        window_title (str): 닫을 창의 제목
    
    Returns:
        bool: 창을 닫았으면 True, 못 닫았으면 False
    """
    import time
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
    from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
    from pkg_py.functions_split.is_window_opened import is_window_opened
    from pkg_py.system_object.gui_util import get_windows_opened

    # 닫을 창 제목들
    window_titles_to_close = [window_title]

    max_wait_time = 10  # 최대 10초 대기
    wait_count = 0
    
    while wait_count < max_wait_time:
        # 현재 열린 창 목록 확인 (디버깅용)
        windows_opened = get_windows_opened()
        everything_windows = [w for w in windows_opened if "Everything" in w]
        if everything_windows:
            ensure_printed(f"발견된 Everything 창들: {everything_windows}", print_color='yellow')
        
        # 각 창 제목에 대해 창이 열려있는지 확인하고 닫기
        for title in window_titles_to_close:
            if is_window_opened(window_title_seg=title):
                ensure_printed(f"창 닫기 시도: {title}", print_color='cyan')
                ensure_process_killed(window_title=title)
                return True  # 창을 닫았으면 True 반환
        
        time.sleep(0.5)  # 0.5초씩 대기
        wait_count += 1
    
    ensure_printed(f"'{window_title}' 창을 찾을 수 없거나 닫을 수 없습니다.", print_color='red')
    return False  # 창을 닫지 못했으면 False 반환
