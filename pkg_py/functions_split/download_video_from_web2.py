from pkg_py.system_object.directories_reuseable import D_PROJECT

from pkg_py.functions_split.pk_press import pk_press


def download_video_from_web2():
    if not is_internet_connected():
        raise
    while 1:
        f_png = rf"{D_PROJECT}\pkg_png\download_video_via_chrome_extensions1.png"
        is_image_finded = click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=100)
        if is_image_finded:
            pk_sleep(30)
            pk_press("ctrl", "f")
            pk_press("end")
            pk_press("ctrl", "a")
            pk_press("backspace")
            write_fast("save")
            pk_press("enter")
            pk_press("enter")
            pk_press("esc")
            pk_press("enter")
            f_png = rf"{D_PROJECT}\pkg_png\download_video_via_chrome_extensions2.png"
            is_image_finded = click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=100)
            if is_image_finded:
                pk_press("shift", "w")
            else:
                pk_speak_v2(str_working="이미지를 찾을 수 없어 해당 자동화 기능을 마저 진행할 수 없습니다", comma_delay=0.98)
        else:
            pk_speak_v2(str_working="이미지를 찾을 수 없어 해당 자동화 기능을 마저 진행할 수 없습니다", comma_delay=0.98)
        break
    pass
