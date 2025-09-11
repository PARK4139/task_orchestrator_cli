def keyUp(key: str):
    import inspect
    import pyautogui
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()
    pyautogui.keyUp(key)
