def ensure_process_killed_by_image_name(image_name, force_kill=False, timeout=10):
    from pkg_py.functions_split import ensure_command_excuted_to_os

    # return ensure_command_excuted_to_os(f'wmic process where name="{image_name}" delete ')
    # return ensure_process_killed_by_pid(image_name, force_kill, timeout)
    return ensure_command_excuted_to_os(f'taskkill /f /im "{image_name}"')  # fast
