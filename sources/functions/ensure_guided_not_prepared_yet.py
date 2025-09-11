def ensure_not_prepared_yet_guided():
    import logging
    from functions.ensure_spoken import ensure_spoken
    from objects.pk_map_texts import PkTexts
    from sources.objects.pk_etc import PK_UNDERLINE

    try:

        logging.debug(PK_UNDERLINE)
        msg = PkTexts.NOT_PREPARED_YET
        ensure_spoken(msg, wait=True)
        logging.debug("이 기능은 현재 개발 중이거나 아직 구현되지 않았습니다.")
        logging.debug("개발자에게 문의하거나 나중에 다시 시도해주세요.")
        logging.debug(PK_UNDERLINE)
    except Exception as e:
        logging.debug(f"Failed to show guidance message: {e}")
