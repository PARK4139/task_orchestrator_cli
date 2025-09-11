import logging


def get_no_blank_str_working_validated(str_working):
    name = str_working.strip()
    if not name:
        logging.debug("blank, name not allowed. Please try again.")
        raise ValueError("Input is blank")
    return name
