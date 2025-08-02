from pkg_py.functions_split.get_file_id import get_file_id
from pkg_py.functions_split.get_values_from_historical_file_routine import get_values_from_historical_file_routine
from pkg_py.functions_split.ensure_tasklist_got import get_image_names_from_tasklist
import traceback
from pkg_py.functions_split.ensure_process_killed_by_image_name_or_pid import (
    ensure_process_killed_by_image_name,
    get_process_info_by_name
)
from pkg_py.functions_split.ensure_window_title_replaced import ensure_window_title_replaced
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.ensure_exception_routine_done import ensure_exception_routine_done
from pkg_py.functions_split.ensure_finally_routine_done import ensure_finally_routine_done
from pkg_py.functions_split.ensure_colorama_initialized_once import ensure_colorama_initialized_once
from pkg_py.system_object.directories_reuseable import D_PROJECT
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

def pk_ensure_process_killed_by_image_name(image_name, force_kill=False, timeout=10):
    """
    이미지명으로 프로세스를 종료하는 함수 (wrapper)
    
    Args:
        image_name (str): 프로세스 이미지명
        force_kill (bool): 강제 종료 여부 (기본값: False)
        timeout (int): 종료 대기 시간 (초, 기본값: 10)
    
    Returns:
        bool: 종료 성공 여부
    """
    return ensure_process_killed_by_image_name(image_name, force_kill, timeout)

def pk_get_process_info_by_name(process_name):
    """
    프로세스명으로 실행 중인 프로세스 정보를 반환 (wrapper)
    
    Args:
        process_name (str): 프로세스명
    
    Returns:
        list: 프로세스 정보 리스트 [(pid, name, exe), ...]
    """
    return get_process_info_by_name(process_name)

if __name__ == "__main__":
    import inspect
    
    try:
        ensure_colorama_initialized_once()
        ensure_window_title_replaced(get_nx(__file__))
        
        # 파일명에서 함수명 추출
        import os
        file_name = os.path.basename(__file__)
        func_n = file_name.replace('.py', '')

        key_name = "img_name"
        img_name = get_values_from_historical_file_routine(
            file_id=get_file_id(key_name, func_n), 
            key_hint=f'{key_name}=', 
            options_default=get_image_names_from_tasklist(), 
            editable=True
        )
        pk_ensure_process_killed_by_image_name(image_name=img_name)
    except Exception as exception:
        ensure_exception_routine_done(traceback=traceback, exception=exception)
    finally:
        ensure_finally_routine_done(D_PROJECT=D_PROJECT, __file__=__file__, STAMP_TRY_GUIDE=STAMP_TRY_GUIDE) 