from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def back_up_pnx_without_venv_and_idea(pnx_working, d_dst, with_timestamp=1):
    # done : compress f_rar without .venv and .idea
    # done : save f_rar without timestamp

    if not does_pnx_exist(pnx=pnx_working):
        ensure_printed(str_working=rf'''not does_pnx_exist  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return

    # 압축
    return compress_pnx_without_venv_and_idea_via_rar(pnx=pnx_working, d_dst=d_dst, with_timestamp=with_timestamp)
