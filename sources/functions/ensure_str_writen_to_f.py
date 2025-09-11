from pathlib import Path

from sources.objects.encodings import Encoding


def ensure_str_writen_to_f(msg: str, f: str or Path, mode: str = "a", encoding=None) -> None:
    from enum import Enum
    encoding: Enum

    encoding = encoding or Encoding.UTF8  # None 또는 False 인 경우 Encoding.UTF8를 할당 (**"단축 평가(short-circuit evaluation)를 활용한 기본값 할당"**)

    f = str(f)
    with open(file=f, mode=mode, encoding=encoding.value) as file:
        file.write(msg)
