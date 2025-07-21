

def get_list_calculated(origin_list, minus_list=None, plus_list=None, dedup=True):
    """
    origin_list에서 minus_list 항목들을 제거하고 plus_list 항목들을 추가합니다.

    Parameters:
        origin_list (list): 원본 리스트
        minus_list (list | None): 제거할 항목 리스트 (None이면 무시)
        plus_list (list | None): 추가할 항목 리스트 (None이면 무시)
        dedup (bool): True면 중복 없이, False면 순서 유지하며 중복 허용

    Returns:
        list: 최종 결과 리스트
    """
    # None 방지
    minus_list = minus_list or []
    plus_list = plus_list or []

    if dedup:
        return list((set(origin_list) - set(minus_list)) | set(plus_list))
    else:
        minus_set = set(minus_list)
        result = [x for x in origin_list if x not in minus_set]
        result.extend(plus_list)
        return result
