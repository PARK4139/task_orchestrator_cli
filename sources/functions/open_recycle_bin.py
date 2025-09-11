import requests
from sources.functions.ensure_command_executed import ensure_command_executed
from sources.objects.task_orchestrator_cli_directories  import D_TASK_ORCHESTRATOR_CLI

from collections import Counter



def open_recycle_bin():
    ensure_command_executed(cmd='explorer.exe shell:RecycleBinFolder')
