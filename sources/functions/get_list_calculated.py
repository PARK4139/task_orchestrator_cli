def get_list_calculated(origin_list, minus_list=None, plus_list=None, dedup=True):
    import logging
    from sources.objects.pk_local_test_activate import LTA
    origin_list = origin_list or []
    minus_list = minus_list or []
    plus_list = plus_list or []
    print_limit = min(len(origin_list), len(minus_list), len(plus_list))
    if LTA:
        logging.debug(f'''print_limit={print_limit} {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(f'''len(origin_list)={len(origin_list)} {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(f'''len(minus_list)={len(minus_list)} {'%%%FOO%%%' if LTA else ''}''')
        logging.debug(f'''len(plus_list)={len(plus_list)} {'%%%FOO%%%' if LTA else ''}''')

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
            logging.debug(f'''len(result)={len(result)} {'%%%FOO%%%' if LTA else ''}''')
        return result
    else:
        minus_set = set(minus_list)
        result = [x for x in origin_list if x not in minus_set]
        result.extend(plus_list)
        if LTA:
            logging.debug(f'''len(result)={len(result)} {'%%%FOO%%%' if LTA else ''}''')
        return result
