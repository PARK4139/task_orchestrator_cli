from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.pk_system_object.state_via_context import SpeedControlContext
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state

from pkg_py.functions_split.pk_print import pk_print


def ensure_d_size_stable(d_working, limit_seconds):
    """_d_ 크기와 f 개수가 일정한지 확인"""

    import time
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    prev_size, prev_count = get_d_size_and_f_cnt(d_working)

    time_s = time.time()
    pk_context_state = SpeedControlContext()

    pk_print(f'''started at {time_s} for {limit_seconds} seconds stable monitoring{'%%%FOO%%%' if LTA else ''}''')
    while 1:
        pk_sleep(milliseconds=pk_context_state.milliseconds_for_speed_control)
        cur_size, cur_count = get_d_size_and_f_cnt(d_working)  # 현재 크기 및 f 개수 확인
        set_pk_context_state((cur_size, cur_count), pk_context_state)  # 상태 변화 감지

        pk_print(
            f'''d size: {cur_size}, f cnt: {cur_count}, pk_state.milliseconds_for_speed_control={pk_context_state.milliseconds_for_speed_control} {'%%%FOO%%%' if LTA else ''}''')

        # _d_ 크기나 f 개수가 변경되면 즉시 0 반환
        if cur_size != prev_size or cur_count != prev_count:
            if LTA:
                pk_print(f"d size stable = 0")
            return 0
        time_e = time.time()
        time_delta = time_e - time_s
        if limit_seconds < time_delta:
            if LTA:
                pk_print(f"d size stable = 1")
            pk_print(f'''ensured d size is stable for {limit_seconds} seconds{'%%%FOO%%%' if LTA else ''}''')
            return 1  # 일정 시간 동안 변화가 없으면 안정적이라고 판단
