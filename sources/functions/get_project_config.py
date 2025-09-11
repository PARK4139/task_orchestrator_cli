import logging


def get_project_config(key: str, initial: str) -> str:
    import os

    path = os.path.join(D_TASK_ORCHESTRATOR_CLI_SENSITIVE, f"pk_token_{key}.toml")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(initial)
        logging.debug(f"[Config] Initialized '{key}' with default '{initial}' in {path}")
        return initial
    with open(path, 'r', encoding='utf-8') as f:
        value = f.readline().strip() or initial
    logging.debug(f"[Config] Loaded '{key}' = '{value}'")
    return value
