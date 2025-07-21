from pkg_py.simple_module.part_593_ensure_window_to_front import ensure_window_to_front
from base64 import b64encode

from pkg_py.pk_system_layer_100_Local_test_activate import LTA
from pkg_py.simple_module.part_014_pk_print import pk_print


def ask_to_chatGPT(question: str):
    # todo : ref : not ready
    pk_print(f'''this service is not ready  {'%%%FOO%%%' if LTA else ''}''', print_color='red')
    return

    # str preprocess
    question = question.replace(" ", "+")
    question = question.strip()

    # search in chatGPT
    # todo : candi : chatGPT api 사용
    # todo : candi : selenium, cloudflare 사용
    # todo : final : chatGPT api 사용
    # cmd = f'explorer "https://www.google.com/search?q={question}"  >nul'
    # cmd_to_os(cmd=cmd)
    # pk_print(f'''{cmd}  {'%%%FOO%%%' if LTA else ''}''', print_color="blue"))

    # move window to front
    window_title_seg = rf"ChatGPT"
    while 1:
        ensure_window_to_front(window_title_seg=window_title_seg)
        if is_front_window_title(window_title_seg=window_title_seg):
            break
