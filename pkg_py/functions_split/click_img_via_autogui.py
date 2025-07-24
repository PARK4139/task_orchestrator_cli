from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def click_img_via_autogui(img, x_cal=0, y_cal=0):
    import pyautogui
    # confidence=0.7(70%)유사도를 낮춰 인식률개선시도, region 낮춰 속도개선시도, grayscale 흑백으로 판단해서 속도개선시도,

    # 이미지중앙좌표 클릭
    img_finding_loop_cnt = 0
    img_finding_loop_cnt_limit = 10
    while 1:
        img_finding_loop_cnt = img_finding_loop_cnt + 1
        try:
            x, y = pyautogui.locateCenterOnScreen(image=img, confidence=0.7, grayscale=True)
        except pyautogui.ImageNotFoundException:
            pk_print(rf"이미지찾기", print_color='red')
            # pk_print(f"{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}", print_color='red')
            break
        if x is not None and y is not None:
            x_cal = x_cal
            y_cal = y_cal
            x = x - x_cal
            y = y - y_cal

            # 마우스위치 기록
            initial_position = pyautogui.position()

            duration = 1
            move_mouse(x_abs=x, y_abs=y, duration=duration)
            pyautogui.click()

            # 마우스위치 원복
            x, y = initial_position
            duration = 0
            move_mouse(x_abs=x, y_abs=y, duration=duration)
            # pk_print(rf"이미지중앙좌표클릭 ({x}, {y})  {'%%%FOO%%%' if LTA else ''}", print_color='green')
            break

        pk_print(f'''이미지중앙좌표클릭  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
        if img_finding_loop_cnt == img_finding_loop_cnt_limit:
            pk_print(f'''이미지중앙좌표클릭  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
            break
