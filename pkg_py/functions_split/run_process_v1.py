
#
# from colorama import init as pk_colorama_init
# pk_colorama_init_once()
def pk_run_process_v1(pk_program_n_seg=None, pk_arg_list=None):
else:
for pk_idx, pk_python_program_pnx in enumerate(pk_python_program_pnx_list):
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.print import pk_print
from pkg_py.system_object.local_test_activate import LTA
if LTA:
if pk_program_n_seg in pk_python_program_pnx:
if pk_program_n_seg:
pk_print(f'''pk_idx={pk_idx} get_nx(pk_python_program_pnx)={get_nx(pk_python_program_pnx)} pk_python_program_n_seg={pk_program_n_seg} {'%%%FOO%%%' if LTA else ''}''', print_color='green')
pk_print(f'''pk_idx={pk_idx} get_nx(pk_python_program_pnx)={get_nx(pk_python_program_pnx)} pk_python_program_n_seg={pk_program_n_seg} {'%%%FOO%%%' if LTA else ''}''', print_color='red')
pk_python_program_pnx_list = get_pk_system_process_pnx_list()
run_pk_system_process_by_idx(pk_idx=int(pk_idx), pk_arg_list=pk_arg_list)
