def get_validated(target: any):
    import inspect
    func_n = inspect.currentframe().f_code.co_name
    if target is None:
        target = "논값"
    if target == "":
        target = "공백"
    if type(target) == str:
        if is_pattern_in_prompt(prompt=target, pattern=r'[^a-zA-Z0-9가-힣\s]',
                                with_case_ignored=False):  # 특수문자 패턴 정의( 알파벳, 숫자, 한글, 공백을 제외한 모든 문자)
            target = get_str_replaced_special_characters(target, "$특수문자$")
        return target
    else:
        return target
