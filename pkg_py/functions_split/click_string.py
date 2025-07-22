from pkg_py.functions_split.pk_sleep import pk_sleep


def click_string(string, doubleclick_mode=False):
    import time
    time_limit = 20
    time_s = time.time()
    while 1:
        # pk_print(str_working=time.time() - time_s)
        if time.time() - time_s > time_limit:
            break
        if does_text_bounding_box_exist_via_easy_ocr(string=string):
            break
        pk_sleep(seconds=0.5)
    click_mouse_left_btn(doubleclick_mode=doubleclick_mode)
