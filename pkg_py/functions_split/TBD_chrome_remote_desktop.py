from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.directories import D_PKG_TXT
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.functions_split.ensure_command_excuted_to_os import ensure_command_excuted_to_os
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.functions_split.ensure_pressed import ensure_pressed
from pkg_py.functions_split.ensure_window_to_front import ensure_window_to_front


def TBD_chrome_remote_desktop(hostname):
    import inspect

    func_n = inspect.currentframe().f_code.co_name
    f_func_n_txt = rf'{D_PROJECT}\pkg_txt\{func_n}.txt'

    # 페이지 열기
    url =URL_CHROME_REMOTE
    ensure_command_excuted_to_os(cmd=f'explorer "{url}"')
    ensure_printed(str_working=rf'''url="{url}"  {'%%%FOO%%%' if LTA else ''}''')

    # 창 앞으로 이동
    ensure_window_to_front(window_title_seg="Chrome")

    # chrome 창 탭 중 해당 url로 이동
    # move_chrome_tab_by_url(url_to_move=url)

    # 클릭
    click_string(string=hostname)

    # PIN 입력
    token_chrome_remote_pin_encoded = get_token_from_f_txt(f_token=rf'{D_PKG_TXT}\token_chrome_remote_pin.txt',
                                                           initial_str="")
    token_chrome_remote_pin = decode_via_pk_system(token_chrome_remote_pin_encoded)
    write(token_chrome_remote_pin, milliseconds=5000)
    ensure_pressed("enter")
