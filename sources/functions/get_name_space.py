

def get_name_space():  # name space # namespace # 파이썬 네임스페이스
    import inspect
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    dir()
    return dir()
