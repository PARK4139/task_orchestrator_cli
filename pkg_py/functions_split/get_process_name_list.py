def get_process_name_list(unique: bool = True, sort: bool = True) -> list:
    """
    현재 실행 중인 모든 프로세스의 이름 목록을 반환합니다.

    :param unique: True일 경우 중복 remove
    :param sort: True일 경우 알파벳 순 정렬
    :return: 프로세스 이름 리스트
    """
    import psutil
    names = []

    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name']:
                names.append(proc.info['name'])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if unique:
        names = list(set(names))
    if sort:
        names.sort()

    return names


