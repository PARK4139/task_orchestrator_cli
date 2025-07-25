from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_historical import get_history_file
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.functions_split.pk_measure_seconds import pk_measure_seconds
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_sleep import pk_sleep
from pkg_py.system_object.directories import D_PKG_HISTORY
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025


@pk_measure_seconds
def ensure_files_stable_after_change(f_list, stable_seconds_limit, monitoring_interval_seconds=0.2):
    from pkg_py.functions_split.pk_sleep import pk_sleep
    import os
    import time
    from pkg_py.functions_split.get_nx import get_nx

    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style

    f_list = [get_pnx_os_style(f) for f in f_list]

    def get_mtime_map(f_list):
        result = {}
        for f in f_list:
            f_clean = os.path.abspath(f.strip())
            try:
                if os.path.exists(f_clean):
                    result[f] = os.path.getmtime(f_clean)
                else:
                    pk_print(f"❌ 경로 없음: {f_clean}", print_color='red')
            except Exception as e:
                pk_print(f"❌ getmtime 실패: {f_clean} | {e}", print_color='red')
        return result

    f_nx_list = [get_nx(f) for f in f_list]
    pk_print(f"⏳ {stable_seconds_limit}초간 f_nx_list={f_nx_list} 변경 감시 시작...", print_color='white')
    baseline = get_mtime_map(f_list)
    start_time = time.time()

    while True:
        current = get_mtime_map(f_list)
        for f in f_list:
            if f in baseline and f in current and baseline[f] != current[f]:
                pk_print(f"f_list is not stable ({f})")
                return False
        if time.time() - start_time >= stable_seconds_limit:
            pk_print(f"f_list is stable for ({stable_seconds_limit})")
            return True

        pk_sleep(monitoring_interval_seconds)


def get_value_from_fzf_routine(file_id, options, editable):
    import subprocess
    from pkg_py.workspace.pk_workspace import save_to_history, fallback_choice, get_fzf_command, get_last_history
    ensure_pnx_made(pnx=D_PKG_HISTORY, mode="f")
    history_file = get_history_file(file_id=file_id)

    last_selected = get_last_history(history_file)
    pk_print(f'''[{PkMessages2025.DATA}] last_selected={last_selected} {'%%%FOO%%%' if LTA else ''}''')
    selected_value = None
    fzf_cmd = get_fzf_command()

    if editable == True:
        ensure_pnx_opened_by_ext(pnx=history_file)
        ensure_window_to_front(window_title_seg=get_nx(history_file))
        # ipdb.set_trace()

    try:
        cmd = [fzf_cmd, "--print-query"] if fzf_cmd else None
        if not cmd:
            return fallback_choice(options, last_selected)

        if last_selected and last_selected in options:
            cmd += ["--query", last_selected]

        fzf_input = "\n".join(options)
        proc = subprocess.Popen(
            cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True,
            encoding='utf-8',  # pk_option
        )

        out, _ = proc.communicate(input=fzf_input)
        lines = out.strip().split("\n")  # strip은 마지막 개행 제거

        # 기본적으로 fzf --print-query 출력은:
        #   1. 사용자가 입력한 쿼리 (query)
        #   2. 선택된 값 (선택이 있다면)
        query = lines[0] if len(lines) > 0 else ""
        selection = lines[1] if len(lines) > 1 else ""

        # 조건: 선택된 값이 options 중 하나일 경우 → 그 값을 리턴
        # 그렇지 않으면 → 직접 입력한 쿼리(query) 값을 리턴
        if selection in options:
            selected_value = selection
        else:
            selected_value = query

        pk_print(f'''[{PkMessages2025.DATA}] selected_value={selected_value} {'%%%FOO%%%' if LTA else ''}''')

        if not selected_value:
            print("Selection was cancelled.")
            return None

        return selected_value


    except Exception as e:
        print(f"[ERROR] Failed to execute fzf: {e}")
        selected_value = fallback_choice(options, last_selected)

    if selected_value not in options:
        print(f"[WARN] Entered value is not in the option list: {selected_value}")

    contents_to_save = selected_value
    pk_print(f'''[{PkMessages2025.DATA}] contents_to_save={contents_to_save} {'%%%FOO%%%' if LTA else ''}''')
    save_to_history(contents_to_save=contents_to_save, history_file=history_file)
    return selected_value


def get_value_via_fzf_or_history(key_name, file_id, options, editable=False):
    from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
    from pkg_py.system_object.map_massages import PkMessages2025
    # decision = get_value_completed(key_hint=rf"{key_name}=", values=[PkMessages2025.VIA_FZF, PkMessages2025.VIA_HISTORICAL_FILE]) # pk_option
    decision = PkMessages2025.VIA_FZF  # pk_option
    if decision == PkMessages2025.VIA_FZF:
        selected_value = get_value_from_fzf_routine(file_id=file_id, options=options, editable=editable)
        return selected_value
    elif decision == PkMessages2025.VIA_HISTORICAL_FILE:
        selected_value = get_values_from_historical_file_routine(file_id=file_id, key_hint=f'{key_name}=', options_default=options, editable=editable)
        return selected_value
    else:
        selected_value = decision
        return selected_value


