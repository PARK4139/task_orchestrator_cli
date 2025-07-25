
allowed_extension_tuple = get_tuple_from_set(get_extension_set_from_d(d_working))
def pk_ensure_f_list_organized_by_ngram(token_splitter_pattern, d_working):
f_to_organize_list = [f for f in os.listdir(d_working) if f.endswith(allowed_extension_tuple)]
from pkg_py.functions_split.get_value_completed import get_value_completed
get_value_completed(key_hint='max_n=', values=["2", "3", "4", "5", "6", "7", "8", "9", "10"]))  # 3 or 10  추천
if not f_to_organize_list:
import os
max_n = int(
min_support = int(get_value_completed(key_hint='min_support=', values=["2", "3", "4", "5"]))  # 3 추천
pk_organize_f_list_by_ngram(f_to_organize_list, d_working, token_splitter_pattern, min_support, max_n)
print("📁 대상 파일이 없습니다.")
return
