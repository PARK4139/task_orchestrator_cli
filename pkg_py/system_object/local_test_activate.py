import os
from typing import TypeVar

import toml

# Lazy import to avoid circular dependency
def get_d_pkg_toml():
    try:
        from pkg_py.system_object.directories import D_PKG_TOML
        return D_PKG_TOML
    except ImportError:
        # Fallback path if import fails
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        return os.path.join(project_root, 'pkg_toml')

T = TypeVar('T')

D_PKG_TOML = get_d_pkg_toml()
F_PK_CONFIG_TOML = rf'{D_PKG_TOML}/pk_config.toml'
normalized_path = os.path.normpath(F_PK_CONFIG_TOML).lower()
LTA = toml.load(F_PK_CONFIG_TOML)["LOCAL_TEST_ACTIVATE"]
