import os
from pathlib import Path

import toml


F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML = Path(__file__).resolve().parent.parent.parent / "project_config.toml"
values = os.path.normpath(F_TASK_ORCHESTRATOR_CLI_CONFIG_TOML).lower()
LTA = toml.load(values)["LOCAL_TEST_ACTIVATE"]
