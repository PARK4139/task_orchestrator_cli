
# cmd_to_os(f'taskkill /f /pid {pid}', debug_mode=debug_mode)
# function_arg_names= [param.name for param in inspect.signature(process_kill).parameters.values()] # fail
None_count = Nones.count(None)
Nones = [img_name, pid]
cmd_to_os(f'taskkill /f /im "{img_name}"')
cmd_to_os(f'taskkill /f /pid {pid}')
cmd_to_os(f'wmic process where name="{img_name}" delete ')
def kill_process(img_name=None, pid=None):
func_n = inspect.currentframe().f_code.co_name
if None_count == 0:
if None_count == 1:
if None_count == 2:
if img_name is not None:
if pid is not None:
img_name = img_name.replace("\"", "")
img_name = img_name.replace("\'", "")
import inspect
pk_print(str_working=rf''' 이 {func_n}()의 인자는 최대 1개 까지 받을 수 있습니다.  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
pk_print(str_working=rf''' 이 {func_n}()의 인자는 최소 1개의 인자가 요구됩니다.  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
pk_print(str_working=rf'''{PK_UNDERLINE}{func_n}()  {'%%%FOO%%%' if LTA else ''}''')
