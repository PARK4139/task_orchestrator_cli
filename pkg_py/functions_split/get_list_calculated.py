from pkg_py.functions_split.pk_print import pk_print
from pkg_py.system_object.local_test_activate import LTA


def get_list_calculated(origin_list, minus_list=None, plus_list=None, dedup=True):
    minus_list = minus_list or []
    plus_list = plus_list or []
    if LTA:
        pk_print(f'''origin_list[:3]={origin_list[:3]} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''minus_list[:3]={minus_list[:3]} {'%%%FOO%%%' if LTA else ''}''')
        pk_print(f'''plus_list[:3]={plus_list[:3]} {'%%%FOO%%%' if LTA else ''}''')
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
            pk_print(f'''result[:3]={result[:3]} {'%%%FOO%%%' if LTA else ''}''')
        return result
    else:
        minus_set = set(minus_list)
        result = [x for x in origin_list if x not in minus_set]
        result.extend(plus_list)
        if LTA:
            pk_print(f'''result[:3]={result[:3]} {'%%%FOO%%%' if LTA else ''}''')
        return result


