from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_mouse_moved(x_abs: float, y_abs: float, duration=1):
    import pyautogui
    pyautogui.moveTo(x_abs, y_abs, duration)
