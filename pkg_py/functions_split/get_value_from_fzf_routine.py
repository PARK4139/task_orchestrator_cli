from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.fallback_choice import fallback_choice
from pkg_py.functions_split.get_f_historical import get_history_file
from pkg_py.functions_split.get_fzf_command import get_fzf_command
from pkg_py.functions_split.get_last_history import get_last_history
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.save_to_history import save_to_history
from pkg_py.system_object.directories import D_PKG_HISTORY
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025


def get_value_from_fzf_routine(file_id, options, editable):
    import subprocess
    ensure_pnx_made(pnx=D_PKG_HISTORY, mode="f")
    history_file = get_history_file(file_id=file_id)

    last_selected = get_last_history(history_file)
    ensure_printed(f'''[{PkMessages2025.DATA}] last_selected={last_selected} {'%%%FOO%%%' if LTA else ''}''')
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

        ensure_printed(f'''[{PkMessages2025.DATA}] selected_value={selected_value} {'%%%FOO%%%' if LTA else ''}''')

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
    ensure_printed(f'''[{PkMessages2025.DATA}] contents_to_save={contents_to_save} {'%%%FOO%%%' if LTA else ''}''')
    save_to_history(contents_to_save=contents_to_save, history_file=history_file)
    return selected_value
