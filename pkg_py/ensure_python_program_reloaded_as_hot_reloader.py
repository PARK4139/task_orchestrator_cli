

import ipdb

from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.functions_split.get_window_title_list import get_window_title_list
from pkg_py.functions_split.print_iterable_as_vertical import print_iterable_as_vertical


def get_value_from_fzf(key_name, values):
    import inspect
    import os
    import subprocess

    from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
    from pkg_py.functions_split.get_file_id import get_file_id
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.pk_system_object.PkMessages2025 import PkMessages2025
    from pkg_py.workspace.pk_workspace import save_to_history, fallback_choice, get_fzf_command, get_last_history
    if not values:
        print("선택할 수 있는 항목이 없습니다.")
        return None

    decision = get_value_completed(key_hint=rf"{key_name}=", values=[PkMessages2025.VIA_FZF])
    # if decision == PkMessages2025.VIA_FZF:
    #     ensure_pk_system_exit_silent()

    func_n = inspect.currentframe().f_code.co_name
    base_dir = os.path.abspath(os.path.dirname(__file__))
    key_name = "value_of_fzf"
    history_file = os.path.join(base_dir, f"{get_file_id(key_name, func_n)}.history")

    last_selected = get_last_history(history_file)
    selected_value = None
    fzf_cmd = get_fzf_command()

    try:
        # fzf로 선택
        cmd = [fzf_cmd] if fzf_cmd else None
        if not cmd:
            return fallback_choice(values, last_selected)

        if last_selected and last_selected in values:
            cmd += ["--query", last_selected]

        fzf_input = "\n".join(values)
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        out, _ = proc.communicate(input=fzf_input)
        selected_value = out.strip()

        if not selected_value:
            print("선택이 취소되었습니다.")
            return None

    except Exception as e:
        print(f"[ERROR] fzf 실행 실패: {e}")
        selected_value = fallback_choice(values, last_selected)

    if selected_value not in values:
        print(f"[WARN] 선택된 값이 유효하지 않습니다: {selected_value}")
        return None

    save_to_history(selected_value, history_file)
    return selected_value


