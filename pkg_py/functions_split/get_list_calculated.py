from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.local_test_activate import LTA


def get_list_calculated(origin_list, minus_list=None, plus_list=None, dedup=True):
    origin_list = origin_list or []
    minus_list = minus_list or []
    plus_list = plus_list or []
    print_limit = min(len(origin_list), len(minus_list), len(plus_list))
    if LTA:
        ensure_printed(f'''origin_list[:{len(origin_list)}]={origin_list[:print_limit]} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''minus_list[:{len(minus_list)}]={minus_list[:print_limit]} {'%%%FOO%%%' if LTA else ''}''')
        ensure_printed(f'''plus_list[:{len(plus_list)}]={plus_list[:print_limit]} {'%%%FOO%%%' if LTA else ''}''')
    if dedup:
        seen = set()
        result = []
        for x in origin_list:
            if x not in minus_list and x not in seen:
                seen.add(x)
                result.append(x)
        for x in plus_list:
            if x not in seen:
                seen.add(x)
                result.append(x)
        if LTA:
            ensure_printed(f'''result[:{len(result)}]={result[:print_limit]} {'%%%FOO%%%' if LTA else ''}''')
        return result
    else:
        minus_set = set(minus_list)
        result = [x for x in origin_list if x not in minus_set]
        result.extend(plus_list)
        if LTA:
            ensure_printed(f'''result[:{len(result)}]={result[:print_limit]} {'%%%FOO%%%' if LTA else ''}''')
        return result
