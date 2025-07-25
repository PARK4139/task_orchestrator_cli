
cmd_to_os(f'wmic process where name="{process_img_n}" delete ')
def kill_process_via_wmic(process_img_n=None, debug_mode=True):
else:
func_n = inspect.currentframe().f_code.co_name
if process_img_n is not None:
import inspect
pk_print(rf"{func_n}() 동작 조건 불충족")
pk_print(rf"{func_n}() 동작 조건 충족")
process_img_n = process_img_n.replace("\"", "")
process_img_n = process_img_n.replace("\'", "")
return
