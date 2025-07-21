

# import win32process


def get_weekday_as_english():
    from datetime import datetime
    now = datetime.now()
    weekdays_korean = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    return weekdays_korean[now.weekday()]
