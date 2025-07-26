from pkg_py.functions_split.ensure_py_system_process_ran_by_pnx import ensure_py_system_process_ran_by_pnx
from pkg_py.functions_split.measure_seconds import measure_seconds


@measure_seconds
def ensure_pk_system_started_v5():
    from pkg_py.functions_split.fallback_choice import fallback_choice
    from pkg_py.functions_split.get_f_historical import get_history_file
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_fzf_command import get_fzf_command
    from pkg_py.functions_split.get_last_history import get_last_history
    from pkg_py.functions_split.get_refactor_py_file_list import get_refactor_py_file_list
    from pkg_py.functions_split.save_to_history import save_to_history
    from pkg_py.system_object.local_test_activate import LTA

    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front

    from pkg_py.functions_split.ensure_slept import ensure_slept

    import os
    import subprocess
    import inspect
    from pkg_py.functions_split.get_sorted_pk_file_list import get_excutable_pk_system_file_list
    while True:

        func_n = inspect.currentframe().f_code.co_name

        pk_file_list = get_excutable_pk_system_file_list()  # pkg_py 폴더의 py 파일 추가
        pk_file_list += get_refactor_py_file_list()  # refactor 폴더의 py 파일 추가
        if not pk_file_list:
            print("실행 가능한 pk_*.py/refactor/*.py 파일이 없습니다.")
            return

        last_selected_guide_mode = None
        if LTA:
            last_selected_guide_mode = True  # pk_option
        else:
            last_selected_guide_mode = False

        key_name = "last_selected"
        last_selected = None
        history_file = get_history_file(file_id=get_file_id(key_name, func_n))
        if last_selected_guide_mode == True:
            last_selected = get_last_history(history_file)
        file_to_excute = None
        fzf_cmd = get_fzf_command()
        if fzf_cmd:
            try:
                display_names = [os.path.basename(p)[3:] for p in pk_file_list]  # remove 'pk_'
                fzf_input = "\n".join(display_names)
                cmd = [fzf_cmd]
                if last_selected_guide_mode == True:
                    if last_selected and last_selected in pk_file_list:
                        fname = os.path.basename(last_selected)[3:]
                        cmd += ["--query", fname]
                proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
                out, _ = proc.communicate(input=fzf_input)
                selected_name = out.strip()
                file_to_excute = next(
                    (p for p in pk_file_list if os.path.basename(p) == f"pk_{selected_name}"),
                    None
                )
            except Exception as e:
                print(f"[ERROR] fzf 실행 실패: {e}")
                file_to_excute = fallback_choice(pk_file_list, last_selected)
        else:
            file_to_excute = fallback_choice(pk_file_list, last_selected)

        if not file_to_excute:
            print("실행이 취소되었습니다.")
            return

        if not os.path.exists(file_to_excute):
            print(f"오류: 파일이 존재하지 않습니다: {file_to_excute}")
            return

        if last_selected_guide_mode == True:
            save_to_history(contents_to_save=file_to_excute, history_file=history_file)
        file_to_excute = os.path.normpath(file_to_excute)
        file_title = os.path.basename(file_to_excute)

        # 제목에서 pk_ 접두사 제거
        if file_title.startswith("pk_"):
            file_title = file_title[3:]

            ensure_py_system_process_ran_by_pnx(file_to_excute, file_title)
        ensure_slept(milliseconds=500)
        if LTA:
            ensure_window_to_front(window_title_seg=rf"file_to_excute")  # pk_option
            # ensure_window_to_front(window_title_seg=rf"{func_n.replace("_v5", "")}")  # pk_option
        else:
            ensure_window_to_front(window_title_seg=rf"file_to_excute")  # pk_option
