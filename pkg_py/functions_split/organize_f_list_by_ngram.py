
)
ans = ans.lower()
ans = ans.strip()
ans = pk_input_v44_uv_theme(
categorized_f_dict = get_categorized_f_dict_by_priority_ngrams(f_to_organize_list, min_support=min_support,
def pk_organize_f_list_by_ngram(f_to_organize_list, d_working, token_splitter_pattern, min_support, max_n):
else:
fuzzy_accept=[("o", "ok", "yes", "y"), ("x", "no", "n")],
if ans == 'o':
limit_seconds=60,
masked=False,
max_n=max_n,
move_f_list_by_category(categorized_f_dict, base_p=d_working)
print("\n✅ 분류 완료!")
print("\n❌ 분류를 취소했습니다.")
print_preview(categorized_f_dict)
return_default="x",
str_working="위와 같이 파일을 분류할까요? (o/x):",
token_splitter_pattern=token_splitter_pattern)
validator=lambda s: s.lower() in {"o", "x", "yes", "no", "y", "n"},
