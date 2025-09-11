def get_url_list_encoded_element(working_list):
    import logging
    from sources.objects.pk_local_test_activate import LTA
    import urllib.parse

    logging.debug(f'''working_list={working_list}  {'%%%FOO%%%' if LTA else ''}''')
    return [urllib.parse.quote(item) for item in working_list]
