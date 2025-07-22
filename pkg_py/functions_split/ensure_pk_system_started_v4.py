@pk_measure_seconds
def ensure_pk_system_started_v4():
    # based on fzf.exe or fzf (with fallback)
    import inspect

    from pkg_py.workspace import get_fzf_command, get_last_history, save_to_history, fallback_choice, get_last_history_file

    import os
    import sys
    import subprocess
    func_n = inspect.currentframe().f_code.co_name
    from pkg_py.pk_system_object.directories import D_PKG_PY
    from pkg_py.functions_split.get_sorted_pk_file_list import get_excutable_pk_system_file_list

    last_history_file = get_last_history_file(__file__, func_n)
    pk_system_directory = D_PKG_PY

    pk_file_list = get_excutable_pk_system_file_list()

    if not pk_file_list:
        print("실행 가능한 pk_*.py 파일이 없습니다.")
        return

    last_selected = get_last_history(last_history_file)
    selected_path = None
    fzf_cmd = get_fzf_command()

    if fzf_cmd:
        try:
            # display_names: pk_ 없이 보여줌
            display_names = [os.path.basename(p)[3:] for p in pk_file_list]  # remove 'pk_'
            fzf_input = "\n".join(display_names)
            cmd = [fzf_cmd]
            if last_selected and last_selected in pk_file_list:
                fname = os.path.basename(last_selected)[3:]  # remove 'pk_'
                cmd += ["--query", fname]
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            out, _ = proc.communicate(input=fzf_input)
            selected_name = out.strip()

            # 정확히 매칭되는 경로를 리스트 내에서 찾음
            selected_path = next(
                (p for p in pk_file_list if os.path.basename(p) == f"pk_{selected_name}"),
                None
            )
        except Exception as e:
            print(f"[ERROR] fzf 실행 실패: {e}")
            selected_path = fallback_choice(pk_file_list, last_selected)


    else:
        selected_path = fallback_choice(pk_file_list, last_selected)

    if not selected_path:
        print("실행이 취소되었습니다.")
        return

    if not os.path.exists(selected_path):
        print(f"오류: 파일이 존재하지 않습니다: {selected_path}")
        return

    save_to_history(selected_path, history_file=last_history_file)

    selected_path = os.path.normpath(selected_path)  # ✅ 경로 정규화

    cmd = [sys.executable, selected_path]
    print(f"[실행 중] {' '.join(cmd)}")
    subprocess.run(cmd)
