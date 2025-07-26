from pkg_py.functions_split.ensure_printed import ensure_printed


def add_os_sys_environment_variable(environment_variable_name: str, environment_variable_value: str):
    import inspect
    import sys

    """시스템 환경변수 path 업데이트"""
    func_n = inspect.currentframe().f_code.co_name
    ensure_printed("테스트가 필요한 함수를 적용하였습니다")
    ensure_printed("기대한 결과가 나오지 않을 수 있습니다")
    ensure_printed("업데이트 전 시스템 환경변수")
    for i in sys.path:
        ensure_printed(i, print_color='blue')
    sys.path.insert(0, environment_variable_value)
    sys.path.append(environment_variable_value)
    ensure_printed("업데이트 전 시스템 환경변수")
    for i in sys.path:
        ensure_printed(i, print_color='blue')
