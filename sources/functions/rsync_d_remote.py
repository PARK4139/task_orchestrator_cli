import requests
import platform
import nest_asyncio
import mutagen
from urllib.parse import urlparse
from selenium.webdriver.common.action_chains import ActionChains
from PySide6.QtWidgets import QApplication
from sources.functions.ensure_printed_once import ensure_printed_once
from sources.functions.get_list_sorted import get_list_sorted
from sources.objects.pk_etc import PkFilter
from functools import partial
from dataclasses import dataclass
from base64 import b64decode
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_RESOURCES
import logging
from sources.functions.does_pnx_exist import is_pnx_existing


def rsync_d_remote(d_pnx):
    """이게 뭐냐면 외부망에 있는 d를 동기화. 리눅스 rsync 에 의존하는 기술"""

    # todo : chore :

    if not is_internet_connected():
        raise
    ensure_spoken(PkMents2025Korean.NOT_PREPARED_YET)
    pass
