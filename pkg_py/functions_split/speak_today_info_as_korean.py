def speak_today_info_as_korean():
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    yyyy = get_time_as_('%Y')
    MM = get_time_as_('%m')
    dd = get_time_as_('%d')

    pk_speak(str_working=f'{int(yyyy)}년 {int(MM)}월 {int(dd)}일', after_delay=0.95)