def reload_python_program_as_hot_reloader():
    from pkg_py.functions_split.get_pnx_list import get_pnx_list
    from pkg_py.system_object.directories import D_PKG_PY
    from pkg_py.workspace.pk_workspace import pk_ensure_process_killed, is_process_killed
    from pkg_py.workspace.pk_workspace import pk_run_py_system_process_by_pnx
    from pkg_py.functions_split.chcp_65001 import chcp_65001
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_os_n import get_os_n
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_set_from_list import get_set_from_list
    from pkg_py.pk_interface_graphic_user import get_windows_opened
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.system_object.local_test_activate import LTA
    import inspect
    if get_os_n() == 'windows':
        chcp_65001()
    func_n = inspect.currentframe().f_code.co_name

    windows_opened = get_set_from_list(get_windows_opened())

    # pk_option
    # decision = get_value_completed(key_hint=rf"{PkMessages2025.MODE}=", values=[PkMessages2025.FILE_GEN_TIME_STABLE_MODE, PkMessages2025.LOOP_MODE_N_SECONDS_INTERVAL])
    # mode = decision
    # mode = PkMessages2025.FILE_GEN_TIME_STABLE_MODE # pk_option
    mode = PkMessages2025.LOOP_MODE_N_SECONDS_INTERVAL

    key_name = 'file_to_hot_reload'
    file_list = get_pnx_list(d_working=D_PKG_PY, with_walking=0, filter_option="f")
    file_to_hot_reload = get_value_via_fzf_or_history(key_name=key_name, options=file_list, file_id=get_file_id(key_name, func_n))
    file_to_hot_reload = get_pnx_os_style(file_to_hot_reload)
    pk_print(f'''file_to_hot_reload={file_to_hot_reload} {'%%%FOO%%%' if LTA else ''}''')

    files_to_monitor = [
        file_to_hot_reload,
        # get_pnx_os_style(rf"{D_PKG_PY}/pk_system_blahblah.py"),
    ]
    files_to_execute = [
        file_to_hot_reload,
    ]
    loop_cnt = 1
    # stable_seconds_limit = 4 # pk_option
    # stable_seconds_limit = 1 # pk_option
    stable_seconds_limit = 3  # pk_option

    window_title_to_kill = None
    file_to_excute = None

    if mode == PkMessages2025.FILE_GEN_TIME_STABLE_MODE:
        while 1:
            if loop_cnt == 1:
                # if window_title_to_kill is None:
                #     window_title_to_kill = get_value_completed(message='window_title_to_kill=', alternative_values=window_opened_set)
                for f in files_to_execute:
                    f = get_pnx_os_style(f)
                    pk_print(f'''f={f} {'%%%FOO%%%' if LTA else ''}''')

                    windows_opened.add(get_nx(f))
                    # pk_run_process(pk_program_n_seg=get_nx(f))
                    file_to_excute = f
                    pk_run_py_system_process_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
                    # window_title_to_kill = get_nx(f) # pk_option
                    window_title_to_kill = f  # pk_option
                loop_cnt = loop_cnt + 1
                continue
            if not ensure_files_stable_after_change(f_list=files_to_monitor, stable_seconds_limit=1):
                pk_print("Detected file changes (step 1)", print_color='green')
                if ensure_files_stable_after_change(f_list=files_to_monitor, stable_seconds_limit=stable_seconds_limit):
                    pk_print("Confirmed stable after changes (step 2)", print_color='green')
                    for f in files_to_execute:
                        pk_print("Killing old process (step 3)", print_color='green')
                        pk_ensure_process_killed(window_title=get_nx(window_title_to_kill))
                        if not is_process_killed(window_title_seg=get_nx(f)):
                            pk_print("Old process still alive, retrying kill (step 4)", print_color='green')
                            pk_ensure_process_killed(window_title=get_nx(window_title_to_kill))
                        else:
                            pk_print("Old process terminated successfully (step 5)", print_color='green')
                        file_to_excute = f
                        pk_run_py_system_process_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
            else:
                pk_print("No change detected, waiting... (step 6)", print_color='green')
                continue
    elif mode == PkMessages2025.LOOP_MODE_N_SECONDS_INTERVAL:
        while 1:
            if loop_cnt == 1:
                # if window_title_to_kill is None:
                #     window_title_to_kill = get_value_completed(message='window_title_to_kill=', alternative_values=window_opened_set)
                for f in files_to_execute:
                    f = get_pnx_os_style(f)
                    pk_print(f'''f={f} {'%%%FOO%%%' if LTA else ''}''')

                    windows_opened.add(get_nx(f))
                    # pk_run_process(pk_program_n_seg=get_nx(f))
                    file_to_excute = f
                    pk_run_py_system_process_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
                    # window_title_to_kill = get_nx(f)  # pk_option
                    window_title_to_kill = f  # pk_option
                loop_cnt = loop_cnt + 1
                continue
            for f in files_to_execute:
                pk_ensure_process_killed(window_title=get_nx(window_title_to_kill))
                while 1:
                    if not is_process_killed(window_title_seg=get_nx(f)):
                        pk_ensure_process_killed(window_title=get_nx(window_title_to_kill))
                        file_to_excute = f
                    else:
                        break
                pk_run_py_system_process_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
            # pk_sleep(seconds=2) # pk_option
            pk_sleep(seconds=3)  # pk_option
            # pk_sleep(seconds=5) # pk_option


