from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def get_pk_token(f_token, text_plain):
    from sources.objects.task_orchestrator_cli_urls import URL_GIT_HUB_TASK_ORCHESTRATOR_CLI_CACHE_SENSITIVE_GIT
    from sources.functions.ensure_pnx_moved import ensure_pnx_moved
    from sources.functions.ensure_pnx_removed import ensure_pnx_removed
    from sources.functions.ensure_repo_cloned_via_git import ensure_repo_cloned_via_git
    from sources.functions.get_text_decoded_from_token_file import get_text_decoded_from_token_file
    from sources.functions.ensure_text_encrypted_to_token_file import ensure_text_encrypted_to_token_file
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE

    from sources.functions.does_pnx_exist import is_pnx_existing
    import logging
    from sources.objects.task_orchestrator_cli_directories import D_PK_RECYCLE_BIN
    from sources.objects.pk_local_test_activate import LTA

    import os

    f_master_key = rf"{D_TASK_ORCHESTRATOR_CLI_SENSITIVE}/task_orchestrator_cli_token_key.toml"

    if not is_pnx_existing(pnx=f_master_key):
        ensure_pnx_removed(D_PK_RECYCLE_BIN)
        ensure_repo_cloned_via_git(repo_url=URL_GIT_HUB_TASK_ORCHESTRATOR_CLI_CACHE_SENSITIVE_GIT, d_dst=D_PK_RECYCLE_BIN)
        f_master_key_cloned = os.path.join(D_PK_RECYCLE_BIN, "task_orchestrator_cli_token_key.toml")
        if not os.path.exists(f_master_key_cloned):
            raise FileNotFoundError(f"Cloned key file not found at: {f_master_key_cloned}")
        ensure_pnx_moved(pnx=f_master_key_cloned, d_dst=D_TASK_ORCHESTRATOR_CLI_SENSITIVE)

    ensure_text_encrypted_to_token_file(f_token=f_token, text_plain=text_plain, f_key=f_master_key)
    text_plain = get_text_decoded_from_token_file(f_token=f_token, f_key=f_master_key)

    if LTA:
        logging.debug(f'''text_plain={text_plain} {'%%%FOO%%%' if LTA else ''}''')

    return text_plain
