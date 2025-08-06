

def get_str_today_day_info():
    yyyy = get_time_as_('%Y')
    MM = get_time_as_('%m')
    dd = get_time_as_('%d')
    HH = get_time_as_('%H')
    mm = get_time_as_('%M')
    # week_name=get_weekday_as_korean()
    # return f'대한민국 표준시 기준, 현재시각 {int(yyyy)}년 {int(MM)}월 {int(dd)}일 {week_name}요일 {int(HH)}시 {int(mm)}분'
    from pkg_py.functions_split.get_weekday import get_weekday
    week_name = get_weekday()
    # return f'Based on Korea Standard Time, the current time is {int(yyyy)} year {int(MM)} month {int(dd)} day, {week_name}, {int(HH)} hour {int(mm)} minute'
    # return f'the current time is {int(yyyy)} year {int(MM)} month {int(dd)} day, {week_name}, {int(HH)} hour {int(mm)} minute'
    return f'{int(yyyy)} {int(MM)} {int(dd)} {week_name} {int(HH)} {int(mm)}'
