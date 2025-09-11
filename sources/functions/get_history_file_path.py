from pathlib import Path


def get_history_file_path(file_id: str) -> Path:
    history_dir = Path.home() / ".git_config_history"
    history_dir.mkdir(parents=True, exist_ok=True)
    return history_dir / f"history_{file_id}.txt"


