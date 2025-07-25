def get_text_from_history_file(file_id: str) -> str | None:
    file_path = get_history_file_path(file_id)
    if not file_path.exists():
        file_path.write_text("")  # create an empty file
        return None
    content = file_path.read_text().strip()
    return content if content else None


