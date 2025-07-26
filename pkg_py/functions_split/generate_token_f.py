from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def generate_token_f(f, initial_str):
    if not does_pnx_exist(pnx=f):
        ensure_pnx_made(pnx=f, mode="f")
    ensure_printed(f'''f={f}  {'%%%FOO%%%' if LTA else ''}''')
    line_list = get_list_from_f(f=f)
    line_list = get_list_removed_by_removing_runtine(working_list=line_list)
    # ensure_iterable_printed_as_vertical(item_iterable=line_list, item_iterable_n='line_list')
    if len(line_list) == 0:
        token = initial_str
        if initial_str != "":
            ensure_str_writen_to_f(msg=f"{token}\n", f=f, mode="w")
            ensure_printed(str_working=rf'''token is generated token={token}  {'%%%FOO%%%' if LTA else ''}''',
                     print_color='green')
