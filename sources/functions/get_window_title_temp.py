from sources.functions.ensure_seconds_measured import ensure_seconds_measured
from sources.objects.pk_local_test_activate import LTA

@ensure_seconds_measured
def get_window_title_temp():
    return "임시 생성 창(닫으셔도 되요)"