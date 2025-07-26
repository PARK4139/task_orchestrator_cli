from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed


def should_i_do_cli(title, search_keyword_default=""):
    ensure_printed(f'''{title}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    ensure_printed(f'''search_keyword_default={search_keyword_default}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue")
    if search_keyword_default == "":
        txt_written = input("search_keyword:").strip()
    else:
        txt_written = search_keyword_default
    return txt_written
