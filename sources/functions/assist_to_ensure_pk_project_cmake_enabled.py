from functions.get_wsl_distro_config import get_wsl_distro_config
from functions.get_wsl_distro_name_installed import get_wsl_distro_name_installed


def assist_to_ensure_project_cmake_executed_at_remote_device_target():
    from functions.build_project_cmake import build_project_cmake
    from functions.ensure_command_to_remote_os_with_pubkey import ensure_command_to_target_with_pubkey
    from functions.exec_project_cmake import exec_project_cmake
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_CMAKE

    import logging

    from functions.ensure_remote_os_as_nopasswd import ensure_remote_os_as_nopasswd
    from functions.ensure_ssh_public_key_to_remote_os import ensure_ssh_public_key_to_remote_os
    from functions.ensure_wsl_distro_session import ensure_wsl_distro_session
    from sources.objects.pk_local_test_activate import LTA

    wsl_distro_name = get_wsl_distro_name_installed()

    ensure_wsl_distro_session(wsl_distro_name=wsl_distro_name)

    wsl_distro_config = get_wsl_distro_config()

    ensure_ssh_public_key_to_remote_os(**wsl_distro_config)
    ensure_remote_os_as_nopasswd(**wsl_distro_config)

    project_pnx = D_TASK_ORCHESTRATOR_CLI_CMAKE
    try:
        std_outs, std_err_list = ensure_command_to_target_with_pubkey(cmd=rf"sudo apt update", **wsl_distro_config)
        std_outs, std_err_list = ensure_command_to_target_with_pubkey(cmd=rf"echo y | sudo apt install build-essential", **wsl_distro_config)
        std_outs, std_err_list = ensure_command_to_target_with_pubkey(cmd=rf"echo y | sudo apt install libyaml-cpp-dev", **wsl_distro_config)
    except:
        logging.debug(f'''{'[ TRY GUIDE ]'} ssh -p {wsl_distro_config.port} {wsl_distro_config.user_n}@{wsl_distro_config.ip} {'%%%FOO%%%' if LTA else ''}''')

    build_project_cmake(project_pnx=project_pnx, **wsl_distro_config)
    exec_project_cmake(project_pnx=project_pnx, **wsl_distro_config)
