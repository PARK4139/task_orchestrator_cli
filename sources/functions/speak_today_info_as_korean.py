def speak_today_info_as_korean():
    from sources.functions.ensure_spoken import ensure_spoken
    from sources.functions.get_time_as_ import get_time_as_

    yyyy = get_time_as_('%Y')
    MM = get_time_as_('%m')
    dd = get_time_as_('%d')

    ensure_spoken(text=f'{int(yyyy)}년 {int(MM)}월 {int(dd)}일', after_delay=0.95)
