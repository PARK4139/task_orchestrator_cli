





def ensure_writen_like_human(str_working: str, interval=0.04):  # interval 낮을 수록 빠름 # cmd.exe 를 admin 으로 열면 클립보드가 막혀있음.
    import logging
    import inspect

    import pyautogui
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    pyautogui.write(str_working, interval=interval)  # 한글 미지원.
    logging.debug(rf"{str_working}")
