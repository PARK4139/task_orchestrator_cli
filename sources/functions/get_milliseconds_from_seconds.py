def get_milliseconds_from_seconds(seconds: float) -> float:
    import logging
    milliseconds = seconds * 1000
    logging.debug(f"get_milliseconds_from_seconds: {seconds} seconds converted to {milliseconds} milliseconds.")
    return milliseconds
