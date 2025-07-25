
'.webp', '.jfif']])
['.jpg', '.jpeg', '.png',
continue  # _d_는 무시
d_new = os.path.join(d_working, keyword.lower())
d_new = os.path.join(d_working, x_extracted.replace(".", ""))
d_working = get_value_completed(key_hint='d_working=',
def pk_ensure_f_list_organized_by_keyword_and_x():
except KeyboardInterrupt:
f_new = get_pnx_new(d_working=d_new, pnx=pnx)
f_nx = pnx_nx
for keyword in keyword_to_organize_list:
for pnx_nx in pnx_nx_list:
from pkg_py.functions_split.get_value_completed import get_value_completed
from pkg_py.functions_split.print import pk_print
from pkg_py.system_object.directories import D_PK_WORKING, D_DOWNLOADS
from pkg_py.system_object.directories_reuseable import D_PROJECT
if ensure_d_size_stable(d_working, limit_seconds=5):
if keyword in f_nx:
if not os.path.exists(f_new):
if not os.path.isfile(pnx):
if x_extracted in x_to_organize_list:
import os
keyword_to_organize_list = get_values_completed(key_hint='keyword_to_organize_list=',
move_pnx(pnx=pnx, d_dst=d_new)
os.makedirs(d_new, exist_ok=True)
pk_print("\n 모니터링 중지됨.")
pk_print(f"f 이동 {f_nx} → {f_new}", print_color='green')
pnx = os.path.join(d_working, pnx_nx)
pnx_nx_list = os.listdir(d_working)  # _d_ 목록 가져오기
try:
values=[['seg', 'SEG']])
values=[os.getcwd(), D_PK_WORKING, D_PROJECT, D_DOWNLOADS])
while 1:
x_extracted = get_x(pnx).lower()  # 확장자 캐싱
x_to_organize_list = get_values_completed(key_hint='x_to_organize_list=', values=[['mp4', 'mkv', 'avi'],
