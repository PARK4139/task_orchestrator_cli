from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def pk_back_up_pnx_without_venv_and_idea(pnx_working, d_dst, with_timestamp=1):
    # done : compress f_rar without .venv and .idea
    # done : save f_rar without timestamp

    if not does_pnx_exist(pnx=pnx_working):
        pk_print(working_str=rf'''not does_pnx_exist  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        return

    # 압축
    return compress_pnx_without_venv_and_idea_via_rar(pnx=pnx_working, d_dst=d_dst, with_timestamp=with_timestamp)
