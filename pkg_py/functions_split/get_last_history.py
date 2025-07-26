import os


def get_last_history(history_file):
    if os.path.exists(history_file):
        with open(history_file, encoding="utf-8") as f:
            return f.read().strip()
    return None
