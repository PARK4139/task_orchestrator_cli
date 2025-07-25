
# 프로그램초기 1회 만 동작
# 프로그램초기실행완료여부 pickle 에 저장  -> 프로그램초기실행완료여부==False 면 출력
def pk_print_once(msg):
f_pkl = os.path.join(D_PKG_PKL, f'{file_id}.pkl')
file_id = "state_about_pk_print_once"
from pkg_py.functions_split.load_logged_set import load_logged_set
from pkg_py.functions_split.print import pk_print
from pkg_py.functions_split.save_logged_set import save_logged_set
from pkg_py.system_object.directories import D_PKG_PKL
if msg in logged_set:
import os.path
logged_set = load_logged_set(f_pkl)
logged_set.add(msg)
pk_print(msg)
return
save_logged_set(logged_set, f_pkl)
