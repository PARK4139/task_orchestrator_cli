import toml
import time
import pandas as pd
import os
import ipdb
import asyncio
from selenium.webdriver.support import expected_conditions as EC
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.system_object.local_test_activate import LTA
from gtts import gTTS
from enum import Enum
from dirsync import sync
from datetime import datetime
from collections import Counter
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist

from pkg_py.functions_split.get_pnx_list import get_pnx_list


def get_random_korean_phone_number():
    import secrets
    return secrets.choice([
        "010-1234-5678", "02-9876-5432", "031-111-2222", "051-555-7777", "070-1234-5678",
        # "+1-123-456-7890", "+44-20-1234-5678", "+81-3-1234-5678", "+86-10-1234-5678", "+61-2-1234-5678"
    ])
