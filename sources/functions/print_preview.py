def print_preview(categorized_f_dict):
    import logging
    import logging
    from sources.objects.pk_local_test_activate import LTA
    logging.debug(f'''[ ngram 기반 분류결과(preview) ] {'%%%FOO%%%' if LTA else ''}''')
    for group, files in categorized_f_dict.items():
        f_filtered = []
        for f in files:
            if len(f_filtered) < 10:
                f_filtered.append(f)
            elif len(f_filtered) == 10:
                f_filtered.append("...")
            else:
                pass
        logging.debug(f"\n\U0001F4C2 {group} = {f_filtered}")
