from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.etc import PK_UNDERLINE


def ensure_seconds_measured_to_exec_function_via_cprofile():
    import cProfile
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    ensure_printed(str_working=rf'''{PK_UNDERLINE}{func_n}() s %%%FOO%%%''', print_color='blue')
    cProfile.run('function_to_test()')
    ensure_printed(str_working=rf'''{PK_UNDERLINE}{func_n}() e %%%FOO%%%''', print_color='blue')