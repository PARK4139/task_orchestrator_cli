
#     window_title_to_kill = get_value_completed(message='window_title_to_kill=', alternative_values=window_opened_set)
# decision = get_value_completed(key_hint=rf"{PkMessages2025.MODE}=", values=[PkMessages2025.FILE_GEN_TIME_STABLE_MODE, PkMessages2025.LOOP_MODE_N_SECONDS_INTERVAL])
# from pkg_py.workspace.pk_workspace import pk_run_py_system_process_by_pnx
# get_pnx_os_style(rf"{D_PKG_PY}/pk_system_blahblah.py"),
# if window_title_to_kill is None:
# mode = PkMessages2025.FILE_GEN_TIME_STABLE_MODE # pk_option
# mode = decision
# pk_option
# pk_run_process(pk_program_n_seg=get_nx(f))
# pk_sleep(seconds=2) # pk_option
# pk_sleep(seconds=5) # pk_option
# stable_seconds_limit = 1 # pk_option
# stable_seconds_limit = 4 # pk_option
# window_title_to_kill = get_nx(f)  # pk_option
# window_title_to_kill = get_nx(f) # pk_option
]
break
chcp_65001()
continue
def reload_python_program_as_hot_reloader():
elif mode == PkMessages2025.LOOP_MODE_N_SECONDS_INTERVAL:
else:
f = get_pnx_os_style(f)
file_list = get_pnx_list(d_working=D_PKG_PY, with_walking=0, filter_option="f")
file_to_excute = None
file_to_excute = f
file_to_hot_reload = get_pnx_os_style(file_to_hot_reload)
file_to_hot_reload = get_value_via_fzf_or_history(key_name=key_name, options=file_list, file_id=get_file_id(key_name, func_n))
file_to_hot_reload,
files_to_execute = [
files_to_monitor = [
for f in files_to_execute:
from pkg_py.functions_split.chcp_65001 import chcp_65001
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_os_n import get_os_n
from pkg_py.functions_split.get_pnx_list import get_pnx_list
from pkg_py.functions_split.get_pnx_os_style import get_pnx_os_style
from pkg_py.functions_split.get_set_from_list import get_set_from_list
from pkg_py.functions_split.print import pk_print
from pkg_py.pk_interface_graphic_user import get_windows_opened
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.system_object.local_test_activate import LTA
func_n = inspect.currentframe().f_code.co_name
if ensure_files_stable_after_change(f_list=files_to_monitor, stable_seconds_limit=stable_seconds_limit):
if get_os_n() == 'windows':
if loop_cnt == 1:
if mode == PkMessages2025.FILE_GEN_TIME_STABLE_MODE:
if not ensure_files_stable_after_change(f_list=files_to_monitor, stable_seconds_limit=1):
if not is_process_killed(window_title_seg=get_nx(f)):
import inspect
key_name = 'file_to_hot_reload'
loop_cnt = 1
loop_cnt = loop_cnt + 1
mode = PkMessages2025.LOOP_MODE_N_SECONDS_INTERVAL
pk_ensure_process_killed(window_title=get_nx(window_title_to_kill))
pk_print("Confirmed stable after changes (step 2)", print_color='green')
pk_print("Detected file changes (step 1)", print_color='green')
pk_print("Killing old process (step 3)", print_color='green')
pk_print("No change detected, waiting... (step 6)", print_color='green')
pk_print("Old process still alive, retrying kill (step 4)", print_color='green')
pk_print("Old process terminated successfully (step 5)", print_color='green')
pk_print(f'''f={f} {'%%%FOO%%%' if LTA else ''}''')
pk_print(f'''file_to_hot_reload={file_to_hot_reload} {'%%%FOO%%%' if LTA else ''}''')
pk_run_py_system_process_by_pnx(file_to_excute=file_to_excute, file_title=get_nx(file_to_excute))
pk_sleep(seconds=3)  # pk_option
stable_seconds_limit = 3  # pk_option
while 1:
window_title_to_kill = None
window_title_to_kill = f  # pk_option
windows_opened = get_set_from_list(get_windows_opened())
windows_opened.add(get_nx(f))
