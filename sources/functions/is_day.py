from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI
from dataclasses import dataclass
from base64 import b64decode


def is_day(dd):
    from datetime import datetime
    return datetime.today().day == int(dd)
