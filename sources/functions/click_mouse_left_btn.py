def click_mouse_left_btn(x_abs=None, y_abs=None, doubleclick_mode=False):
    import inspect
    import pyautogui
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    if doubleclick_mode == True:
        clicks = 2
    else:
        clicks = 1
    if x_abs and y_abs:
        pyautogui.click(button='left', clicks=clicks, interval=0, x=x_abs, y=y_abs)
    else:
        pyautogui.click(button='left', clicks=clicks, interval=0)
