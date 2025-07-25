
# done : compress f_rar without .venv and .idea
# done : save f_rar without timestamp
# 압축
def pk_back_up_pnx_without_venv_and_idea(pnx_working, d_dst, with_timestamp=1):
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.functions_split.print import pk_print
from pkg_py.system_object.local_test_activate import LTA
if not does_pnx_exist(pnx=pnx_working):
pk_print(str_working=rf'''not does_pnx_exist  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
return
return compress_pnx_without_venv_and_idea_via_rar(pnx=pnx_working, d_dst=d_dst, with_timestamp=with_timestamp)
