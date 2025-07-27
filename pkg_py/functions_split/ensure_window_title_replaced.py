def ensure_window_title_replaced(window_title):
    import os
    return os.system(f"title {window_title}")
