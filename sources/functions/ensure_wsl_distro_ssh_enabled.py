from sources.functions.ensure_seconds_measured import ensure_seconds_measured





@ensure_seconds_measured
def ensure_wsl_distro_ssh_enabled():
    import logging
    from functions.ensure_remote_os_as_nopasswd import ensure_remote_os_as_nopasswd
    from functions.ensure_ssh_public_key_to_remote_os import ensure_ssh_public_key_to_remote_os
    from functions.ensure_wsl_distro_session import ensure_wsl_distro_session
    from sources.objects.pk_local_test_activate import LTA
    from dataclasses import asdict

    remote_device_target_config = get_wsl_distro_config()
    ensure_wsl_distro_session(wsl_distro_name=remote_device_target_config.distro_name)
    ensure_ssh_public_key_to_remote_os(**asdict(remote_device_target_config))
    ensure_remote_os_as_nopasswd(**asdict(remote_device_target_config))

    commands_to_execute = [
        "sudo apt update",
        "echo y | sudo apt install build-essential",
        "echo y | sudo apt install libyaml-cpp-dev",
    ]

    # 원격 OS에 여러 명령어를 순차적으로 실행하고 오류를 처리합니다.
    # Lazy import for ensure_command_to_remote_os_with_pubkey
    try:
        from functions.ensure_command_to_remote_os_with_pubkey import ensure_command_to_target_with_pubkey
    except ImportError:
        logging.error("ensure_command_to_remote_os_with_pubkey 함수를 임포트할 수 없습니다.")
        return

    for cmd in commands_to_execute:
        try:
            std_outs, std_err_list = ensure_command_to_target_with_pubkey(cmd=cmd, **asdict(remote_device_target_config))
            logging.debug(f"Command '{cmd}' executed successfully. Stdout: {std_outs}, Stderr: {std_err_list}")
        except Exception as e:
            ip = remote_device_target_config.ip
            port = remote_device_target_config.port
            user_n = remote_device_target_config.user_n
            logging.error(f"Failed to execute command '{cmd}' on remote OS: {e}")
            logging.debug(f"SSH 연결 가이드: ssh -p {port} {user_n}@{ip} {'%%%FOO%%%' if LTA else ''}")
            raise  # Re-raising to indicate failure to the calling function
