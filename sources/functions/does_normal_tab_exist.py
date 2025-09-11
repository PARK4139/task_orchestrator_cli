




def does_normal_tab_exist(driver_selenium, tab_title_negative):
    import random

    for window in driver_selenium.window_handles:  # 모든 탭 이동
        driver_selenium.switch_to.window(window)  # 각 탭으로 전환
        ensure_slept(milliseconds=random.randint(22, 2222))
        if tab_title_negative not in driver_selenium.title:  # 탭 제목 확인
            return 1
    return 0
