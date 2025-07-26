from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os

from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_pressed import ensure_pressed
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
        ensure_pressed("win", "shift", "s", interval=0.5)
        key = "ctrl+s"
        if not is_keyboard_pressed_within_time_limit(key_plus_key=key, time_limit=60):
            ensure_printed(rf"[red] 클릭감지타임아웃 {key}")
        ensure_slept(milliseconds=500)
        ensure_slept(milliseconds=500)
        ensure_pressed("ctrl", "l", interval=0.5)
        ensure_slept(milliseconds=300)
        ensure_copied(str_working=f_p)
        ensure_slept(milliseconds=300)
        ensure_pressed("enter")
        ensure_slept(milliseconds=300)
        print_as_gui(ment="클립보드에 추천f명을 저장해두었습니다")
        key = "left"
        if not is_mouse_button_click_within_time_limit(key="left", time_limit=60):
            ment_error = rf"[red] 클릭감지타임아웃 {key}"
            # raise FridayLogicError(ment_error)
            ensure_printed(ment_error)
        ensure_writen_fast(file_nx)
        ensure_slept(milliseconds=300)
        # press("enter")
        ensure_slept(milliseconds=300)
        if does_pnx_exist(pnx=f):
            cmd = rf"taskkill -im ScreenSketch.exe"
        text_editor = 'explorer.exe'
        cmd = f'{text_editor} "{f_p}" '
        ensure_command_excuted_to_os(cmd=cmd)
    except:
        traceback.print_exc(file=sys.stdout)
