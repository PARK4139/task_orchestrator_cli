def sanitize_filename(name):
    import re
    return re.sub(r'[^a-zA-Z0-9_]', '_', name)
