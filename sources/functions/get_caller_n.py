def get_caller_n():
    # 스택의 바로 이전 프레임이 이 함수를 호출한 프레임입니다.
    # stack()[0]은 현재 프레임(get_caller_n)
    # stack()[1]은 호출자의 프레임
    '''
        # 최상위 호출에서는
        # func_n = get_nx(__file__)

        # 함수내 호출에서는
        # func_n = inspect.currentframe().f_code.co_name

        # 판단귀찮으면
        # from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()
    '''

    import inspect
    import logging
    import os
    caller_frame_record = inspect.stack()[1]
    caller_name = caller_frame_record.function

    if caller_name == '<module>':
        # 최상위 레벨에서 호출됨. 파일 경로를 가져옵니다.
        module_path = caller_frame_record.filename
        caller_name = os.path.splitext(os.path.basename(module_path))[0]
        return caller_name
    else:
        return caller_name
