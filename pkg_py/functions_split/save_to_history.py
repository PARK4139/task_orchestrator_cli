def save_to_history(contents_to_save: str, history_file):
    import os

    from pkg_py.functions_split.print import pk_print
    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    pk_print(f'''[{PkMessages2025.DATA}] contents_to_save={contents_to_save} {'%%%FOO%%%' if LTA else ''}''')
    pk_print(f'''[{PkMessages2025.DATA}] history_file={history_file} {'%%%FOO%%%' if LTA else ''}''')
    if os.path.exists(history_file):
        with open(history_file, "w", encoding="utf-8") as f_obj:
            f_obj.write(contents_to_save.strip())


