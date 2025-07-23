from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def ensure_window_to_front_v1(window_title_seg=None, pid=None):
    import inspect
    # import win32gui  # pywin32
    # import win32process

    import psutil
    func_n = inspect.currentframe().f_code.co_name
    pk_print(f'''func_n={func_n} {'%%%FOO%%%' if LTA else ''}''')
    if window_title_seg is not None:
        pk_print(rf'''window_title_seg="{window_title_seg}"{'%%%FOO%%%' if LTA else ''}''')
        while 1:
            ensure_window_to_front_core(window_title_seg)
            if is_front_window_title(window_title_seg=window_title_seg):
                pk_print(f'''move window (window_title_seg={window_title_seg}) to front via {func_n}()''',
                         print_color='green')
                break
    if pid is not None:
        pk_print(rf'''pid="{pid}"{'%%%FOO%%%' if LTA else ''}''')
        if not str(pid).isdigit():
            # pk_print(f"PID 분석 결과 숫자가 아닌 것으로 판단: {pid}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
            return
        pid = int(pid)
        try:
            # PID에 해당하는 프로세스 객체 가져오기
            process = psutil.Process(pid)

            if process.is_running() and process.status() != psutil.STATUS_ZOMBIE:
                hwnd = win32gui.FindWindow(None, None)  # 첫 번째 창 핸들을 가져옴

                # PID와 연결된 창 핸들을 검색
                while hwnd:
                    _, found_pid = win32process.GetWindowThreadProcessId(hwnd)

                    # 검색된 창의 PID가 입력 PID와 일치하면 창 활성화
                    if found_pid == pid:
                        try:
                            win32gui.SetForegroundWindow(hwnd)  # 창 활성화
                            # pk_print(f"PID {pid}의 창을 활성화했습니다.", print_color='blue')
                            break
                        except Exception as e:
                            # pk_print(f"창 활성화 실패: {e}", print_color='red')
                            pass
                    # 다음 창 핸들 검색
                    hwnd = win32gui.FindWindowEx(None, hwnd, None, None)
                else:
                    # pk_print(f"PID {pid}에 해당하는 창 핸들을 찾을 수 없습니다.", print_color='red')
                    pass
            else:
                # pk_print(f"{UNDERLINE}프로세스가 exec  중이지 않거나 좀비 상태입니다.", print_color='red')
                pass
        except psutil.NoSuchProcess:
            # pk_print(f"{UNDERLINE}유효하지 않은 PID입니다.", print_color='red')
            pass
        except Exception as e:
            pk_print(f"알 수 없는 {e}", print_color='red')
            pass
