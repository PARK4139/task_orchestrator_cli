def kill_wsl_exe():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    process_name = "wsl.exe"
    cmd = "wsl --shutdown"
    cmd_to_os(cmd=cmd, mode="a")
    pids = get_pids("wsl.exe")
    if pids is not None:
        for pid in pids:
            if pid is not None:
                kill_process_via_taskkill(pid=pid)
    ensure_writen_like_person("exit")
    pk_press("enter")


