from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_190_pk_press import pk_press


def get_txt_dragged():
    import clipboard
    clipboard_current_contents = pk_paste()
    while 1:
        pk_press("ctrl", "c")
        pk_sleep(milliseconds=15)
        text_dragged = pk_paste()
        if clipboard_current_contents != text_dragged:
            break
    clipboard.copy(clipboard_current_contents)
    return text_dragged
