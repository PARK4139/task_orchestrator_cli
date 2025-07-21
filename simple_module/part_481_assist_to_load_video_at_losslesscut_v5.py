from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.pk_system_layer_directories import D_DOWNLOADS, D_PKG_PKL
from pkg_py.pk_system_layer_directories import D_WORKING
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_files import F_HISTORICAL_PNX
from pkg_py.simple_module.part_001_ensure_console_cleared import ensure_console_cleared
from pkg_py.simple_module.part_001_set_pk_context_state import set_pk_context_state
from pkg_py.simple_module.part_002_set_pk_context_state_milliseconds_for_speed_control_forcely import \
    set_pk_context_state_milliseconds_for_speed_control_forcely
from pkg_py.simple_module.part_003_get_list_sorted import get_list_sorted
from pkg_py.simple_module.part_003_write_list_to_f import write_list_to_f
from pkg_py.simple_module.part_005_get_nx import get_nx
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_009_pk_sleep import pk_sleep
from pkg_py.simple_module.part_014_pk_print import pk_print
from pkg_py.simple_module.part_017_get_pnx_os_style import get_pnx_os_style
from pkg_py.simple_module.part_019_pk_print_state import pk_print_state
from pkg_py.simple_module.part_190_pk_press import pk_press
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist
from pkg_py.simple_module.part_311_is_window_opened import is_window_opened
from pkg_py.simple_module.part_312_is_window_title_opened import is_window_title_opened
from pkg_py.simple_module.part_330_get_d_working import get_d_working
from pkg_py.simple_module.part_400_is_window_title_front import is_window_title_front
from pkg_py.simple_module.part_467_get_video_filtered_list import get_video_filtered_list
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from pkg_py.simple_module.part_474_get_f_video_to_load import get_f_video_to_load
from pkg_py.simple_module.part_475_rerun_losslesscut import rerun_losslesscut
from pkg_py.simple_module.part_477_is_losslesscut_running import is_losslesscut_running
from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from pkg_py.simple_module.part_804_get_historical_list import get_historical_list


