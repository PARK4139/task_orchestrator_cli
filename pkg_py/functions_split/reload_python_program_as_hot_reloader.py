from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
from pkg_py.functions_split.ensure_files_stable_after_change import ensure_files_stable_after_change
from pkg_py.functions_split.ensure_process_killed import ensure_process_killed
from pkg_py.functions_split.ensure_py_system_process_ran_by_pnx import ensure_py_system_process_ran_by_pnx
from pkg_py.functions_split.ensure_slept import ensure_slept
from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_value_via_fzf_or_history import get_value_via_fzf_or_history
from pkg_py.functions_split.is_process_killed import is_process_killed
from pkg_py.system_object.directories import D_PK_FUNCTIONS_SPLIT
from pkg_py.system_object.map_massages import PkMessages2025


def reload_python_program_as_hot_reloader():
    from pkg_py.functions_split.get_pnx_list import get_pnx_list
    from pkg_py.system_object.directories import D_PKG_PY
    # from pkg_py.workspace.pk_workspace import ensure_py_system_process_ran_by_pnx
    from pkg_py.functions_split.chcp_65001 import chcp_65001
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_os_n import get_os_n
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_set_from_list import get_set_from_list
    from pkg_py.pk_interface_graphic_user import get_windows_opened
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    import inspect
    if get_os_n() == 'windows':
        chcp_65001()
    func_n = inspect.currentframe().f_code.co_name

    windows_opened = get_set_from_list(get_windows_opened())

    # pk_option
    # decision = get_value_completed(key_hint=rf"{PkMessages2025.MODE}=", values=[PkMessages2025.FILE_GEN_TIME_STABLE_MODE, PkMessages2025.LOOP_MODE_N_SECONDS_INTERVAL])
    # mode = decision
    mode = PkMessages2025.FILE_GEN_TIME_STABLE_MODE  # pk_option
    # mode = PkMessages2025.LOOP_MODE_N_SECONDS_INTERVAL  # pk_option

    key_name = 'file_to_monitor'
    file_list = get_pnx_list(d_working=D_PK_FUNCTIONS_SPLIT, with_walking=0, filter_option="f")
    file_list += get_pnx_list(d_working=D_PKG_PY, with_walking=0, filter_option="f")
    file_to_monitor = get_value_via_fzf_or_history(key_name=key_name, options=file_list, file_id=get_file_id(key_name, func_n))
    file_to_monitor = get_pnx_os_style(file_to_monitor)
    ensure_printed(f'''file_to_monitor={file_to_monitor} {'%%%FOO%%%' if LTA else ''}''')

    key_name = 'file_to_excute'
    file_list = get_pnx_list(d_working=D_PKG_PY, with_walking=0, filter_option="f")
    file_to_excute = get_value_via_fzf_or_history(key_name=key_name, options=file_list, file_id=get_file_id(key_name, func_n))
    file_to_excute = get_pnx_os_style(file_to_excute)
    ensure_printed(f'''file_to_excute={file_to_excute} {'%%%FOO%%%' if LTA else ''}''')

    files_to_monitor = [
        file_to_monitor,
        # get_pnx_os_style(rf"{D_PKG_PY}/pk_system_blahblah.py"),
    ]
    files_to_execute = [
        file_to_excute,
    ]
    loop_cnt = 1
    # stable_seconds_limit = 4 # pk_option
    # stable_seconds_limit = 1 # pk_option
    stable_seconds_limit = 3  # pk_option

    window_title_to_kill = None
    file_to_excute = None

    if mode == PkMessages2025.FILE_GEN_TIME_STABLE_MODE:
        while 1:
            ensure_console_cleared()
            if loop_cnt == 1:
                # if window_title_to_kill is None:
                #     window_title_to_kill = get_value_completed(message='window_title_to_kill=', alternative_values=window_opened_set)
                for f in files_to_execute:
                    f = get_pnx_os_style(f)
                    ensure_printed(f'''f={f} {'%%%FOO%%%' if LTA else ''}''')

                    windows_opened.add(get_nx(f))
                    # pk_run_process(pk_program_n_seg=get_nx(f))
                    file_to_excute = f
                    ensure_py_system_process_ran_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
                    window_title_to_kill = get_nx(f)  # pk_option
                    # window_title_to_kill = f  # pk_option
                loop_cnt = loop_cnt + 1
                continue
            if not ensure_files_stable_after_change(f_list=files_to_monitor, stable_seconds_limit=1):
                ensure_printed("Detected file changes (step 1)", print_color='green')
                if ensure_files_stable_after_change(f_list=files_to_monitor, stable_seconds_limit=stable_seconds_limit):
                    ensure_printed("Confirmed stable after changes (step 2)", print_color='green')
                    for f in files_to_execute:
                        ensure_printed("Killing old process (step 3)", print_color='green')
                        ensure_process_killed(window_title=window_title_to_kill)
                        if not is_process_killed(window_title_seg=get_nx(f)):
                            ensure_printed("Old process still alive, retrying kill (step 4)", print_color='green')
                            ensure_process_killed(window_title=window_title_to_kill)
                        else:
                            ensure_printed("Old process terminated successfully (step 5)", print_color='green')
                        file_to_excute = f
                        ensure_py_system_process_ran_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
            else:
                ensure_printed("No change detected, waiting... (step 6)", print_color='green')
                continue
    elif mode == PkMessages2025.LOOP_MODE_N_SECONDS_INTERVAL:
        while 1:
            if loop_cnt == 1:
                # if window_title_to_kill is None:
                #     window_title_to_kill = get_value_completed(message='window_title_to_kill=', alternative_values=window_opened_set)
                for f in files_to_execute:
                    f = get_pnx_os_style(f)
                    ensure_printed(f'''f={f} {'%%%FOO%%%' if LTA else ''}''')

                    windows_opened.add(get_nx(f))
                    # pk_run_process(pk_program_n_seg=get_nx(f))
                    file_to_excute = f
                    ensure_py_system_process_ran_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
                    window_title_to_kill = get_nx(f)  # pk_option
                    # window_title_to_kill = f  # pk_option
                loop_cnt = loop_cnt + 1
                continue
            for f in files_to_execute:
                ensure_process_killed(window_title=window_title_to_kill)
                while 1:
                    if not is_process_killed(window_title_seg=get_nx(f)):
                        ensure_process_killed(window_title=window_title_to_kill)
                        file_to_excute = f
                    else:
                        break
                ensure_py_system_process_ran_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
            # ensure_slept(seconds=2) # pk_option
            ensure_slept(seconds=3)  # pk_option
            # ensure_slept(seconds=5) # pk_option
