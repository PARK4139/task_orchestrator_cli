




def pk_initialize_and_customize_logging_config(__file__):
    """description  : Replaced print() with logging.info() in pk_system """
    """call example : 
        pk_initialize_and_customize_logging_config(__file__)

        logging.warning(msg)
        logging.error(msg)
        logging.critical(msg)
        logging.debug(msg)
        logging.info(msg)
    """
    import logging
    from pkg_py.pk_system_layer_files import F_TEMP_TXT
    logging.basicConfig(
        level=logging.DEBUG,  # setting to record from level DEBUG to level info
        format="[%(asctime)s] [%(levelname)s] [%(message)s]",
        encoding="utf-8",
        handlers=[
            logging.FileHandler(f"{F_TEMP_TXT}", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )


