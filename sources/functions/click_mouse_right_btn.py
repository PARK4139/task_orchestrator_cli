







def click_mouse_right_btn(abs_x=None, abs_y=None):
    import inspect
    import pyautogui
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if abs_x and abs_y:
        pyautogui.click(button='right', clicks=1, interval=0)
    else:
        pyautogui.click(button='right', clicks=1, interval=0, x=abs_x, y=abs_y, )
