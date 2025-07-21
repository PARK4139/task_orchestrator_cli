import tqdm
import functools
from selenium.webdriver.chrome.options import Options
from pkg_py.pk_system_layer_encodings import Encoding
from pkg_py.pk_system_layer_directories_reuseable import D_PROJECT
from pkg_py.pk_system_layer_400_state_via_context import SpeedControlContext
from pkg_py.simple_module.part_005_get_value_completed import get_value_completed
from pkg_py.simple_module.part_019_get_pnx_list import get_pnx_list


def get_list_converted_from_byte_list_to_str_list(item_byte_list, encoding=None):
    """
    기본적으로 utf-8로 디코딩을 시도하되,
    실패할 경우 cp949로 재시도하고,
    둘 다 실패하면 대체문자로 표시합니다.
    """

    encoding = encoding or Encoding.UTF8
    result = []
    for item in item_byte_list:
        try:
            # 1) 우선 utf-8 디코딩
            decoded = item.decode(encoding)
        except UnicodeDecodeError:
            try:
                # 2) 실패하면 cp949로 재시도
                decoded = item.decode('cp949')
            except UnicodeDecodeError:
                # 3) 그래도 안 되면 대체문자 처리
                decoded = item.decode('utf-8', errors='replace')
        result.append(decoded)
    return result
