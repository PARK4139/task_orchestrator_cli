








def is_christmas():
    yyyy = get_time_as_('%Y')
    if is_month(mm=12) and is_day(dd=25):
        return 1
    else:
        return 0