def ensure_window_os_variable_path_deduplicated():
    import os

    current_path = os.environ.get("PATH", "")
    path_list = current_path.split(";")

    seen = set()
    cleaned_paths = []

    for path in path_list:
        path = path.strip()
        if path and path.lower() not in seen:
            seen.add(path.lower())
            cleaned_paths.append(path)

    final_path = ";".join(cleaned_paths)

    if len(final_path) > 1024:
        print("[WARNING] PATH is too long. 'setx' may truncate it.")

    result = os.system(f'setx PATH "{final_path}"')
    if result == 0:
        print("[SUCCESS] System PATH deduplicated and updated successfully.")
    else:
        print("[ERROR] Failed to update system PATH.")

    print("\n[PATH] Final deduplicated PATH entries:")
    for i, p in enumerate(cleaned_paths, 1):
        print(f"[PATH_ENTRY {str(i).zfill(2)}] {p}")


def update_system_path_with_deduplication(additional_path: str = None):
    import os

    current_path = os.environ.get("PATH", "")
    path_list = current_path.split(";")

    seen = set()
    cleaned_paths = []

    for path in path_list:
        path = path.strip()
        if path and path.lower() not in seen:
            seen.add(path.lower())
            cleaned_paths.append(path)

    if additional_path:
        ap = additional_path.strip()
        if ap and ap.lower() not in seen:
            cleaned_paths.append(ap)

    final_path = ";".join(cleaned_paths)

    if len(final_path) > 1024:
        print("PATH too long! setx may truncate it.")

    os.system(f'setx PATH "{final_path}"')
    print("PATH updated with deduplication.")


def ensure_os_path_added():
    import os
    import subprocess
    from pathlib import Path


    """
    표준 라이브러리와 시스템 명령(setx, 쉘 프로파일 편집)을 사용해
    중복을 제거하고 지정한 경로를 PATH 환경 변수에
    현재 프로세스와 영구 등록(Windows Registry 또는 쉘 프로파일)합니다.
    또한 사용자가 입력했던 경로를 홈 디렉토리의 ힴ토리 파일에 기록합니다.
    """
    os_path_to_add = input("추가할 경로를 입력하세요: ").strip()

    if not os.path.isdir(os_path_to_add):
        print(f"경로가 존재하지 않습니다: {os_path_to_add}")
        return

    # 히스토리 파일 설정
    hist_file = Path.home() / ".ensure_os_path_history.txt"
    history = []
    if hist_file.exists():
        history = [line.strip() for line in hist_file.read_text(encoding="utf-8").splitlines() if line.strip()]

    # 히스토리에 추가 (중복 제거)
    if os_path_to_add in history:
        history.remove(os_path_to_add)
    history.insert(0, os_path_to_add)
    hist_file.write_text("\n".join(history), encoding="utf-8")

    # 현재 PATH 가져와 항목별 분리
    current_paths = os.environ.get("PATH", "").split(os.pathsep)
    unique_paths = []
    for p in current_paths:
        if p and p not in unique_paths and os.path.isdir(p):
            unique_paths.append(p)

    # 새 경로 추가
    if os_path_to_add not in unique_paths:
        unique_paths.append(os_path_to_add)

    # 새로운 PATH 문자열 생성
    new_path_str = os.pathsep.join(unique_paths)

    # 현재 프로세스에 적용
    os.environ["PATH"] = new_path_str
    print("✅ PATH가 업데이트되었습니다.")
    print(f"새 PATH: {new_path_str}")

    # 영구 등록
    if os.name == "nt":
        try:
            # setx는 1024자 제한이 있으므로 주의
            subprocess.run(["setx", "PATH", new_path_str], check=True, shell=True)
            print("✅ Windows 레지스트리에 영구 등록되었습니다.")
            print("새로운 CMD 창을 열어 변경 사항을 확인하세요.")
        except subprocess.CalledProcessError as e:
            print(f"❌ setx 실행 중 오류 발생: {e}")
    else:
        shell = os.path.basename(os.environ.get("SHELL", ""))
        profile_map = {"bash": ".bashrc", "zsh": ".zshrc"}
        profile = Path.home() / profile_map.get(shell, ".profile")
        export_line = f'\n# ensure_os_path_added 추가\nexport PATH="{new_path_str}"\n'
        try:
            text = profile.read_text(encoding="utf-8")
            # 이미 추가된 export_line이 없을 때만 붙임
            if export_line.strip() not in text:
                profile.write_text(text + export_line, encoding="utf-8")
            print(f"✅ {profile.name}에 export 라인이 추가되었습니다.")
            print("새 터미널을 열어 변경 사항을 확인하세요.")
        except Exception as e:
            print(f"❌ 프로파일에 추가 중 오류 발생: {e}")
