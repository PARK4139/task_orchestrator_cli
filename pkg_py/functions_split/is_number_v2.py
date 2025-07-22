import speech_recognition as sr
from pkg_py.functions_split.kill_self_pk_program import kill_self_pk_program
from pkg_py.functions_split.get_pnx_unix_style import get_pnx_unix_style


def is_number_v2(prompt: str):
    try:
        float(prompt)  # 숫자 형태로 변환을 시도
        return 1
    except ValueError:
        return 0
