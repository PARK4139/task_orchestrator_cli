

# import pywin32
from pkg_py.pk_system_layer_encodings import Encoding


def write_str_to_f(msg: str, f: str, mode: str = "a", encoding=None) -> None:
    """
    문자열을  f에 저장하는 함수.

    :param text: 저장할 문자열
    :param f: f 경로
    :param mode: f 열기 모드 (기본값: "a" - 추가 모드)
    :param encoding: 인코딩 방식 (기본값: Encoding.UTF8)
    """

    from enum import Enum
    encoding: Enum
    # if encoding is None:
    #     encoding = Encoding.UTF8
    encoding = encoding or Encoding.UTF8  # None 또는 False 인 경우 Encoding.UTF8를 할당 (**"단축 평가(short-circuit evaluation)를 활용한 기본값 할당"**)

    with open(file=f, mode=mode, encoding=encoding.value) as file:
        file.write(msg)
