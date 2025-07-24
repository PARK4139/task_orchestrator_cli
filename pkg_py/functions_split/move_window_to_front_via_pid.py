from pkg_py.functions_split.pk_print import pk_print


def move_window_to_front_via_pid(pid):
    import inspect
    
    
    import win32con
    import psutil

    func_n = inspect.currentframe().f_code.co_name
    if not str(pid).isdigit():
        pk_print(f"[{func_n}()] PID가 숫자가 아닙니다: {pid}", print_color='red')
        return
    pid = int(pid)
    try:
        process = psutil.Process(pid)
        if not (process.is_running() and process.status() != psutil.STATUS_ZOMBIE):
            pk_print(f"[{func_n}()] 프로세스가 실행 중이 아니거나 좀비 상태입니다", print_color='red')
            return

        def enum_handler(hwnd, result):
            try:
                _, hwnd_pid = win32process.GetWindowThreadProcessId(hwnd)
                if hwnd_pid == pid and win32gui.IsWindowVisible(hwnd):
                    result.append(hwnd)
            except Exception:
                pass

        hwnd_list = []
        win32gui.EnumWindows(enum_handler, hwnd_list)
        if not hwnd_list:
            pk_print(f"[{func_n}()] PID {pid}에 연결된 창이 없습니다", print_color='red')
            return
        hwnd = hwnd_list[0]
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        # 포그라운드로 이동
        win32gui.SetForegroundWindow(hwnd)
        win32gui.BringWindowToTop(hwnd)
        pk_print(f"[{func_n}()] PID {pid}의 창을 앞으로 가져왔습니다", print_color='green')
    except psutil.NoSuchProcess:
        pk_print(f"[{func_n}()] 유효하지 않은 PID입니다: {pid}", print_color='red')
    except Exception as e:
        pk_print(f"[{func_n}()] 알 수 없는 오류: {e}", print_color='red')
