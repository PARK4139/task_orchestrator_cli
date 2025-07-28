# from pkg_py.workspace.pk_workspace import update_system_path_with_deduplication, ensure_window_os_path_deduplicated


def ensure_os_env_sys_variables_applied():
    # 아...이거 좋은데. python 설치에 의존됨... 결국 batch 로 작성을 해야하나?
    from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
    from pkg_py.system_object.directories import (
        D_PKG_WINDOWS, D_PKG_TXT, D_PKG_WINDOWS, D_PK_MEMO, D_DOWNLOADS,
        D_PK_SYSTEM, D_PK_WORKING, D_AUTO_UTILITY,
    )
    from pkg_py.system_object.files import (
        F_UV_EXE, F_UV_ZIP, F_PK_ALIAS_MACROS_TXT,
    )
    import os
    import subprocess
    from pkg_py.functions_split.ensure_printed import ensure_printed

    ensure_window_os_path_deduplicated()

    PK_URL = "https://github.com/astral-sh/uv/releases/download/0.6.12/uv-x86_64-pc-windows-msvc.zip"
    env_vars = {
        "PK_URL": PK_URL,
        "D_DOWNLOADS": D_DOWNLOADS,
        "D_PK_SYSTEM": D_PK_SYSTEM,
        "D_PK_WORKING": D_PK_WORKING,
        "D_PK_MEMO": D_PK_MEMO,
        "D_PKG_WINDOWS": D_PKG_WINDOWS,
        "D_PKG_WINDOWS": D_PKG_WINDOWS,
        "D_PKG_TXT": D_PKG_TXT,
        "F_UV_ZIP": F_UV_ZIP,
        "F_UV_EXE": F_UV_EXE,
        "F_PK_ALIAS_MACROS_TXT": F_PK_ALIAS_MACROS_TXT,
        "D_AUTO_UTILITY": D_AUTO_UTILITY,
    }
    env_vars = {k: get_pnx_os_style(v) for k, v in env_vars.items()}

    registry_logs = []
    session_logs = []
    setx_logs = []

    for key, value in env_vars.items():
        os.environ[key] = value
        session_logs.append((key, value))

        try:
            subprocess.run(["setx", key, value], check=True, capture_output=True)
            setx_logs.append((key, "Registered for next session"))

            completed = subprocess.run(
                ["reg", "query", "HKCU\\Environment", "/v", key],
                capture_output=True, text=True
            )
            if completed.returncode == 0:
                lines = completed.stdout.strip().splitlines()
                result_line = lines[-1] if lines else "(no result)"
                registry_logs.append((key, result_line))
            else:
                registry_logs.append((key, "Failed to confirm"))
        except subprocess.CalledProcessError as e:
            ensure_printed(f"[ERROR] Failed to setx {key}: {e}", print_color="red")

    # Append D_PKG_WINDOWS to PATH (session)
    D_PKG_WINDOWS = get_pnx_os_style(env_vars['D_PKG_WINDOWS'])
    if D_PKG_WINDOWS not in os.environ.get("PATH", ""):
        os.environ["PATH"] += ";" + D_PKG_WINDOWS
        session_logs.append(("PATH", f"+= {D_PKG_WINDOWS}"))

    try:
        update_system_path_with_deduplication(D_PKG_WINDOWS)
        setx_logs.append(("PATH", f"+= {D_PKG_WINDOWS}"))

        completed = subprocess.run(
            ["reg", "query", "HKCU\\Environment", "/v", "PATH"],
            capture_output=True, text=True
        )
        if completed.returncode == 0:
            lines = completed.stdout.strip().splitlines()
            result_line = lines[-1] if lines else "(no result)"
            registry_logs.append(("PATH", result_line))
        else:
            registry_logs.append(("PATH", "Failed to confirm"))
    except subprocess.CalledProcessError as e:
        ensure_printed(f"[ERROR] Failed to update PATH: {e}", print_color="red")

    # ▶ [SESSION] 출력
    ensure_printed("\n[SESSION] Environment Variables (Current Session)", print_color="green")
    for key, value in session_logs:
        ensure_printed(f"[SESSION] Set {key.ljust(24)} = {value}", print_color="green")

    # ▶ [SETX] 출력
    ensure_printed("\n[SETX] Environment Variables (Next Session)", print_color="blue")
    for key, msg in setx_logs:
        ensure_printed(f"[SETX]    {key.ljust(24)} {msg}", print_color="blue")

    # ▶ [REGISTRY] 결과 출력
    ensure_printed("\n[REGISTRY] Confirmation Results", print_color="cyan")
    parsed_logs = []
    for key, raw_line in registry_logs:
        try:
            parts = raw_line.strip().split(None, 2)
            reg_type = parts[1] if len(parts) >= 2 else "???"
            reg_value = parts[2] if len(parts) >= 3 else raw_line
        except Exception:
            reg_type = "???"
            reg_value = raw_line
        parsed_logs.append((key, reg_type, reg_value))

    max_key_len = max(len(key) for key, _, _ in parsed_logs)
    max_type_len = max(len(tp) for _, tp, _ in parsed_logs)

    for key, reg_type, reg_value in parsed_logs:
        formatted = (
            f"[REGISTRY] {key.ljust(max_key_len)} → "
            f"{reg_type.ljust(max_type_len)}  {reg_value}"
        )
        ensure_printed(formatted, print_color="cyan")

    # [PATH] 중복 제거 후 출력
    ensure_printed("\n[PATH] Current PATH entries (session)", print_color="cyan")
    path_entries = os.environ.get("PATH", "").split(";")
    seen = set()
    deduped_entries = []
    for p in path_entries:
        p_clean = p.strip()
        if p_clean and p_clean.lower() not in seen:
            seen.add(p_clean.lower())
            deduped_entries.append(p_clean)

    for i, entry in enumerate(deduped_entries, 1):
        ensure_printed(f"[PATH_ENTRY {str(i).zfill(2)}] {entry}", print_color="white")
