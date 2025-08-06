from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.etc import


@ensure_seconds_measured
def run_pk_system_process_by_path(pnx, pk_arg_list=None):
    from pkg_py.system_object.local_test_activate import LTA
    # pk_#
    from pkg_py.functions_split.ensure_tmux_pk_session_removed import ensure_tmux_pk_session_removed
    from pkg_py.functions_split.is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.functions_split.is_os_windows import is_os_windows
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
    from pkg_py.functions_split.get_cmd_to_autorun import get_cmd_to_autorun
    from pkg_py.functions_split.ensure_printed import ensure_printed
    import os
    import subprocess

    if pk_arg_list is None:
        pk_arg_list = []

    cmd_to_run = "python"
    # nx = get_nx(pnx) # pk_option
    # nx = rf"{pk_}{get_nx(pnx)}" # pk_option
    nx = get_nx(pnx).replace(pk_, "") # pk_option

    if is_os_windows():

        cmd_to_autorun = get_cmd_to_autorun()
        arg_cnt_allowed = 2
        while len(pk_arg_list) <= arg_cnt_allowed:
            pk_arg_list.append('')

        if pk_arg_list[2] in ['-ww', '--without window']:
            cmd = f'cmd.exe /c "{cmd_to_autorun} && title {nx} && {cmd_to_run} {pnx}"'
            ensure_command_excuted_to_os(cmd=cmd, mode='a', mode_with_window=0)
        else:
            cmd = f'start "" cmd.exe /c "{cmd_to_autorun} && title {nx} && {cmd_to_run} {pnx}"'
            ensure_command_excuted_to_os(cmd=cmd, mode='a', mode_with_window=1)

        if LTA:
            ensure_printed(f'{'[ TRY GUIDE ]'} {cmd} %%%FOO%%%')

    elif is_os_wsl_linux():

        is_tmux = bool(os.environ.get("TMUX"))
        full_cmd = f"{cmd_to_run} {pnx}"
        if LTA:
            full_cmd += "; sleep 99999"

        if is_tmux:
            current_pane = subprocess.check_output("tmux display -p '#{pane_id}'", shell=True).decode().strip()
            ensure_command_excuted_to_os("tmux split-window -v")
            ensure_command_excuted_to_os(f"tmux send-keys -t {current_pane} '{full_cmd}' C-m")
            if LTA:
                ensure_printed(f"{'[ TRY GUIDE ]'} tmux split → send-keys: {full_cmd}")
        else:
            tmux_session = nx.replace(".", "_")
            ensure_tmux_pk_session_removed(tmux_session)
            ensure_command_excuted_to_os(f"tmux new-session -s {tmux_session} -d '{full_cmd}'")
            ensure_command_excuted_to_os(f"tmux attach-session -t {tmux_session}")
            if LTA:
                ensure_printed(f"{'[ TRY GUIDE ]'} tmux new-session: {full_cmd}")
    else:
        # 기타 리눅스
        cmd = f"{cmd_to_run} {pnx}"
        ensure_command_excuted_to_os(cmd=cmd)
        if LTA:
            ensure_printed(f"{'[ TRY GUIDE ]'} {cmd}")
