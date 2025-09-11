from sources.functions.ensure_pressed import ensure_pressed
from sources.functions.ensure_slept import ensure_slept


from sources.functions.ensure_typed import ensure_typed


def ensure_cursor_moved_to_text_location(text_to_move_cursor):
    ensure_pressed("ctrl", "f")
    ensure_slept(100)
    ensure_typed(text_to_move_cursor)
    ensure_slept(100)
    ensure_pressed("enter")


