

from pkg_py.pk_system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def does_normal_tab_exist(driver_selenium, tab_title_negative):
    import inspect
    import random

    func_n = inspect.currentframe().f_code.co_name
    for window in driver_selenium.window_handles:  # 모든 탭 이동
        driver_selenium.switch_to.window(window)  # 각 탭으로 전환
        pk_sleep(milliseconds=random.randint(22, 2222))
        if tab_title_negative not in driver_selenium.title:  # 탭 제목 확인
            return 1
    pk_print(f'''abnormal tab title({tab_title_negative}) detedcted  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    return 0
