
from pkg_py.functions_split.press import press


def get_txt_dragged():
    import clipboard
    clipboard_current_contents = pk_paste()
    while 1:
        pk_press("ctrl", "c")
        ensure_slept(milliseconds=15)
        text_dragged = pk_paste()
        if clipboard_current_contents != text_dragged:
            break
    clipboard.copy(clipboard_current_contents)
    return text_dragged
