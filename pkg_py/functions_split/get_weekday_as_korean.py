

def get_weekday_as_korean():
    from datetime import datetime
    now = datetime.now()
    weekdays_korean = ['월', '화', '수', '목', '금', '토', '일']
    return weekdays_korean[now.weekday()]
