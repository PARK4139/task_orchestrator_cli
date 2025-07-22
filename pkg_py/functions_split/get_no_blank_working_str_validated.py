from pkg_py.functions_split.pk_print import pk_print


def get_no_blank_working_str_validated(working_str):
    name = working_str.strip()
    if not name:
        pk_print("❌ blank, name not allowed. Please try again.", print_color='red')
        raise ValueError("Input is blank")
    return name
