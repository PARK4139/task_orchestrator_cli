from pkg_py.system_object.local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print


def print_from_pnx_list_to_semantic_words(pnx):
    import inspect
    import re
    from collections import Counter

    func_n = inspect.currentframe().f_code.co_name

    txt_to_exclude_list = [
        F_DB_YAML,
        F_SUCCESS_LOG,
        F_LOCAL_PKG_CACHE,
    ]

    # d_list, f_list=get_sub_pnxs_without_walking(pnx=item_pnx, txt_to_exclude_list=txt_to_exclude_list)
    d_list, f_list = get_sub_pnx_list(pnx=pnx, txt_to_exclude_list=txt_to_exclude_list)

    # pnxs=d_list
    pnxs = f_list

    # 수십개의 f 경로에서 2개 이상의 한글로 구성된 의미론적인 단어를 추출
    special_korean_words = []

    def extract_korean_words(pnx):
        pattern = r'[가-힣]{2,}'  # 한글만 추출하는 정규식
        korean_words = re.findall(pattern=pattern, string=pnx)  # 2개 이상 한글 문자로 이루어진 단어를 찾음
        return korean_words

    for item in pnxs:
        item_pnx = item[0]
        korean_words = extract_korean_words(item_pnx)
        special_korean_words = special_korean_words + korean_words
    word_count = Counter(special_korean_words)
    pk_print(str_working=rf'''word_count="{word_count}"  {'%%%FOO%%%' if LTA else ''}''')
