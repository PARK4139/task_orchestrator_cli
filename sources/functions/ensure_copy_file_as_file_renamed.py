from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_copy_file_as_file_renamed(file_to_copy, file_renamed):
    import logging
    import shutil

    from functions.get_caller_n import get_caller_n
    from functions.get_text_red import get_text_red
    from objects.pk_map_texts import PkTexts

    func_n = get_caller_n()
    if file_to_copy.exists():
        if file_renamed.exists():
            file_renamed.unlink()
        shutil.copy2(src=str(file_to_copy), dst=str(file_renamed), follow_symlinks=True)
    else:
        logging.debug(f"{PkTexts.WARNING} Gitignore source '{file_to_copy}' not found. Skipping.")
        return False

    if not file_renamed.exists():
        logging.debug(get_text_red(f"{func_n}() is failed"))
        return False
    else:
        return True