def reload_python_program_as_hot_reloader():
    import os

    from pkg_py.functions_split.ensure_pk_system_exit_silent import ensure_pk_system_exit_silent
    from pkg_py.functions_split.get_pnx_list import get_pnx_list
    from pkg_py.pk_system_object.directories import D_PKG_PY
    from pkg_py.workspace.pk_workspace import pk_kill_process, is_process_killed
    from pkg_py.workspace.pk_workspace import pk_run_py_system_process_by_pnx
    from pkg_py.functions_split.chcp_65001 import chcp_65001
    from pkg_py.functions_split.ensure_console_cleared import ensure_console_cleared
    from pkg_py.functions_split.ensure_f_list_change_stable import ensure_f_list_change_stable
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_os_n import get_os_n
    from pkg_py.functions_split.get_pk_system_process_pnx_list import get_pk_system_process_pnx_list
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.functions_split.get_set_from_list import get_set_from_list
    from pkg_py.functions_split.get_window_opened_list import get_window_opened_list
    from pkg_py.functions_split.pk_print import pk_print
    from pkg_py.pk_system_object.Local_test_activate import LTA
    from pkg_py.pk_system_object.state_via_database import PkSqlite3DB
    import inspect
    if get_os_n() == 'windows':
        chcp_65001()

    func_n = inspect.currentframe().f_code.co_name
    # f.py
    # pnx_monitored_list = [
    #     # D_PROJECT,
    #     # rf"{__file__}",
    #     # rf"{D_PKG_PY}/test_monitor_process_cpu.py",
    #     # rf"{D_PROJECT}/pkg_friday/__init__.py",
    #     # rf"{D_PKG_PY}/pk_test.py",cmake
    # ]
    # pnx_to_excute_list = [
    #     rf"{D_PKG_PY}/test_build_and_exec_cmake_project.py",
    # ]
    # # monitoring_interval_seconds = 0.1
    # monitoring_interval_seconds = 1
    # while 1:
    #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
    #         # cmd_f_in_cmd_exe_like_person(cmd_prefix='python',  f=rf"{f_test_py}")
    #         for f in pnx_to_excute_list:
    #             asyncio.run(pk_kill_process_as_async(f=f))
    #         for f in pnx_to_excute_list:
    #             asyncio.run(pk_run_process_as_async(f=f))

    # f.cpp
    # pnx_monitored_list = [
    #     rf"{D_PKG_PY}/pk_hot_reloader.py",
    #     rf"{D_PKG_PY}/pk_build_and_exec_cmake_project.py",
    #     # rf"{PKG_CMAKE_PROJECT}/src/.vscode",
    #     rf"{D_PKG_CMAKE_PROJECT}/CMakeLists.txt",
    #     rf"{D_PKG_CMAKE_PROJECT}/src/config.yaml",
    #     rf"{D_PKG_CMAKE_PROJECT}/src/core.cpp",
    #     rf"{D_PKG_CMAKE_PROJECT}/src/core.h",
    #     rf"{D_PKG_CMAKE_PROJECT}/src/main.cpp",
    # ]
    # pnx_to_excute_list = [
    #     rf"{D_PKG_PY}/pk_build_and_exec_cmake_project.py",
    # ]
    # # monitoring_interval_seconds = 0.1
    # # monitoring_interval_seconds = 5
    # monitoring_interval_seconds = 1
    # while 1:
    #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
    #         # cmd_f_in_cmd_exe_like_person(cmd_prefix='python',  f=rf"{f_test_py}")
    #         for f in pnx_to_excute_list:
    #             asyncio.run(kill_process_as_async(f=f))
    #         for f in pnx_to_excute_list:
    #             asyncio.run(pk_run_process_as_async(f=f))

    # project_streamlit
    # pnx_monitored_list = [
    #     rf"{D_PKG_PY}/pk_hot_reloader.py",
    #     rf"{D_PROJECT_STREAMLIT}",
    # ]
    # pnx_to_excute_list = [
    #     rf"{D_PROJECT_STREAMLIT}/main.py",
    # ]
    # monitoring_interval_seconds = 1
    # while 1:
    #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
    #         for f in pnx_to_excute_list:
    #             asyncio.run(pk_kill_process_as_async(f=f))
    #         for f in pnx_to_excute_list:
    #             cmd = f'start "" streamlit run {f}'
    #             cmd_to_os(cmd=cmd, mode='a')

    # project_fastapi
    # wsl_distro_n = 'Ubuntu-24.04'
    # config_remote_os = {
    #     'port': ensure_and_get_wsl_port(wsl_distro_n),
    #     'ip': get_wsl_ip(wsl_distro_n),
    #     'user_n': get_wsl_user_n(wsl_distro_n),
    #     'pw': get_wsl_pw(wsl_distro_n),
    #     'local_ssh_public_key': os.path.join(os.environ["USERPROFILE"], ".ssh", "id_ed25519.pub"),
    #     'local_private_key': os.path.expanduser("~/.ssh/id_ed25519"),
    # }
    # ip = config_remote_os['ip']
    # pw = config_remote_os['pw']
    # port = config_remote_os['port']
    # user_n = config_remote_os['user_n']
    # local_ssh_public_key = config_remote_os['local_ssh_public_key']
    # local_private_key = config_remote_os['local_private_key']
    # project_pnx = get_pnx_unix_style_for_wsl(pnx=D_PROJECT_CMAKE)
    # if LTA:
    #     pk_print(f'''{STAMP_TRY_GUIDE} ssh -p {port} {user_n}@{ip} {'%%%FOO%%%' if LTA else ''}''')
    #
    # ensure_ssh_public_key_to_remote_os(ip=ip, port=port, user_n=user_n, pw=pw, local_ssh_public_key=local_ssh_public_key)
    # ensure_remote_os_as_nopasswd(ip=ip, port=port, user_n=user_n, pw=pw, local_private_key=local_private_key)
    #
    # pnx_monitored_list = [
    #     rf"{D_PKG_PY}/pk_hot_reloader.py",
    #     rf"{D_PROJECT_FASTAPI}",
    #     rf"{D_PROJECT}/project_fastapi.Dockerfile",
    #     rf"{D_PROJECT}/requirements.txt",
    # ]
    # pnx_to_excute_list = [
    #     rf"{D_PROJECT}/project_fastapi.Dockerfile",
    # ]
    # monitoring_interval_seconds = 1
    # while 1:
    #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
    #         for f in pnx_to_excute_list:
    #             asyncio.run(pk_kill_process_as_async(f=f))
    #         for f in pnx_to_excute_list:
    #             f = get_pnx_unix_style_for_wsl(f)
    #             cmd = f'docker build -t image_project_fastapi -f "{f}" .'
    #             pk_print(f'''cmd={cmd} %%%FOO%%%''')
    #             std_out_list, std_err_list = cmd_to_remote_os_with_pubkey(ip=ip, port=port, user_n=user_n, local_private_key=local_private_key, cmd=cmd)
    #             print_iterable_as_vertical(item_iterable=std_out_list, item_iterable_n="std_out_list")
    #             print_iterable_as_vertical(item_iterable=std_err_list, item_iterable_n="std_err_list")
    #             # build_and_run_docker_image(f=rf'{D_PROJECT}/test.Dockerfile')

    # f.py with pk_test.py
    # pnx_monitored_list = [
    #     rf"{D_PKG_PY}/pk_test.py",
    # ]
    # pnx_to_excute_list = [
    #     rf"{D_PKG_PY}/pk_test.py",
    # ]
    # # monitoring_interval_seconds = 0.1
    # monitoring_interval_seconds = 1
    # while 1:
    #     if does_f_changed(pnx_list=pnx_monitored_list, monitoring_interval_seconds=monitoring_interval_seconds, pnx_changed_cnt_limit=1):
    #         # cmd_f_in_cmd_exe_like_person(cmd_prefix='python',  f=rf"{f_test_py}")
    #         for f in pnx_to_excute_list:
    #             asyncio.run(pk_kill_process_as_async(f=f))
    #         for f in pnx_to_excute_list:
    #             asyncio.run(pk_run_process_as_async(f=f))

    # f.py with pk_test.py way 2
    window_opened_list = get_window_opened_list()
    window_opened_set = get_set_from_list(window_opened_list)

    pk_system_process_pnx = get_pk_system_process_pnx_list()
    # last_history_file = get_last_history_file(__file__, func_n)
    # last_selected = get_last_history(last_history_file)

    db = PkSqlite3DB()
    func_n = inspect.currentframe().f_code.co_name
    LAST_HISTORY_PREFIX = "LAST_HISTORY : "

    # key_name = "last_selected"
    # last_selected = db.get_values(db_id=db.get_id(key_name, func_n)) or ""
    # last_selected = last_selected or ""
    # last_selected = last_selected.replace(f"{LAST_HISTORY_PREFIX}", "")
    # db.reset_values(db_id=db.get_id(key_name, func_n))
    # last_selected = last_selected.strip()
    # last_selected = get_pnx_os_style(last_selected)
    # pk_print(f'''last_selected={last_selected} {'%%%FOO%%%' if LTA else ''}''')
    # key_name = "last_selected"
    # db.set_values(db_id=db.get_id(key_name, func_n), values=last_selected.strip())
    # ensure_pk_system_exit_silent()  # todo

    # key_name = "file_to_hot_reload"
    # f_historical = get_f_historical(file_id=get_file_id(key_name, func_n))
    # values_default = get_list_calculated(origin_list=[f"{LAST_HISTORY_PREFIX}{last_selected}"], plus_list=get_values_from_historical_file(f_historical=f_historical) + pk_system_process_pnx, minus_list=[LAST_HISTORY_PREFIX], dedup=True)
    # values_default = get_list_calculated(origin_list=pk_system_process_pnx, dedup=True) # pk_option
    # pk_print(f'''values_default={values_default} {'%%%FOO%%%' if LTA else ''}''')
    # ensure_pk_system_exit_silent() # pk_option
    # values_optional = [F_TEST_PY] + get_list_calculated(origin_list=get_values_from_historical_file(f_historical=f_historical) + pk_system_process_pnx, dedup=True) # pk_option
    # values_optional = [F_TEST_PY] + pk_system_process_pnx  # pk_option
    # file_to_hot_reload = get_value_completed(key_hint='file_to_hot_reload=', values=values_optional)

    key_name = 'file_to_hot_reload'
    file_list = get_pnx_list(d_working=D_PKG_PY, with_walking=0, filter_option="f")
    file_to_hot_reload = get_value_from_fzf(key_name=key_name, values=file_list)
    file_to_hot_reload = get_pnx_os_style(file_to_hot_reload)
    pk_print(f'''file_to_hot_reload={file_to_hot_reload} {'%%%FOO%%%' if LTA else ''}''')
    # save_to_history(contents_to_save=file_to_hot_reload, history_file=last_history_file)

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
        if not ensure_f_list_change_stable(f_list=f_monitored_list, limit_seconds=limit_seconds):
            pk_print("step 1", print_color='green')
            if ensure_f_list_change_stable(f_list=f_monitored_list, limit_seconds=limit_seconds):
                pk_print("step 2", print_color='green')
                # window_tilte_to_kill_list = []
                for f in pnx_to_execute_list:
                    pk_print("step 3", print_color='green')
                    pk_kill_process(window_title=get_nx(window_title_to_kill))
                    if not is_process_killed(window_title_seg=get_nx(f)):
                        pk_print("step 4", print_color='green')
                        pk_kill_process(window_title=get_nx(window_title_to_kill))
                        # pk_kill_process(window_title=window_title_to_kill) # 의도치 않았는데 cmd 모두종료되나?
                        # break
                    else:
                        pk_print("step 5", print_color='green')
                        # break
                    file_to_excute = f
                    pk_run_py_system_process_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
                    # run_pk_python_program_by_path(pnx=file_to_excute)
        else:
            pk_print("step 6", print_color='green')
            ensure_console_cleared()
            continue