def assist_to_load_video_at_losslesscut_v5(max_files=30):
    # it wors at windows

    import inspect

    pk_context_state = SpeedControlContext()

    try:
        func_n = inspect.currentframe().f_code.co_name
        F_CACHE = f"{D_PKG_PKL}/{func_n}.pkl"
        # ensure_pnx_removed(pnx=F_CACHE)
        # if not does_pnx_exist(pnx=F_CACHE):
        #     pk_print(f'''의도대로 동작''', print_color='green')
        #     return
        historical_pnx_list = get_historical_list(f=F_HISTORICAL_PNX)
        option_values = historical_pnx_list + get_list_sorted(
            working_list=[get_d_working(), D_WORKING, D_PROJECT, D_DOWNLOADS], mode_asc=1)
        d_working = get_value_completed(key_hint='d_working=', values=option_values)
        d_working = get_pnx_os_style(pnx=d_working)
        d_working = d_working.strip()
        values_to_save = []
        values_all = [d_working] + historical_pnx_list + option_values
        for value in values_all:
            if does_pnx_exist(pnx=value):
                values_to_save.append(value)
        write_list_to_f(f=F_HISTORICAL_PNX, working_list=values_to_save, mode="w")
        ext_allowed_list = ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm']
        video_ignored_keyword_list = ['-seg', 'SEG-']
        f_video_list_allowed = get_video_filtered_list(d_working, ext_allowed_list, video_ignored_keyword_list)[
                               :max_files]
        f_video_to_load = get_f_video_to_load(f_video_list_allowed)
        loop_cnt = 1
        state = {'running': 0, 'loading': 0, 'loaded': 0, 'playing': 0}
        while True:
            ensure_console_cleared()
            if f_video_to_load is None:
                pk_print(f'''f_video_to_load is None {'%%%FOO%%%' if LTA else ''}''')
                f_video_list_allowed = get_video_filtered_list(d_working, ext_allowed_list, video_ignored_keyword_list)[
                                       :max_files]
                f_video_to_load = get_f_video_to_load(f_video_list_allowed)
                continue
            pk_print_state(state=state, pk_id="%%%FOO%%%")
            if not does_pnx_exist(pnx=f_video_to_load):
                f_video_to_load = get_f_video_to_load(f_video_list_allowed)
                set_pk_context_state_milliseconds_for_speed_control_forcely(value=100)
                state['playing'] = 0
            if state == {'running': 1, 'loading': 1, 'loaded': 1, 'playing': 0}:
                window_title = f"정리 중 - LosslessCut"
                if is_window_opened(window_title_seg=window_title):
                    state = {'running': 0, 'loading': 0, 'loaded': 0, 'playing': 0}
                    continue
            pk_print_state(state=state, pk_id="%%%FOO%%%")
            if not is_losslesscut_running(F_CACHE):
                rerun_losslesscut(F_CACHE)
                state['running'] = 1
                # if f_video_to_load is None:
                #     return
                load_f_video_on_losslesscut(f_video_to_load)
                state['playing'] = 0
            else:
                state['running'] = 1
            pk_print_state(state=state, pk_id="%%%FOO%%%")
            window_title = "LosslessCut"
            if is_window_title_opened(window_title):
                load_f_video_on_losslesscut(f_video_to_load)
                state['playing'] = 0
                continue
            window_title = "Loading file - LosslessCut"
            if is_window_title_opened(window_title):
                ensure_window_to_front(window_title_seg=window_title)
                if is_window_title_front(window_title):
                    pk_press("esc")
                state['loading'] = 1
                state['playing'] = 0
                continue
            window_title = "파일 불러오는 중 - LosslessCut"
            if is_window_title_opened(window_title):
                ensure_window_to_front(window_title_seg=window_title)
                if is_window_title_front(window_title):
                    pk_press("esc")
                state['loading'] = 1
                state['playing'] = 0
                continue
            window_title = f"파일 불러오는 중 - {get_nx(f_video_to_load)} - LosslessCut"
            if is_window_title_opened(window_title):
                ensure_window_to_front(window_title_seg=window_title)
                if is_window_title_front(window_title):
                    pk_press("esc")
                state['loading'] = 1
                state['playing'] = 0
                continue
            pk_print_state(state=state, pk_id="%%%FOO%%%")
            if is_window_title_opened(f"{get_nx(f_video_to_load)} - LosslessCut"):
                state['loaded'] = 1
            pk_print_state(state=state, pk_id="%%%FOO%%%")
            if state == {'running': 1, 'loading': 1, 'loaded': 1, 'playing': 0}:
                window_title = f"{get_nx(f_video_to_load)} - LosslessCut"
                while 1:
                    ensure_window_to_front(window_title_seg=window_title)
                    if is_window_title_front(window_title):
                        pk_press("esc")
                        pk_sleep(milliseconds=300)
                        pk_press("space")
                        state['playing'] = 1
                        # for _ in range(10):
                        #     pk_sleep(milliseconds=300)
                        #     pk_press("tab")
                        # pk_sleep(milliseconds=300)
                        # pk_press("space")
                        # click_mouse_left_display_center()
                        pk_print(f'''step 1{'%%%FOO%%%' if LTA else ''}''')
                        break
            pk_print_state(state=state, pk_id="%%%FOO%%%")
            if state == {'running': 1, 'loading': 0, 'loaded': 1, 'playing': 0}:
                window_title = f"{get_nx(f_video_to_load)} - LosslessCut"
                while 1:
                    ensure_window_to_front(window_title_seg=window_title)
                    if is_window_title_front(window_title):
                        pk_press("esc")
                        pk_sleep(milliseconds=300)
                        pk_press("space")
                        state['playing'] = 1
                        pk_sleep(milliseconds=300)
                        pk_press("f11")
                        pk_sleep(milliseconds=300)
                        pk_print(f'''step 2{'%%%FOO%%%' if LTA else ''}''')
                        break
                state = {'running': 1, 'loading': 1, 'loaded': 1, 'playing': 1}
            pk_print_state(state=state, pk_id="%%%FOO%%%")
            set_pk_context_state(state, pk_context_state)
            pk_sleep(milliseconds=pk_context_state.milliseconds_for_speed_control)
            loop_cnt = loop_cnt + 1
    except Exception as e:
        import traceback
        pk_print(f'''{traceback.format_exc()}  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
