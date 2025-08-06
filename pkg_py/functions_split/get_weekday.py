def get_weekday():
    from datetime import datetime
    from pkg_py.system_object.map_massages import PkMessages2025
    
    now = datetime.now()
    weekday_index = now.weekday()
    
    weekdays = [
        PkMessages2025.MONDAY,
        PkMessages2025.TUESDAY, 
        PkMessages2025.WEDNESDAY,
        PkMessages2025.THURSDAY,
        PkMessages2025.FRIDAY,
        PkMessages2025.SATURDAY,
        PkMessages2025.SUNDAY
    ]
    
    return weekdays[weekday_index] 