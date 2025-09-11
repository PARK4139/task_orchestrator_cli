from sources.functions.get_f_historical import ensure_history_file_pnx_return
from sources.functions.get_list_by_file_id import get_list_by_file_id
from functions.get_list_removed_element_empty import get_list_removed_empty
from sources.functions.get_list_removed_none import get_list_removed_none
from sources.functions.get_list_striped import get_list_striped
from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext


def get_value_by_file_id(file_id):
    import logging
    import logging

    from sources.objects.pk_local_test_activate import LTA
    from sources.objects.pk_map_texts import PkTexts
    from sources.functions.get_nx import get_nx
    from sources.functions.ensure_value_completed import ensure_value_completed
    from sources.functions.ensure_window_to_front import ensure_window_to_front
    text_to_move_cursors = get_list_by_file_id(file_id)
    logging.debug(f'''text_to_move_cursors={text_to_move_cursors} {'%%%FOO%%%' if LTA else ''}''')
    text_to_move_cursors = get_list_striped(text_to_move_cursors)
    logging.debug(f'''text_to_move_cursors={text_to_move_cursors} {'%%%FOO%%%' if LTA else ''}''')
    text_to_move_cursors = get_list_removed_none(text_to_move_cursors)
    logging.debug(f'''text_to_move_cursors={text_to_move_cursors} {'%%%FOO%%%' if LTA else ''}''')
    text_to_move_cursors = get_list_removed_empty(text_to_move_cursors)
    logging.debug(f'''text_to_move_cursors={text_to_move_cursors} {'%%%FOO%%%' if LTA else ''}''')
    while 1:
        logging.debug(f'''len(text_to_move_cursors)={len(text_to_move_cursors)} {'%%%FOO%%%' if LTA else ''}''')
        if len(text_to_move_cursors) == 1:
            text_to_move_cursor = text_to_move_cursors[0]
            if text_to_move_cursor is not None and text_to_move_cursor.strip() != "" and len(text_to_move_cursors) == 1:
                return text_to_move_cursor
        else:
            logging.debug(f'''text_to_move_cursors is None={text_to_move_cursors is None} {'%%%FOO%%%' if LTA else ''}''')
            f_historical = ensure_history_file_pnx_return(file_id)
            ensure_pnx_opened_by_ext(pnx=f_historical)
            ensure_window_to_front(get_nx(f_historical))
            decision = ensure_value_completed(key_hint=PkTexts.ARE_YOU_SURE_EDIT_DONE,
                                              options=[PkTexts.YES, PkTexts.NO])
            if decision == PkTexts.YES:
                text_to_move_cursors = get_list_by_file_id(file_id)
                continue
