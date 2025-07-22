

def get_name_space():  # name space # namespace # 파이썬 네임스페이스
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    dir()
    return dir()
