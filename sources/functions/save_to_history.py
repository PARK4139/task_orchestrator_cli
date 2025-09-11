from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def save_to_history(contents_to_save: str, history_file):
    import os

    import logging
    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.pk_map_texts import PkTexts
    logging.debug(f'''contents_to_save={contents_to_save} {'%%%FOO%%%' if LTA else ''}''')
    logging.debug(f'''history_file={history_file} {'%%%FOO%%%' if LTA else ''}''')
    if os.path.exists(history_file):
        with open(history_file, "w", encoding="utf-8") as f_obj:
            f_obj.write(contents_to_save.strip())
