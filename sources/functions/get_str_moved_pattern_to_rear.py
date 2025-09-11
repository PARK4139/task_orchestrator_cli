import secrets

from selenium.webdriver.chrome.options import Options
from sources.functions.get_list_sorted import get_list_sorted

from enum import Enum
from concurrent.futures import ThreadPoolExecutor
from sources.functions.ensure_value_completed import ensure_value_completed

from sources.functions.get_d_working import get_d_working


def get_str_moved_pattern_to_rear(pattern, item_pnx):
    import re
    match = re.search(pattern=pattern, string=item_pnx)
    n = get_n(item_pnx)
    p = get_p(item_pnx)
    x = get_x(item_pnx)
    if match:
        pattern = match.group(1)
        item_pnx_new = rf"{p}\{n.replace(pattern, '')}_{pattern}{x}"
        return item_pnx_new
    else:
        # 패턴이 없으면 원래 f명 반환
        return item_pnx
