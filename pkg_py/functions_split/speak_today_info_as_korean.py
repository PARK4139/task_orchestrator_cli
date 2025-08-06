

def speak_today_info_as_korean():
    import inspect
    from pkg_py.functions_split import ensure_spoken, get_time_as_

    yyyy = get_time_as_('%Y')
    MM = get_time_as_('%m')
    dd = get_time_as_('%d')

    ensure_spoken(str_working=f'{int(yyyy)}년 {int(MM)}월 {int(dd)}일', after_delay=0.95)
