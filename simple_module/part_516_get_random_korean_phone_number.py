import toml
import time
import pandas as pd
import os
import ipdb
import asyncio
from selenium.webdriver.support import expected_conditions as EC
from pkg_py.simple_module.part_009_cmd_to_os import cmd_to_os
from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from gtts import gTTS
from enum import Enum
from dirsync import sync
from datetime import datetime
from collections import Counter
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_012_get_pnx_wsl_unix_style import get_pnx_wsl_unix_style
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist

from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def get_random_korean_phone_number():
    import secrets
    return secrets.choice([
        "010-1234-5678", "02-9876-5432", "031-111-2222", "051-555-7777", "070-1234-5678",
        # "+1-123-456-7890", "+44-20-1234-5678", "+81-3-1234-5678", "+86-10-1234-5678", "+61-2-1234-5678"
    ])
