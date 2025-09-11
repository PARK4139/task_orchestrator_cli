from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_sensitive_info_masked(info: str, visible_chars: int = 4) -> str:
    if not info:
        return ""
    if len(info) <= visible_chars * 2:
        return "*" * len(info)
    return (
            info[:visible_chars]
            + "*" * (len(info) - visible_chars * 2)
            + info[len(info) - visible_chars:]
    )

# def ensure_sensitive_info_masked(info: str):
#     masked_info =   info[:3] +  "*" * int(len(info)-3) + "*" * get_random_int(4)
#     return masked_info
