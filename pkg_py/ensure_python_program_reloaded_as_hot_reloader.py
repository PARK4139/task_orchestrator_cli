import ipdb

from pkg_py.functions_split.ensure_pnx_made import ensure_pnx_made
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_historical import get_history_file
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_sleep import pk_sleep
from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.pk_system_object.map_massages import PkMessages2025
from pkg_py.pk_system_object.directories import D_PKG_HISTORY
from pkg_py.pk_workspace2 import ensure_files_stable_after_change


def get_values_from_fzf_routine(file_id, options, editable):
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
        cmd = [fzf_cmd, "--print-query"] if fzf_cmd else None    #  fzf 창에서 cmd 받을 때
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
        selected_value = out
        pk_print(f'''[{PkMessages2025.DATA}] selected_value={selected_value} {'%%%FOO%%%' if LTA else ''}''')
        if not selected_value:
            print("Selection was cancelled.")
            return None

    except Exception as e:
        print(f"[ERROR] Failed to execute fzf: {e}")
        selected_value = fallback_choice(options, last_selected)

    if selected_value not in options:
        print(f"[WARN] Entered value is not in the option list: {selected_value}")

    contents_to_save =selected_value
    pk_print(f'''[{PkMessages2025.DATA}] contents_to_save={contents_to_save} {'%%%FOO%%%' if LTA else ''}''')
    save_to_history(contents_to_save=contents_to_save, history_file=history_file)
    return selected_value


def get_value_via_fzf_or_history(key_name, file_id, options, editable=False):
    from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
    from pkg_py.pk_system_object.map_massages import PkMessages2025
    # decision = get_value_completed(key_hint=rf"{key_name}=", values=[PkMessages2025.VIA_FZF, PkMessages2025.VIA_HISTORICAL_FILE]) # pk_option
    decision = PkMessages2025.VIA_FZF  # pk_option
    if decision == PkMessages2025.VIA_FZF:
        selected_value = get_values_from_fzf_routine(file_id=file_id, options=options, editable=editable)
        return selected_value
    elif decision == PkMessages2025.VIA_HISTORICAL_FILE:
        selected_value = get_values_from_historical_file_routine(file_id=file_id, key_hint=f'{key_name}=', options_default=options, editable=editable)
        return selected_value
    else:
        selected_value = decision
        return selected_value


def reload_python_program_as_hot_reloader():
    from pkg_py.functions_split.get_pnx_list import get_pnx_list
    from pkg_py.pk_system_object.directories import D_PKG_PY
    from pkg_py.workspace.pk_workspace import pk_ensure_process_killed, is_process_killed
    from pkg_py.workspace.pk_workspace import pk_run_py_system_process_by_pnx
    from pkg_py.functions_split.chcp_65001 import chcp_65001
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_os_n import get_os_n
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_set_from_list import get_set_from_list
    from pkg_py.pk_interface_graphic_user import get_windows_opened
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.pk_system_object.local_test_activate import LTA
    import inspect
    if get_os_n() == 'windows':
        chcp_65001()
    func_n = inspect.currentframe().f_code.co_name

    window_opened_list = get_windows_opened()
    window_opened_set = get_set_from_list(window_opened_list)

    key_name = 'file_to_hot_reload'
    file_list = get_pnx_list(d_working=D_PKG_PY, with_walking=0, filter_option="f")
    file_to_hot_reload = get_value_via_fzf_or_history(key_name=key_name, options=file_list, file_id=get_file_id(key_name, func_n))
    file_to_hot_reload = get_pnx_os_style(file_to_hot_reload)
    pk_print(f'''file_to_hot_reload={file_to_hot_reload} {'%%%FOO%%%' if LTA else ''}''')

    f_monitored_list = [
        file_to_hot_reload,
        # get_pnx_os_style(rf"{D_PKG_PY}/pk_system_blahblah.py"),
    ]
    pnx_to_execute_list = [
        file_to_hot_reload,
    ]
    loop_cnt = 1
    # limit_seconds = 4
    limit_seconds = 1

    window_title_to_kill = None
    while 1:
        if loop_cnt == 1:
            # if window_title_to_kill is None:
            #     window_title_to_kill = get_value_completed(message='window_title_to_kill=', alternative_values=window_opened_set)
            for f in pnx_to_execute_list:
                f = get_pnx_os_style(f)
                window_opened_set.add(get_nx(f))
                # pk_run_process(pk_program_n_seg=get_nx(f))
                file_to_excute = f
                pk_run_py_system_process_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
                # window_title_to_kill = get_nx(f)
                window_title_to_kill = f  # pk_option
            loop_cnt = loop_cnt + 1
            continue
        if not ensure_files_stable_after_change(f_list=f_monitored_list, limit_seconds=limit_seconds):
            pk_print("Detected file changes (step 1)", print_color='green')
            if ensure_files_stable_after_change(f_list=f_monitored_list, limit_seconds=limit_seconds):
                pk_print("Confirmed stable after changes (step 2)", print_color='green')
                for f in pnx_to_execute_list:
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
