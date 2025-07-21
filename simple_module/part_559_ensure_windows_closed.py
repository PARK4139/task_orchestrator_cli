

def ensure_windows_closed():
    import win32gui

    from pkg_py.simple_module.part_829_ensure_func_info_saved import ensure_func_info_saved
    from pkg_py.pk_system_layer_PkMessages2025 import PkMessages2025
    from pkg_py.simple_module.part_014_pk_print import pk_print

    import win32com.client

    import pythoncom
    import os
    import traceback
    # import win32gui
    import win32con
    import inspect
    try:

        func_n = inspect.currentframe().f_code.co_name
        pythoncom.CoInitialize()  # COM Initialization
        shell = win32com.client.Dispatch("Shell.Application")
        windows = shell.Windows()
        path_to_windows = {}
        pk_print("Window explorer.exe 중복창 탐지 중...")
        for window in windows:
            try:
                hwnd = window.HWND  # 창의 핸들값 가져오기
                if not hwnd:
                    pk_print(f"HWND를 찾을 수 없는 창: {window.Name}", print_color='red')
                    continue
                current_path = window.Document.Folder.Self.Path
                if not current_path:
                    pk_print("경로를 확인할 수 없는 창이 발견됨", print_color='red')
                    continue

                # 경로 정규화
                normalized_path = os.path.normpath(current_path).lower()

                # 창 목록에 추가
                path_to_windows.setdefault(normalized_path, []).append((hwnd, window))

            except Exception as e:
                pk_print(f"창 처리 중 오류 발생: {e}", print_color='red')
                continue

        # 중복된 창 닫기
        for path, win_list in path_to_windows.items():
            if len(win_list) > 1:
                pk_print(f"[중복창 탐지] {len(win_list)}개 창 중복 path={path}")
                for hwnd, window in win_list[1:]:  # 첫 번째 창을 제외한 나머지 창 닫기
                    try:
                        window.Quit()  # pk_print(f"[중복창 닫기] hwnd={hwnd} path={path}")
                        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)  # 추가적으로 윈도우 강제 닫기 시도

                        pk_print(f"[중복창 닫기] window={window} hwnd={hwnd} path={path}", print_color="green")
                    except:
                        pk_print(f"[중복창 닫기] window={window} hwnd={hwnd} path={path}", print_color='red')
        func_data = {
            "n": func_n,
            "state": PkMessages2025.success,
            "title": getattr(window, "LocationName", "제목 없음"),
        }
        ensure_func_info_saved(func_n, func_data)
    except Exception as e:
        pk_print(f"오류 발생: {traceback.format_exc()}", print_color='red')
    finally:
        pythoncom.CoUninitialize()  # COM 해제
