from pkg_py.functions_split.ensure_tasklist_got import (
    get_image_names_from_tasklist,
    ensure_tasklist_got_with_pid,
    ensure_tasklist_got_filtered,
    get_pids_by_process_name,
    get_pid_by_window_title,
    get_process_name_by_pid,
    get_process_info_by_window_title,
    get_process_info_by_name,
    get_process_info_by_pid
)

def pk_get_image_names_from_tasklist():
    """
    tasklist 명령어의 결과에서 이미지명을 수집하고 중복을 제거한 리스트를 반환 (wrapper)
    
    Returns:
        list: 이미지명 리스트 (중복 제거됨)
    """
    return get_image_names_from_tasklist()

def pk_ensure_tasklist_got_with_pid():
    """
    tasklist 명령어의 결과에서 이미지명과 PID를 함께 수집 (wrapper)
    
    Returns:
        list: (이미지명, PID) 튜플 리스트
    """
    return ensure_tasklist_got_with_pid()

def pk_ensure_tasklist_got_filtered(filter_keywords=None):
    """
    tasklist 명령어의 결과에서 특정 키워드로 필터링된 이미지명 리스트 반환 (wrapper)
    
    Args:
        filter_keywords (list): 필터링할 키워드 리스트 (기본값: None, 모든 프로세스)
    
    Returns:
        list: 필터링된 이미지명 리스트
    """
    return ensure_tasklist_got_filtered(filter_keywords)

def pk_get_pids_by_process_name(process_img_n):
    """
    프로세스명으로 PID 리스트를 반환 (wrapper)
    
    Args:
        process_img_n (str): 프로세스 이미지명
    
    Returns:
        list: PID 리스트
    """
    return get_pids_by_process_name(process_img_n)

def pk_get_pid_by_window_title(window_title_seg):
    """
    윈도우 타이틀로 PID를 찾는 함수 (wrapper)
    
    Args:
        window_title_seg (str): 윈도우 타이틀 일부
    
    Returns:
        str or list: PID 또는 PID 리스트
    """
    return get_pid_by_window_title(window_title_seg)

def pk_get_process_name_by_pid(pid):
    """
    PID로 프로세스명을 찾는 함수 (wrapper)
    
    Args:
        pid (int or str): 프로세스 ID
    
    Returns:
        str or None: 프로세스명 또는 None
    """
    return get_process_name_by_pid(pid)

def pk_get_process_info_by_window_title(window_title_seg):
    """
    윈도우 타이틀로 프로세스 정보를 찾는 함수 (wrapper)
    
    Args:
        window_title_seg (str): 윈도우 타이틀 일부
    
    Returns:
        list: 프로세스 정보 리스트 [(pid, name, exe), ...]
    """
    return get_process_info_by_window_title(window_title_seg)

def pk_get_process_info_by_name(process_name):
    """
    프로세스명으로 실행 중인 프로세스 정보를 반환 (wrapper)
    
    Args:
        process_name (str): 프로세스명
    
    Returns:
        list: 프로세스 정보 리스트 [(pid, name, exe), ...]
    """
    return get_process_info_by_name(process_name)

def pk_get_process_info_by_pid(pid):
    """
    PID로 프로세스 정보를 반환 (wrapper)
    
    Args:
        pid (int): 프로세스 ID
    
    Returns:
        tuple or None: (pid, name, exe) 또는 None
    """
    return get_process_info_by_pid(pid) 