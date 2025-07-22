import socket
from pkg_py.functions_split.pk_press import pk_press

from pkg_py.pk_system_object.files import F_POT_PLAYER_MINI_64_EXE
from datetime import date
from collections import Counter
from bs4 import BeautifulSoup


def get_list_leaved_element_pattern(items, pattern):
    import re
    if isinstance(pattern, str):
        pattern = re.compile(pattern)
    matches = []
    for line in items:
        if isinstance(line, bytes):
            try:
                line = line.decode('utf-8')  # 기본 UTF-8 시도
            except UnicodeDecodeError:
                line = line.decode('cp949')  # UTF-8 실패 시 CP949로 디코딩
        found = pattern.findall(line)
        if found:
            matches.extend(found)
    return matches
