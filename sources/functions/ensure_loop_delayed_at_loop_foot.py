def ensure_loop_delayed_at_loop_foot(loop_cnt, mode_level, miliseconds_limit=10000):
    from sources.functions.ensure_slept import ensure_slept

    from sources.objects.pk_map_texts import PkTexts

    from sources.objects.pk_local_test_activate import LTA
    if mode_level == 1:  # strict level
        if LTA:
            input(PkTexts.IF_YOU_WANT_MORE_PRESS_ENTER)
    if mode_level == 2:
        print(rf"[{PkTexts.WAITING}] {miliseconds_limit}{PkTexts.MILLISECONDS}")
        ensure_slept(milliseconds=miliseconds_limit)
    if mode_level == 3:  # natural operation
        if loop_cnt == 1:
            input(PkTexts.IF_YOU_WANT_MORE_PRESS_ENTER)
