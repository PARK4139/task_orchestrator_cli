from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.cmd_to_os import cmd_to_os

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def collect_img_for_autogui():
    import inspect
    import sys
    import traceback

    func_n = inspect.currentframe().f_code.co_name
    server_time = get_time_as_('%Y_%m_%d_%H_%M_%S')
    func_n_server_time_png = rf'{D_PKG_PNG}\{func_n}_{server_time}.png'
    f = func_n_server_time_png
    f_p = get_p(func_n_server_time_png)
    file_nx = get_nx(func_n_server_time_png)
    ensure_pnx_made(f_p, mode="d")
    try:
        pk_press("win", "shift", "s", interval=0.5)
        key = "ctrl+s"
        if not is_keyboard_pressed_within_time_limit(key_plus_key=key, time_limit=60):
            pk_print(rf"[red] 클릭감지타임아웃 {key}")
        pk_sleep(milliseconds=500)
        pk_sleep(milliseconds=500)
        pk_press("ctrl", "l", interval=0.5)
        pk_sleep(milliseconds=300)
        pk_copy(working_str=f_p)
        pk_sleep(milliseconds=300)
        pk_press("enter")
        pk_sleep(milliseconds=300)
        print_as_gui(ment="클립보드에 추천f명을 저장해두었습니다")
        key = "left"
        if not is_mouse_button_click_within_time_limit(key="left", time_limit=60):
            ment_error = rf"[red] 클릭감지타임아웃 {key}"
            # raise FridayLogicError(ment_error)
            pk_print(ment_error)
        write_fast(file_nx)
        pk_sleep(milliseconds=300)
        # press("enter")
        pk_sleep(milliseconds=300)
        if does_pnx_exist(pnx=f):
            cmd = rf"taskkill -im ScreenSketch.exe"
        text_editor = 'explorer.exe'
        cmd = f'{text_editor} "{f_p}" '
        cmd_to_os(cmd=cmd)
    except:
        traceback.print_exc(file=sys.stdout)
