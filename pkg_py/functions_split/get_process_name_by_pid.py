from pkg_py.functions_split.get_list_from_tasklist import get_process_name_by_pid as get_process_name_by_pid_new


def get_process_name_by_pid(pid):
    """
    PID로 프로세스명을 찾는 함수 (기존 함수 호환성 유지)
    
    Args:
        pid (int or str): 프로세스 ID
    
    Returns:
        str or None: 프로세스명 또는 None
    """
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    
    # 새로운 통합 함수 사용
    result = get_process_name_by_pid_new(pid)
    
    # 기존 함수는 실패 시 0을 반환했으므로 호환성 유지
    if result is None:
        return 0
    return result
