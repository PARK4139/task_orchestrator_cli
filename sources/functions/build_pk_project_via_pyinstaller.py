import uuid
import subprocess
import re
import pandas as pd
import functools

from webdriver_manager.chrome import ChromeDriverManager
from sources.functions.get_f_video_to_load import get_f_video_to_load

from sources.functions.ensure_command_executed import ensure_command_executed
from sources.objects.encodings import Encoding
from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI

from passlib.context import CryptContext
from functools import lru_cache
from collections import Counter
from sources.functions.get_pnxs import get_pnxs
from sources.functions.is_d import is_d
from sources.functions.is_os_windows import is_os_windows
import logging
from sources.functions.does_pnx_exist import is_pnx_existing

from sources.objects.pk_local_test_activate import LTA
import logging
from sources.functions.get_pnxs import get_pnxs


def build_pk_project_via_pyinstaller():
    import os

    # 프로젝트 d로 이동
    os.chdir(D_TASK_ORCHESTRATOR_CLI)

    if is_pnx_existing(pnx=D_VENV):
        logging.debug(f"{D_VENV} d가 있습니다")

        # 현재d의 불필요한 타겟들을 삭제
        items_useless = [
            rf"{D_TASK_ORCHESTRATOR_CLI}\pk.exe",
            rf"{D_TASK_ORCHESTRATOR_CLI}\build",
            rf"{D_TASK_ORCHESTRATOR_CLI}\dist",
            rf"{D_TASK_ORCHESTRATOR_CLI}\_internal",
            rf"{D_TASK_ORCHESTRATOR_CLI}\dist.zip",
            rf"{D_TASK_ORCHESTRATOR_CLI}\pk.spec",
        ]
        for item in items_useless:
            reensure_pnx_moved_parmanently(pnx=item)

        # pip 업그레이드
        ensure_command_executed(cmd="python -m pip install --upgrade pip")

        # pip 업그레이드
        ensure_command_executed(cmd="pip install pyinstaller --upgrade")

        if not LTA:
            ensure_command_executed(cmd=rf"python -m PyInstaller -i .\resources\icon.PNG pk_test_test.py")

        if LTA:
            ensure_command_executed(cmd=rf'echo d | xcopy ".\resources" ".\dist\pk_test_test\_internal\resources" /e /h /k /y')

        # f = f'{D_TASK_ORCHESTRATOR_CLI}/pk_temp.py'
        # write_f(f)

        # virtual environment 을 활성화하고, 그 후에 파이썬 스크립트 exec
        # run

        # pk_temp.py
        # os.remove(f)

    else:
        logging.debug(f"{D_VENV} d가 없습니다")
