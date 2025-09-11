# from resources.workspace.pk_workspace import update_system_path_with_deduplication, ensure_os_env_path_deduplicated


def ensure_os_env_sys_variables_applied():
    # 아...이거 좋은데. python 설치에 의존됨... 결국 batch 로 작성을 해야하나?
    from pathlib import Path
    from sources.objects.task_orchestrator_cli_directories import (
        D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES, D_TASK_ORCHESTRATOR_CLI_SENSITIVE, D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES, D_PK_MEMO, D_DOWNLOADS,
        D_TASK_ORCHESTRATOR_CLI, D_PK_WORKING, D_BUSINESS_DEMO,
    )
    from sources.objects.task_orchestrator_cli_files import (
        F_UV_EXE, F_UV_ZIP, F_PK_ALIAS_MACROS_TXT,
    )
    import os
    import subprocess
    import logging

    ensure_os_env_path_deduplicated()

    PK_URL = "https://github.com/astral-sh/uv/releases/download/0.6.12/uv-x86_64-pc-windows-msvc.zip"
    env_vars = {
        "PK_URL": PK_URL,
        "D_DOWNLOADS": D_DOWNLOADS,
        "D_TASK_ORCHESTRATOR_CLI": D_TASK_ORCHESTRATOR_CLI,
        "D_PK_WORKING": D_PK_WORKING,
        "D_PK_MEMO": D_PK_MEMO,
        "D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES": D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES,
        "D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES": D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES,
        "D_TASK_ORCHESTRATOR_CLI_SENSITIVE": D_TASK_ORCHESTRATOR_CLI_SENSITIVE,
        "F_UV_ZIP": F_UV_ZIP,
        "F_UV": F_UV_EXE,
        "F_PK_ALIAS_MACROS_TXT": F_PK_ALIAS_MACROS_TXT,
        "D_BUSINESS_DEMO": D_BUSINESS_DEMO,
    }
    env_vars = {k: Path(v) for k, v in env_vars.items()}

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
            logging.warning(f"Failed to setx {key}: {e}")

    # Append D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES to PATH (session)
    D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES = Path(env_vars['D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES'])
    if D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES not in os.environ.get("PATH", ""):
        os.environ["PATH"] += ";" + D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES
        session_logs.append(("PATH", f"+= {D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES}"))

    try:
        update_system_path_with_deduplication(D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES)
        setx_logs.append(("PATH", f"+= {D_TASK_ORCHESTRATOR_CLI_OS_LAYER_RESOURCES}"))

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
        logging.warning(f"Failed to update PATH: {e}")

    # ▶ [SESSION] 출력
    logging.debug("[SESSION] Environment Variables (Current Session)")
    for key, value in session_logs:
        logging.debug(f"[SESSION] Set {key.ljust(24)} = {value}")

    # ▶ [SETX] 출력
    logging.debug("[SETX] Environment Variables (Next Session)")
    for key, msg in setx_logs:
        logging.debug(f"[SETX]    {key.ljust(24)} {msg}")

    # ▶ [REGISTRY] 결과 출력
    logging.debug("[REGISTRY] Confirmation Results")
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
        logging.debug(formatted)

    ensure_os_env_path_deduplicated()

    # [PATH] 중복 제거 후 출력
    logging.debug("[PATH] Current PATH entries (session)")
    path_entries = os.environ.get("PATH", "").split(";")
    seen = set()
    deduped_entries = []
    for p in path_entries:
        p_clean = p.strip()
        if p_clean and p_clean.lower() not in seen:
            seen.add(p_clean.lower())
            deduped_entries.append(p_clean)

    for i, entry in enumerate(deduped_entries, 1):
        logging.debug(f"[PATH_ENTRY {str(i).zfill(2)}] {entry}")
