

from pkg_py.simple_module.part_002_pk_measure_seconds import pk_measure_seconds


@pk_measure_seconds
def run_pk_python_program_by_path(pnx, pk_arg_list=None):
    from pkg_py.pk_system_layer_100_Local_test_activate import LTA
    from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
    from pkg_py.simple_module.part_001_ensure_tmux_pk_session_removed import ensure_tmux_pk_session_removed
    from pkg_py.simple_module.part_001_is_os_wsl_linux import is_os_wsl_linux
    from pkg_py.simple_module.part_002_is_os_windows import is_os_windows
    from pkg_py.simple_module.part_005_get_nx import get_nx
    from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
    from pkg_py.simple_module.part_013_get_cmd_to_autorun import get_cmd_to_autorun
    from pkg_py.simple_module.part_014_pk_print import pk_print
    import os
    import subprocess

    if pk_arg_list is None:
        pk_arg_list = []

    cmd_to_run = "python"
    nx = get_nx(pnx)

    if is_os_windows():

        cmd_to_autorun = get_cmd_to_autorun()
        arg_cnt_allowed = 2
        while len(pk_arg_list) <= arg_cnt_allowed:
            pk_arg_list.append('')

        if pk_arg_list[2] in ['-ww', '--without window']:
            cmd = f'cmd.exe /c "{cmd_to_autorun} && title {nx} && {cmd_to_run} {pnx}"'
            cmd_to_os(cmd=cmd, mode='a', mode_with_window=0)
        else:
            cmd = f'start "" cmd.exe /c "{cmd_to_autorun} && title {nx} && {cmd_to_run} {pnx}"'
            cmd_to_os(cmd=cmd, mode='a', mode_with_window=1)

        if LTA:
            pk_print(f'{STAMP_TRY_GUIDE} {cmd} %%%FOO%%%')

    elif is_os_wsl_linux():

        is_tmux = bool(os.environ.get("TMUX"))
        full_cmd = f"{cmd_to_run} {pnx}"
        if LTA:
            full_cmd += "; sleep 99999"

        if is_tmux:
            current_pane = subprocess.check_output("tmux display -p '#{pane_id}'", shell=True).decode().strip()
            cmd_to_os("tmux split-window -v")
            cmd_to_os(f"tmux send-keys -t {current_pane} '{full_cmd}' C-m")
            if LTA:
                pk_print(f"{STAMP_TRY_GUIDE} tmux split → send-keys: {full_cmd}")
        else:
            tmux_session = nx.replace(".", "_")
            ensure_tmux_pk_session_removed(tmux_session)
            cmd_to_os(f"tmux new-session -s {tmux_session} -d '{full_cmd}'")
            cmd_to_os(f"tmux attach-session -t {tmux_session}")
            if LTA:
                pk_print(f"{STAMP_TRY_GUIDE} tmux new-session: {full_cmd}")
    else:
        # 기타 리눅스
        cmd = f"{cmd_to_run} {pnx}"
        cmd_to_os(cmd=cmd)
        if LTA:
            pk_print(f"{STAMP_TRY_GUIDE} {cmd}")
