def is_losslesscut_running(F_CACHE):
    from pkg_py.functions_split.is_losslesscut_running_v1 import is_losslesscut_running_v1
    return is_losslesscut_running_v1()  # 느림지면. 재부팅해야 쓸만한 속도.
    # return is_losslesscut_running_v2()
    # return is_losslesscut_running_v3(F_CACHE) # 초기에 F_CASHE 갱신이 안되는 문제가 있음.
