def get_weekday():
    from datetime import datetime
    from sources.objects.pk_map_texts import PkTexts
    
    now = datetime.now()
    weekday_index = now.weekday()
    
    weekdays = [
        PkTexts.MONDAY,
        PkTexts.TUESDAY, 
        PkTexts.WEDNESDAY,
        PkTexts.THURSDAY,
        PkTexts.FRIDAY,
        PkTexts.SATURDAY,
        PkTexts.SUNDAY
    ]
    
    return weekdays[weekday_index] 