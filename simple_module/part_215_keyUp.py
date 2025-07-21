def keyUp(key: str):
    import inspect
    import pyautogui
    func_n = inspect.currentframe().f_code.co_name
    pyautogui.keyUp(key)
