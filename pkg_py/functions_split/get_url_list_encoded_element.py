def get_url_list_encoded_element(working_list):
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA
    import urllib.parse

    ensure_printed(f'''working_list={working_list}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    return [urllib.parse.quote(item) for item in working_list]
