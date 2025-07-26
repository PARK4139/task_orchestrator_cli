

def ensure_process_killed_v17(window_title_seg: str):
    import subprocess
    import wmi
    from pkg_py.functions_split.get_window_title import get_window_title
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.functions_split.get_nx import get_nx

    """
    Kill Windows processes that match a specific window title segment in their command line.
    """
    try:
        window_title = get_window_title(window_title_seg=window_title_seg)
        ensure_printed(f"window_title={window_title} {'%%%FOO%%%' if LTA else ''}")

        if not window_title:
            ensure_printed("window_title is empty", print_color="red")
            return

        matched_pids = set()
        c = wmi.WMI()

        for proc in c.query("SELECT ProcessId, CommandLine, Caption FROM Win32_Process"):
            caption = (proc.Caption or "").lower()
            command_line = (proc.CommandLine or "").lower()
            if "cmd.exe" in caption and get_nx(window_title).lower() in command_line:
                matched_pids.add(proc.ProcessId)

        if not matched_pids:
            ensure_printed(f"PK KILL '{window_title}' not found", print_color="red")
            return

        for pid in matched_pids:
            ensure_printed(f"PK KILL PID={pid} window_title={window_title}", print_color="green")
            subprocess.run(['taskkill', '/PID', str(pid), '/T', '/F'],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)

    except Exception as e:
        ensure_printed(f"[ERROR] {e}", print_color="red")
