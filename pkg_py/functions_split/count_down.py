
def count_down(countdown_limit_upper):  #
    for i in range(0, countdown_limit_upper, -1):
        ensure_printed_and_speak(f'count down {i}')