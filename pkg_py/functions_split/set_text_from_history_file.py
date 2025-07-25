
"""Save text to the corresponding history file."""
def set_text_from_history_file(file_id: str, text: str):
file_path = get_history_file_path(file_id)
file_path.write_text(text.strip())
