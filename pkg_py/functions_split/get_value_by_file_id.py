from pkg_py.functions_split.get_f_historical import get_history_file
from pkg_py.functions_split.get_list_by_file_id import get_list_by_file_id
from pkg_py.functions_split.get_list_removed_element_empty import get_list_removed_empty
from pkg_py.functions_split.get_list_removed_none import get_list_removed_none
from pkg_py.functions_split.get_list_striped import get_list_striped
from pkg_py.functions_split.open_pnx_by_ext import ensure_pnx_opened_by_ext


def get_value_by_file_id(file_id):
    import logging

    from pkg_py.system_object.local_test_activate import LTA
    from pkg_py.system_object.map_massages import PkMessages2025
    from pkg_py.functions_split.get_nx import get_nx
    from pkg_py.functions_split.get_value_completed import get_value_completed
    from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
    text_to_move_cursors = get_list_by_file_id(file_id)
    logging.info(f'''text_to_move_cursors={text_to_move_cursors} {'%%%FOO%%%' if LTA else ''}''')
    text_to_move_cursors = get_list_striped(text_to_move_cursors)
    logging.info(f'''text_to_move_cursors={text_to_move_cursors} {'%%%FOO%%%' if LTA else ''}''')
    text_to_move_cursors = get_list_removed_none(text_to_move_cursors)
    logging.info(f'''text_to_move_cursors={text_to_move_cursors} {'%%%FOO%%%' if LTA else ''}''')
    text_to_move_cursors = get_list_removed_empty(text_to_move_cursors)
    logging.info(f'''text_to_move_cursors={text_to_move_cursors} {'%%%FOO%%%' if LTA else ''}''')
    while 1:
        logging.info(f'''len(text_to_move_cursors)={len(text_to_move_cursors)} {'%%%FOO%%%' if LTA else ''}''')
        if len(text_to_move_cursors) == 1:
            text_to_move_cursor = text_to_move_cursors[0]
            if text_to_move_cursor is not None and text_to_move_cursor.strip() != "" and len(text_to_move_cursors) == 1:
                return text_to_move_cursor
        else:
            logging.info(f'''text_to_move_cursors is None={text_to_move_cursors is None} {'%%%FOO%%%' if LTA else ''}''')
            f_historical = get_history_file(file_id)
            ensure_pnx_opened_by_ext(pnx=f_historical)
            ensure_window_to_front(window_title_seg=get_nx(f_historical))
            decision = get_value_completed(key_hint=PkMessages2025.ARE_YOU_SURE_EDIT_DONE,
                                           values=[PkMessages2025.YES, PkMessages2025.NO])
            if decision == PkMessages2025.YES:
                text_to_move_cursors = get_list_by_file_id(file_id)
                continue
