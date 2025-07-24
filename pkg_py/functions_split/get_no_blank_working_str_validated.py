from pkg_py.functions_split.pk_print import pk_print


def get_no_blank_str_working_validated(str_working):
    name = str_working.strip()
    if not name:
        pk_print("❌ blank, name not allowed. Please try again.", print_color='red')
        raise ValueError("Input is blank")
    return name
