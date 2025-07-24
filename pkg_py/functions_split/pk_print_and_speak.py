from pkg_py.functions_split.pk_print import pk_print


def pk_print_and_speak(str_working, print_color='blue', after_delay=1.00):
    pk_print(str_working=str_working, print_color=print_color)
    try:
        pk_speak(str_working=str_working, after_delay=after_delay)
    except:
        raise
