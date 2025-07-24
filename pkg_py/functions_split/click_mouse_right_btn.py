




# from project_database.test_project_database import MySqlUtil


def click_mouse_right_btn(abs_x=None, abs_y=None):
    import inspect
    import pyautogui
    func_n = inspect.currentframe().f_code.co_name
    if abs_x and abs_y:
        pyautogui.click(button='right', clicks=1, interval=0)
    else:
        pyautogui.click(button='right', clicks=1, interval=0, x=abs_x, y=abs_y, )
