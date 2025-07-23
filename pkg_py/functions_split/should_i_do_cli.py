from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def should_i_do_cli(title, search_keyword_default=""):
    pk_print(f'''{title}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    pk_print(f'''search_keyword_default={search_keyword_default}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    if search_keyword_default == "":
        txt_written = input("search_keyword:").strip()
    else:
        txt_written = search_keyword_default
    return txt_written
