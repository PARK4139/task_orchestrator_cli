from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def check_min_non_null_or_warn(*args, func_n="UNKNOWN", arg_none_required=1):
    non_null_count = sum(arg is not None for arg in args)
    if non_null_count < arg_none_required:
        pk_print(
            rf"{func_n}() 동작 조건 불충족 (요구 조건: 최소 {arg_none_required}개, 현재 {non_null_count}개)  {'%%%FOO%%%' if LTA else ''}",
            print_color='red'
        )
        return False
    return True
