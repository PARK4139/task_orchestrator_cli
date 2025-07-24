from pkg_py.system_object.local_test_activate import LTA

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.is_window_title_opened import is_window_title_opened
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front
from pkg_py.functions_split.get_f_loading_nx_by_pattern import get_f_loading_nx_by_pattern


def handle_losslesscut_loading(window_title, time_limit, with_key_handing=True):
    import time
    if is_window_title_opened(window_title=window_title):
        time_s = time.time()
        while time.time() - time_s <= time_limit:  # 깔끔한 시간제한루프 예시
            f_loading_nx = get_f_loading_nx_by_pattern(pattern=r"_f_ 불러오는 중 - (.+?) - LosslessCut")
            if is_window_title_opened(window_title=rf"_f_ 불러오는 중 - {f_loading_nx} - LosslessCut"):
                pk_press("esc")
                pk_sleep(milliseconds=300)
                pk_press("space")
                break
            ensure_window_to_front(window_title_seg=window_title)
            # todo : 재생여부가 playing 이 아니면 재생하도록 하고 싶은데 CPU 점유율로는 재생여부를 알 수 가 없네.
    pk_print(rf"handle_losslesscut_loading {window_title} ... {'%%%FOO%%%' if LTA else ''}")
