
from pkg_py.functions_split.ensure_pressed import ensure_pressed


def get_txt_dragged():
    import clipboard
    clipboard_current_contents = ensure_pasted()
    while 1:
        ensure_pressed("ctrl", "c")
        ensure_slept(milliseconds=15)
        text_dragged = ensure_pasted()
        if clipboard_current_contents != text_dragged:
            break
    clipboard.copy(clipboard_current_contents)
    return text_dragged
