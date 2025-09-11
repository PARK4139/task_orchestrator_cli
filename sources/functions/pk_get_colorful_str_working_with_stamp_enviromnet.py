import logging
from sources.objects.pk_local_test_activate import LTA


def pk_get_colorful_str_working_with_stamp_enviromnet(func_n):
    """
    함수명과 환경 정보를 포함한 컬러풀한 문자열을 생성합니다.
    
    Args:
        func_n (str): 함수명
        
    Returns:
        str: 컬러풀한 문자열
    """
    import time
    import platform
    import socket
    
    try:
        # 현재 시간
        current_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        
        # 시스템 정보
        system_info = platform.system()
        hostname = socket.gethostname()
        
        # 컬러풀한 문자열 생성
        colorful_str = f"[{current_time}] [{func_n}] [{system_info}@{hostname}]"
        
        if LTA:
            logging.debug(f"Generated colorful string: {colorful_str}")
        
        return colorful_str
        
    except Exception as e:
        logging.debug(f"Failed to generate colorful string: {e}")
        return f"[{func_n}]"
