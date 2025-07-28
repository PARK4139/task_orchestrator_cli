


# from pkg_py.system_object.is_os_windows import is_os_windows
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux

from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
from pkg_py.functions_split.is_os_windows import is_os_windows
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed


def run_pk_system_process_by_idx_v1(pk_idx, pk_arg_list):
    #
    import os
    import subprocess

    cmd_to_run = None
    cmd = None
    if pk_arg_list is None:
        pk_arg_list = []
    if LTA:
        ensure_printed(f'''pk_idx={pk_idx} {'%%%FOO%%%' if LTA else ''}''')
        for idx, _ in enumerate(pk_arg_list):
            ensure_printed(f'''pk_arg_list[{idx}]={pk_arg_list[idx]} {'%%%FOO%%%' if LTA else ''}''')
    available_pk_python_program_pnx = get_available_pk_python_program_pnx(pk_idx)
    if pk_arg_list is None:
        pk_arg_list = []  # ✅ 빈 리스트로 대체
    # if get_x(available_pk_python_program_pnx) == '.py':
    #     cmd_to_run = 'python'
    cmd_to_run = 'uv run python'
    cmd_to_run = 'python'
    if LTA:
        ensure_printed(f'''pk_idx={pk_idx} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''get_nx(pk_python_program_pnx_working)={get_nx(available_pk_python_program_pnx)} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''cmd_to_run={cmd_to_run} {'%%%FOO%%%' if LTA else ''}''')
    if is_os_windows():

        cmd_to_autorun = get_cmd_to_autorun()
        if LTA:
            ensure_printed(f'''pk_arg_list={pk_arg_list} {'%%%FOO%%%' if LTA else ''}''')
        arg_cnt_allowed = 2
        while len(pk_arg_list) <= arg_cnt_allowed:
            pk_arg_list.append('')
        if pk_arg_list[2] in ['-ww', '--without window']:
            if LTA:
                cmd = f'cmd.exe /k "{cmd_to_autorun} && title {get_nx(available_pk_python_program_pnx)}&& {cmd_to_run} {available_pk_python_program_pnx}"'
            else:
                cmd = f'cmd.exe /c "{cmd_to_autorun} && title {get_nx(available_pk_python_program_pnx)}&& {cmd_to_run} {available_pk_python_program_pnx}"'
            # ensure_command_excuted_to_os(cmd=cmd, mode_with_window=0)
            ensure_command_excuted_to_os(cmd=cmd, mode='a', mode_with_window=0)
        else:  # with new window
            if LTA:
                cmd = f'start "" cmd.exe /k "{cmd_to_autorun} && title {get_nx(available_pk_python_program_pnx)}&& {cmd_to_run} {available_pk_python_program_pnx}"'
            else:
                cmd = f'start "" cmd.exe /c "{cmd_to_autorun} && title {get_nx(available_pk_python_program_pnx)}&& {cmd_to_run} {available_pk_python_program_pnx}"'
            #         ensure_command_excuted_to_os(cmd=cmd, mode_with_window=1)
            ensure_command_excuted_to_os(cmd=cmd, mode='a', mode_with_window=1)
        if LTA:
            ensure_printed(f'''{STAMP_TRY_GUIDE} {cmd} {'%%%FOO%%%' if LTA else ''}''')
    if is_os_wsl_linux():

        tmux_upper_pane_active = True
        is_tmux = bool(os.environ.get("TMUX"))
        full_cmd = f"{cmd_to_run} {available_pk_python_program_pnx}"
        if LTA:
            full_cmd += "; sleep 99999"
        if is_os_wsl_linux():

            if is_tmux:
                # 현재 페인 ID 저장
                current_pane = subprocess.check_output("tmux display -p '#{pane_id}'", shell=True).decode().strip()

                # 아래쪽 페인 split
                ensure_command_excuted_to_os("tmux split-window -v")

                # 위쪽 페인을 다시 활성화할지 여부
                if tmux_upper_pane_active:
                    ensure_command_excuted_to_os(f"tmux select-pane -t {current_pane}")

                # 명령어 전송 (기본적으로 위쪽 페인으로 보냄)
                ensure_command_excuted_to_os(f"tmux send-keys -t {current_pane} '{full_cmd}' C-m")
                return
            else:
                # tmux 밖이면: 새 세션 생성 후 attach
                tmux_session = get_nx(available_pk_python_program_pnx).replace(".", "_")
                ensure_tmux_pk_session_removed(tmux_session)
                ensure_command_excuted_to_os(f"tmux new-session -s {tmux_session} -d '{full_cmd}'")
                ensure_command_excuted_to_os(f"tmux attach-session -t {tmux_session}")
                return
        else:
            if is_tmux:
                current_pane = subprocess.check_output("tmux display -p '#{pane_id}'", shell=True).decode().strip()
                ensure_command_excuted_to_os("tmux split-window -v")
                ensure_command_excuted_to_os(f"tmux send-keys -t {current_pane} '{full_cmd}' C-m")
                return
            else:
                tmux_session = get_nx(available_pk_python_program_pnx).replace(".", "_")
                ensure_tmux_pk_session_removed(tmux_session)
                ensure_command_excuted_to_os(f"tmux new-session -s {tmux_session} -d '{full_cmd}'")
                ensure_command_excuted_to_os(f"tmux attach-session -t {tmux_session}")
                return

        # tmux_session = get_nx(available_pk_python_program_pnx).replace(".", "_")
        # ensure_tmux_pk_session_removed(tmux_session)
        #
        # # (A) 이미 tmux 내부에서 실행 중이라면: 현재 활성 페인만 분할해 실행
        # if os.environ.get("TMUX"):

        #     # 수직 분할: -v, 수평 분할: -h 로 바꿀 수 있음
        #     split_flag = "-v"
        #     # LTA 모드라면 끝에 sleep 추가
        #     sleep_cmd = "; sleep 99999" if LTA else ""
        #     ensure_command_excuted_to_os(cmd=(
        #         f"tmux split-window {split_flag} "
        #         # f"'clear && {cmd_to_run} {available_pk_python_program_pnx}{sleep_cmd}'"
        #         f"'{cmd_to_run} {available_pk_python_program_pnx}{sleep_cmd}'"
        #     ))
        #     return
        #
        # # (B) tmux 밖에서 실행 중이라면: new-session → split → attach
        # tmux_session = get_nx(available_pk_python_program_pnx).replace(".", "_")
        # ensure_tmux_pk_session_removed(tmux_session)
        #
        # # 새 세션 생성 & 첫 페인에서 실행
        # ensure_command_excuted_to_os(cmd=(f"tmux new-session -s {tmux_session} -d '{cmd_to_run} {available_pk_python_program_pnx}'"))
        # # 수직 분할 & 아래 페인에서 동일 명령 실행
        # # ensure_command_excuted_to_os(cmd=(f"tmux split-window -v -t {tmux_session} '{cmd_to_run} {available_pk_python_program_pnx}'"))
        # # 세션에 연결
        # ensure_command_excuted_to_os(cmd=f"tmux attach-session -t {tmux_session}")

        # run_pk_for_wsl_linux(
        #     cmd_to_autorun="cmd.exe",
        #     cmd_to_run="uv run python",
        #     available_pk_python_program_pnx=available_pk_python_program_pnx,
        #     pk_arg_list=pk_arg_list,
        #     LTA=True
        # )
    else:
        # run_pk_on_linux(
        #     cmd_to_autorun="source ~/.bashrc",
        #     cmd_to_run="uv run python",
        #     available_pk_python_program_pnx=available_pk_python_program_pnx,
        #     pk_arg_list=pk_arg_list,
        #     LTA=True
        # )
        pass
