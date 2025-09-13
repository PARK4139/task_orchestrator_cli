from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.objects.pk_local_test_activate import LTA

@ensure_seconds_measured
def get_window_title_temp():
    return "temp window"