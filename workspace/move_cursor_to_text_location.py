def move_cursor_to_text_location(text_to_move_cursor):
    pk_press("ctrl", "f")
    pk_type(text_to_move_cursor)
    pk_sleep(100)
    pk_press("enter")


