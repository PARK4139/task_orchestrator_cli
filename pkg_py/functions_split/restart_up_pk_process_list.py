from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.is_os_windows import is_os_windows

from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.directories import D_PK_WORKING
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def restart_up_pk_process_list():
    import asyncio

    if is_os_windows():
        ensure_command_excuted_to_os("chcp 65001")

    if not is_office_pc():
        cmd_list = [
            rf'explorer "{D_PROJECT}\.venv\Scripts\activate && python {D_PKG_PY}\pk_test.py && deactivate"',
        ]
        for cmd in cmd_list:
            ensure_command_excuted_to_os(cmd=cmd, mode='a')

        f_list = [
            rf"{D_PKG_PY}/pk_assist_to_control_wsl.py",
            rf"{D_PKG_PY}/pk_assist_to_kill_explorer_window_duplicated_list.py",
            rf"{D_PKG_PY}/pk_guide_todo.py",

            # 작업 손실 유의
            rf"{D_PKG_PY}/pk_assist_to_run_mini.py",
            rf"{D_PKG_PY}/pk_ensure_video_loaded_at_losslesscut.py",
            rf"{D_PKG_PY}/pk_assist_to_upload_project.py",
            rf"{D_PKG_PY}/pk_assist_to_ensure_f_list_organized_by_nx_delimiter.py",
            # rf"{D_PKG_PY}/pk_assist_to_ensure_f_list_organized_by_ext.py",
            rf"{D_PKG_PY}/pk_ensure_f_list_organized_by_ngram.py",
            rf"{D_PKG_PY}/pk_ensure_f_list_organized_by_keyword_and_x.py",
            # mkr.
            rf"{D_PKG_PY}/pk_assist_to_lock_os.py",  # *
            rf"{D_PKG_PY}/pk_replace_old_str_in_f_nx.py",
            # rf"{D_PKG_PY}/pk_collect_and_download_magnets.py",
        ]
        for f in f_list:
            ensure_process_killed_by_window_title_seg(window_title_seg=get_nx(f))
        for f in f_list:
            pk_run_process(pk_program_n_seg=get_nx(f))

        # with window : oneshot
        f_list = [
            rf"{D_PKG_PY}/pk_kill_us_keyboard.py",
            # todo : [ATTEMPTED] while block in pk_kill_us_keyboard->> void block
        ]
        for f in f_list:
            asyncio.run(ensure_process_killed_as_async(f=f))
        for f in f_list:
            asyncio.run(pk_run_process_as_async(f=f))
        for f in f_list:
            asyncio.run(ensure_process_killed_as_async(f=f))


    elif is_office_pc():
        kakaowork_ink = rf"{D_HOME}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\카카오워크\카카오워크.lnk"
        pycharm2024_2_4_64_exe = r"C:\Program Files\JetBrains\PyCharm Community Edition 2024.2.4\bin\pycharm64.exe"
        cmd_list = [
            # "cls",
            # 'start "" explorer "https://chatgpt.com/"',
            'explorer "https://chatgpt.com/"',
            rf'explorer "{D_PROJECT}\.venv\Scripts\activate && python C:\Users\Autonomousa2z\Downloads\pk_system\pkg_py\pk_test.py && deactivate"',
            f'explorer "{kakaowork_ink}"',
            f'explorer "https://mail.autoa2z.co.kr/#inbox"',
            f'explorer "https://bb.bbgw.kr/a/in.bb"',
            f'explorer "https://shiftee.io/app/companies/2050081/staff/scheduler#month"',
            f'explorer "https://www.notion.so/a2zaidev/PROD-0ff24ea4c8d14f05a2c70cf17db71851"',  # PROD
            f'explorer "https://www.notion.so/a2zaidev/VSTEST-ce7c24c68d6044aeb8eef8f43fa97632"',  # VSTEST
            f'explorer "https://www.notion.so/a2zaidev/1a797f1bfea08096baa4cf21dfd7ff62"',  # 이슈 트래커
            f'start cmd.exe /k "{pycharm2024_2_4_64_exe}"',
            # f'start cmd.exe /k',  # cmd.exe in venv
        ]
        for cmd in cmd_list:
            ensure_command_excuted_to_os(cmd=cmd, mode='a')

        # without window
        f_list = [
            # f'{D_PROJECT_RELEASE_SERVER}/pk_run_release_server.py',
            rf"{D_PKG_PY}/pk_kill_window_duplicated_list.py",
        ]
        for f in f_list:
            asyncio.run(ensure_process_killed_as_async(f=f))
        for f in f_list:
            asyncio.run(pk_run_process_as_async(f=f, mode_with_window=0))

        # with window
        f_list = [
            rf"{D_PKG_PY}/pk_wsl.py",
        ]
        for f in f_list:
            # ensure_process_killed(cmd_exe_title=rf"f_nx")
            asyncio.run(ensure_process_killed_as_async(f=f))
        for f in f_list:
            asyncio.run(pk_run_process_as_async(f=f))

        # with window : oneshot
        f_list = [
            rf"{D_PKG_PY}/pk_kill_us_keyboard.py",
            # todo : [ATTEMPTED] while block in pk_kill_us_keyboard->> void block
        ]
        for f in f_list:
            asyncio.run(ensure_process_killed_as_async(f=f))
        for f in f_list:
            asyncio.run(pk_run_process_as_async(f=f))
        for f in f_list:
            asyncio.run(ensure_process_killed_as_async(f=f))

        # f_cmd
        # pnx = rf"{D_PROJECT_RELEASE_SERVER}/run_release_server.cmd"
        # pnx = get_pnx_os_style(pnx=pnx)
        # ensure_printed(str_working=rf'''pnx="{pnx}"  {'%%%FOO%%%' if LTA else ''}''')
        # while is_f_locked(pnx):  # 배치f이 잠겨 있는지 확인 후 잠겨 있으면 기다림
        #     ensure_printed(f"File is locked, waiting for 1 second...")
        #     ensure_slept(seconds=1)
        # ensure_command_excuted_to_os(cmd=rf'start "" "{pnx}"', encoding=Encoding.UTF8, mode='a')

        # login_and_filter_and_export_addup()

        # taskkill
        #     tasklist | findstr tv_x64.exe
        # ensure_command_excuted_to_os("tasklist | findstr tv_x64.exe")
        kill_list = [
            # "PowerToys.exe",
            # "powertoys.exe",
            # "KMFtp.exe",
            "TeamViewer.exe",
            "TeamViewer_Service.exe",
            "Telegram.exe",
            # "tv_w32.exe",
            # "tv_x64.exe",
            # "tvnserver.exe",
            # "xlaunch.exe",
            # "vcxsrv.exe",
        ]
        for process_name in kill_list:
            ensure_command_excuted_to_os(f"taskkill /f /im {process_name}")

        # # 11) WSL / SSH 서버 exec
        # # "C:\Windows\System32\bash.exe" -c "sudo service ssh start"
        # ensure_command_excuted_to_os(r'"C:\Windows\System32\bash.exe" -c "sudo service ssh start"')

        # # (2) 콘솔 창 제목 설정
        # # title %~nx0
        # # Python에서 batch 스크립트처럼 %~nx0을 쓰기는 어려우므로, 간단히 문자열을 지정합니다.
        # ensure_command_excuted_to_os("title pk_system_shell_start_up.py")

    # pnx
    pnx_list = [
        D_PROJECT,
        D_PK_WORKING,
        # MEMO_TRASH_BIN_TXT,
        F_MEMO_HOW_PK,
        F_MEMO_WORK_PK,
        F_ALIAS_CMD,
    ]
    for pnx in pnx_list:
        pnx = get_pnx_os_style(pnx)
        if does_pnx_exist(pnx=pnx):
            ensure_command_excuted_to_os(f'explorer "{pnx}"')
