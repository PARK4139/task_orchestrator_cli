import requests
import platform
import nest_asyncio
import mutagen
from urllib.parse import urlparse
from selenium.webdriver.common.action_chains import ActionChains
from PySide6.QtWidgets import QApplication
from pkg_py.functions_split.pk_print_once import pk_print_once
from pkg_py.functions_split.get_list_sorted import get_list_sorted
from pkg_py.system_object.etc import PkFilter
from functools import partial
from dataclasses import dataclass
from base64 import b64decode
from pkg_py.system_object.directories import D_PKG_PY
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def rsync_d_remote(d_pnx):
    """이게 뭐냐면 외부망에 있는 d를 동기화. 리눅스 rsync 에 의존하는 기술"""

    # todo : chore :

    if not is_internet_connected():
        raise
    pk_speak(PkMents2025Korean.NOT_PREPARED_YET)
    pass
