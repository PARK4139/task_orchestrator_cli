
def pk_replace_f_nx_list_from_old_str_to_new_str(d_working, old_str, new_str):
else:
f_new = os.path.join(d_working, f_nx_new)
f_nx_new = f_nx.replace(old_str, new_str)
f_nx_new = f_nx_new.strip()
for f_nx in os.listdir(d_working):
from pkg_py.functions_split.print import pk_print
if f_nx_new:
if os.path.isfile(pnx_old) and old_str in f_nx:
import os
os.rename(pnx_old, f_new)
pk_print(f"Renamed: {f_nx} -> {f_nx_new}", print_color='green')
pk_print(f"Renamed: {f_nx} -> {f_nx_new}", print_color='red')
pnx_old = os.path.join(d_working, f_nx)
