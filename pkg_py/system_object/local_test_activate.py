import os
from pathlib import Path
from typing import TypeVar

import toml

from pkg_py.system_object.directories import D_PKG_TOML

T = TypeVar('T')

F_PK_CONFIG_TOML = rf'{D_PKG_TOML}/pk_config.toml'
normalized_path = os.path.normpath(F_PK_CONFIG_TOML).lower()
LTA = toml.load(F_PK_CONFIG_TOML)["LOCAL_TEST_ACTIVATE"]
