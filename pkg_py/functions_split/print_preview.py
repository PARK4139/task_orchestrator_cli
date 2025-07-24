from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def print_preview(categorized_f_dict):
    from colorama import init as pk_colorama_init
    pk_colorama_init_once()

    pk_print(f'''[ ngram 기반 분류결과(preview) ] {'%%%FOO%%%' if LTA else ''}''', print_color='blue')
    # f_print_mode = get_value_completed(message='f_print_mode=', option_values=["o","x"])
    for group, files in categorized_f_dict.items():
        # print(f"\n\U0001F4C2 {group} = []")
        # if f_print_mode=="o":
        #     for f in files:
        #         print(f"  └─ {f}")
        # else:
        #     pass
        f_filtered = []
        for f in files:
            if len(f_filtered) < 10:
                f_filtered.append(f)
            elif len(f_filtered) == 10:
                f_filtered.append("...")
            else:
                pass
        print(f"\n\U0001F4C2 {group} = {f_filtered}")
