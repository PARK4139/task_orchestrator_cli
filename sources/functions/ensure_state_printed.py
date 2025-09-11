import logging


def ensure_state_printed(state, pk_id, state_header=None):
    from sources.objects.pk_local_test_activate import LTA
    if state_header is not None:
        logging.debug(f'''{state_header} {f'{pk_id}' if LTA else ''}''')
    logging.debug(f'''{state} {f'{pk_id}' if LTA else ''}''')
