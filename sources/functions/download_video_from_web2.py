from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI

from sources.functions.ensure_pressed import ensure_pressed


def download_video_from_web2():
    if not is_internet_connected():
        raise
    while 1:
        f_png = rf"{D_TASK_ORCHESTRATOR_CLI}\resources\download_video_via_chrome_extensions1.png"
        is_image_finded = click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=100)
        if is_image_finded:
            ensure_slept(30)
            ensure_pressed("ctrl", "f")
            ensure_pressed("end")
            ensure_pressed("ctrl", "a")
            ensure_pressed("backspace")
            ensure_writen_fast("save")
            ensure_pressed("enter")
            ensure_pressed("enter")
            ensure_pressed("esc")
            ensure_pressed("enter")
            f_png = rf"{D_TASK_ORCHESTRATOR_CLI}\resources\download_video_via_chrome_extensions2.png"
            is_image_finded = click_center_of_img_recognized_by_mouse_left(img_pnx=f_png, loop_limit_cnt=100)
            if is_image_finded:
                ensure_pressed("shift", "w")
            else:
                ensure_spoken_v2(str_working="이미지를 찾을 수 없어 해당 자동화 기능을 마저 진행할 수 없습니다", comma_delay=0.98)
        else:
            ensure_spoken_v2(str_working="이미지를 찾을 수 없어 해당 자동화 기능을 마저 진행할 수 없습니다", comma_delay=0.98)
        break
    pass
