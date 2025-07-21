

# from project_database.test_project_database import MySqlUtil

from pkg_py.simple_module.part_014_pk_print import pk_print


def write_like_person(str_working: str, interval=0.04):  # interval 낮을 수록 빠름 # cmd.exe 를 admin 으로 열면 클립보드가 막혀있음.
    import inspect

    import pyautogui
    func_n = inspect.currentframe().f_code.co_name

    pyautogui.write(str_working, interval=interval)  # 한글 미지원.
    pk_print(rf"{str_working}", print_color='blue')
