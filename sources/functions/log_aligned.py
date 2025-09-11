# @ensure_seconds_measured
def log_aligned(*, key: str, value: str, gap: int, width: int = 100, seperator: str = '|'):
    """
    # expected return format
    key      | value

    # tip
    gap = len("mode_with_window")  # 가장 긴 key 길이

    """
    import logging
    logging.debug(f"{key:<{gap}}  {seperator} {value:<{width}}")
