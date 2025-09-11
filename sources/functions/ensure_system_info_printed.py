from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_system_info_printed():
    import logging

    from sources.functions import ensure_slept, get_os_n
    from sources.functions.ensure_all_import_script_printed import ensure_all_import_script_printed
    from sources.functions.ensure_tasklist_got import get_image_names_from_tasklist, get_tasklist_with_pid
    from sources.functions.ensure_wifi_pw_printed_fixed import ensure_wifi_pw_printed_fixed
    from sources.functions.ensure_wsl_ip_printed import ensure_wsl_ip_printed
    from sources.functions.get_process_names import get_process_names
    from sources.functions.get_process_names_by_window_title import get_process_names_by_window_title
    from sources.functions.get_window_titles import get_window_titles
    from sources.functions.get_wsl_distro_names_installed import get_wsl_distro_names_installed
    from sources.objects.pk_etc import PK_UNDERLINE_HALF

    logging.debug(rf"{PK_UNDERLINE_HALF} os info {PK_UNDERLINE_HALF}")
    os_n = get_os_n()
    logging.debug(rf"os_n={os_n}")

    logging.debug(rf"{PK_UNDERLINE_HALF} window_titles info {PK_UNDERLINE_HALF}")
    for window_title in get_window_titles():
        logging.debug(rf"window_title={window_title}")

    logging.debug(rf"{PK_UNDERLINE_HALF} processes info {PK_UNDERLINE_HALF}")
    process_names = get_process_names()
    for process_name in process_names:
        logging.debug(rf"process_name={process_name}")

    for task in get_tasklist_with_pid():
        logging.debug(rf"task={task}")

    for image_name in get_image_names_from_tasklist():
        logging.debug(rf"image_name={image_name}")

    logging.debug(rf"{PK_UNDERLINE_HALF} single process info {PK_UNDERLINE_HALF}")

    logging.debug(rf"{PK_UNDERLINE_HALF} ai IDE process info {PK_UNDERLINE_HALF}")
    process_names = get_process_names_by_window_title(rf"Gemini - task_orchestrator_cli")
    for process_name in process_names:
        logging.debug(rf"process_name={process_name}")

    logging.debug(rf"{PK_UNDERLINE_HALF} wsl info {PK_UNDERLINE_HALF}")
    wsl_distro_names_installed = get_wsl_distro_names_installed()
    logging.debug(rf"wsl_distro_names_installed={wsl_distro_names_installed}")
    for wsl_distro_name in wsl_distro_names_installed:
        ensure_wsl_ip_printed(wsl_distro_name=wsl_distro_name)

    logging.debug(rf"{PK_UNDERLINE_HALF} network info {PK_UNDERLINE_HALF}")
    wifi_name, wifi_pw = ensure_wifi_pw_printed_fixed()
    logging.debug(rf'wifi_name={wifi_name}')
    logging.debug(rf'wifi_pw={wifi_pw}')
    ensure_slept(seconds=2)

    logging.debug(rf"{PK_UNDERLINE_HALF} python import info {PK_UNDERLINE_HALF}")
    ensure_all_import_script_printed()
