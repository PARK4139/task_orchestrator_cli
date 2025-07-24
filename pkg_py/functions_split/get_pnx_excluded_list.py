from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style


def get_pnx_excluded_list(d_working_list, exclusion_list):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    f_func_n_txt = rf"{D_PKG_TXT}/{func_n}.txt"
    f_func_n_txt = get_pnx_os_style(f_func_n_txt)
    ensure_pnx_made(pnx=f_func_n_txt, mode='f')
    pk_print(f'''func_n={func_n}  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(f'''f_func_n_txt={f_func_n_txt}  {'%%%FOO%%%' if LTA else ''}''')
    pk_print(f'''d_working_list={d_working_list}  {'%%%FOO%%%' if LTA else ''}''')
    make_pnx_interested_list_to_f_txt_x(d_working_list=d_working_list, exclusion_list=exclusion_list)
    return get_list_from_f(f=f_func_n_txt)
