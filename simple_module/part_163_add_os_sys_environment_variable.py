from pkg_py.simple_module.part_014_pk_print import pk_print


def add_os_sys_environment_variable(environment_variable_name: str, environment_variable_value: str):
    import inspect
    import sys

    """시스템 환경변수 path 업데이트"""
    func_n = inspect.currentframe().f_code.co_name
    pk_print("테스트가 필요한 함수를 적용하였습니다")
    pk_print("기대한 결과가 나오지 않을 수 있습니다")
    pk_print("업데이트 전 시스템 환경변수")
    for i in sys.path:
        pk_print(i, print_color='blue')
    sys.path.insert(0, environment_variable_value)
    sys.path.append(environment_variable_value)
    pk_print("업데이트 전 시스템 환경변수")
    for i in sys.path:
        pk_print(i, print_color='blue')
