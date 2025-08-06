from pkg_py.functions_split.ensure_printed import ensure_printed


def get_no_blank_str_working_validated(str_working):
    name = str_working.strip()
    if not name:
        ensure_printed(" blank, name not allowed. Please try again.", print_color='red')
        raise ValueError("Input is blank")
    return name
