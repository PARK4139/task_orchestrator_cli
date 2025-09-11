from pathlib import Path



def save_target_tree_to_f_toml(f, remote_device_target_config):
    import inspect
    from functions.ensure_value_completed_advanced import ensure_value_completed_advanced

    import logging

    from functions import ensure_pnx_made
    from functions.ensure_command_to_remote_os import ensure_command_to_target
    from functions.get_wsl_distro_port import get_wsl_distro_port
    from functions.ensure_dockerfile_writen import ensure_dockerfile_writen
    from functions.ensure_remote_os_as_nopasswd import ensure_remote_os_as_nopasswd
    from functions.ensure_ssh_public_key_to_remote_os import ensure_ssh_public_key_to_remote_os
    from functions.ensure_wsl_distro_enabled import ensure_wsl_distro_enabled
    from functions.ensure_wsl_distro_session import ensure_wsl_distro_session
    from functions.get_n import get_n
    from functions.get_wsl_distro_names_installed import get_wsl_distro_names_installed
    from functions.get_wsl_ip import get_wsl_ip
    from functions.get_wsl_pw import get_wsl_pw
    from functions.get_wsl_user_n import get_wsl_user_n
    from objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_FASTAPI, D_TASK_ORCHESTRATOR_CLI, D_USERPROFILE
    from sources.functions.get_nx import get_nx
    from sources.functions.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
    from sources.objects.pk_local_test_activate import LTA

    import os


    f = Path(f)
    target_device_tree = get_remote_tree(**remote_device_target_config, d_path="~/")
    target_device_tree_list = target_device_tree.split('\n')
    data = {"tree": {"paths": target_device_tree_list}}
    set_data_to_f_toml(data, f)
