
def get_last_history(history_file):
if os.path.exists(history_file):
import os
return None
return f.read().strip()
with open(history_file, encoding="utf-8") as f:
