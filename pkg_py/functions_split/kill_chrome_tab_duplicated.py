

from pkg_py.pk_system_object.local_test_activate import LTA

from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.pk_press import pk_press
from pkg_py.functions_split.is_window_opened import is_window_opened
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def kill_chrome_tab_duplicated():
    chrome_tab_urls_processed = []  # 이미 처리된 URL을 저장하는 리스트
    loop_limit = 10
    loop_out_cnt = 0

    while 1:
        window_title = "Chrome"
        if is_window_opened(window_title_seg=window_title):
            ensure_window_to_front(window_title_seg=window_title)

        pk_print(working_str=rf'''loop_out_cnt="{loop_out_cnt}"  {'%%%FOO%%%' if LTA else ''}''')
        pk_print(working_str=rf'''loop_limit="{loop_limit}"  {'%%%FOO%%%' if LTA else ''}''')

        # 탭을 전환하고 URL을 가져옵니다.
        pk_press("ctrl", "l")
        pk_sleep(milliseconds=5)
        url_dragged = get_text_dragged()

        # 중복 여부 확인
        if url_dragged in chrome_tab_urls_processed:
            pk_print(working_str=rf'''URL already processed: "{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
            pk_press("ctrl", "tab")  # 다음 탭으로 이동
            loop_out_cnt += 1
            if loop_out_cnt >= loop_limit:
                break
            continue

        # 다음 탭으로 전환 후 URL 가져오기
        pk_press("ctrl", "tab")
        pk_sleep(milliseconds=5)
        pk_press("ctrl", "l")
        pk_sleep(milliseconds=5)
        url_dragged_new = get_text_dragged()

        pk_print(working_str=rf'''url_dragged="{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
        pk_print(working_str=rf'''url_dragged_new="{url_dragged_new}"  {'%%%FOO%%%' if LTA else ''}''')

        # 중복된 URL이면 탭 닫기
        if url_dragged == url_dragged_new:
            pk_print(working_str=rf'''Closing duplicate tab for URL: "{url_dragged}"  {'%%%FOO%%%' if LTA else ''}''')
            pk_press("ctrl", "w")  # 탭 닫기
            continue

        # 처리된 URL을 리스트에 추가
        chrome_tab_urls_processed.append(url_dragged)
        pk_print(
            working_str=rf'''chrome_tab_urls_processed="{chrome_tab_urls_processed}"  {'%%%FOO%%%' if LTA else ''}''')

        # 최대 반복 횟수 초과 시 종료
        loop_out_cnt += 1
        if loop_out_cnt >= loop_limit:
            break
