from typing import Optional

from functions import ensure_spoken
from functions.ensure_env_var_reset import ensure_env_var_reset
from functions.ensure_task_orchestrator_cli_env_file_setup import ensure_task_orchestrator_cli_env_file_setup
from sources.functions.ensure_seconds_measured import ensure_seconds_measured

env_path = ensure_task_orchestrator_cli_env_file_setup()


@ensure_seconds_measured
def ensure_env_var_completed_advanced(
        key_name: str,
        func_n,
        mask_log: bool = True,
        sensitive_masking_mode=None,
        options=None,
        history_reset = False
) -> Optional[str]:
    """
    환경 변수에서 값을 가져오거나, 없으면 사용자 입력/옵션 선택을 통해 값을 받습니다.
    선택적으로 .env 파일에 저장하고, 로그에 마스킹 처리할 수 있습니다.
    """

    import logging
    import os

    from dotenv import set_key

    from objects.pk_local_test_activate import LTA

    from functions import ensure_value_completed
    from functions.ensure_matter_device_controlled import ensure_sensitive_info_masked
    from functions.get_env_var_name_id import get_env_var_id

    key_name = key_name.upper()

    if history_reset:
        ensure_env_var_reset(key_name=key_name, func_n=func_n)

    env_var_id = get_env_var_id(key_name, func_n)
    value = os.getenv(env_var_id)
    if not value:
        ensure_spoken(f"해당 환경변수 미등록되어 있습니다. 콘솔에 입력해주세요")

    default_value = None
    if options is None:# Case 1. options가 없는 경우
        if not value:
            logging.warning(f"Environment variable '{key_name}' not found.")
            prompt_message = f"{key_name}="
            value = input(prompt_message).strip()
            if not value:
                logging.error(
                    f"Input for '{key_name}' cannot be empty. Using default fallback if available."
                )
                value = default_value

            # Optional: Ask to save to .env
            if value and value != default_value:
                save_to_env = (
                    input(
                        f"Do you want to save '{key_name}' to your .env file for future use? (y/n): "
                    )
                    .strip()
                    .lower()
                )
                if save_to_env == "y":
                    try:
                        set_key(env_path, env_var_id, value)
                        logging.info(f"'{key_name}' saved to {env_path}")
                    except Exception as e:
                        logging.error(
                            f"Failed to save '{key_name}' to .env file: {e}"
                        )

        # Final fallback
        if not value:
            value = default_value
            if value:
                logging.warning(f"Using default value for '{key_name}': {value}")
            else:
                logging.error(
                    f"No value found for '{key_name}' and no default provided."
                )
                return None
    else: # Case 2. options가 있는 경우
        if not value:  # ENV에 값이 없을 때만 options에서 선택
            logging.warning(f"Environment variable '{key_name}' not found.")
            value = ensure_value_completed(key_hint=key_name, options=options)

            # .env 파일에 저장
            try:
                set_key(env_path, env_var_id, value)
                logging.info(f"'{key_name}' saved to {env_path}")
            except Exception as e:
                logging.error(f"Failed to save '{key_name}' to .env file: {e}")

    if sensitive_masking_mode is None:
        sensitive_masking_mode = True if LTA else False

    log_value = (ensure_sensitive_info_masked(value) if mask_log and sensitive_masking_mode else value)
    logging.info(f"Final value obtained for '{key_name}': {log_value}")
    return value
