

def is_newyear():
    yyyy = get_time_as_('%Y')
    state_yearly = None
    if is_month(mm=1) and is_day(dd=1):
        return 1
    else:
        return 0
