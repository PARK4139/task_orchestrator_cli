from functions.ensure_guided_not_prepared_yet import ensure_not_prepared_yet_guided
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_command_executed_advanced_sync():
    ensure_not_prepared_yet_guided()