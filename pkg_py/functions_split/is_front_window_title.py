def is_front_window_title(window_title_seg):
    if not get_front_window_title() is None:
        if window_title_seg in get_front_window_title():
            return 1
    return 0
