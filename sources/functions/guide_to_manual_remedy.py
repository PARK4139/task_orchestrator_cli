from tkinter import UNDERLINE


import logging
from tkinter import UNDERLINE


import logging


def guide_to_manual_remedy(prompt_remedy):
    print(f'\n')
    ensure_text_saved_to_clipboard(str_working=prompt_remedy)
    logging.debug(f'{PK_UNDERLINE}')
    logging.debug(f'{'[ TRY GUIDE ]'} {prompt_remedy}')
    logging.debug(f'{PK_UNDERLINE}')
