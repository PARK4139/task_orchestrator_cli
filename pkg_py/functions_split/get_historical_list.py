from typing import List


def get_historical_list(f) -> List[str]:
    # if not does_pnx_exist(f):
    #     ensure_pnx_made(pnx=f, mode="f")
    # if not os.path.isfile(f):
    #     return []
    with open(f, 'r', encoding='utf-8') as f:
        # 줄 끝 공백 제거하고, 빈 문자열(빈 줄)은 제외
        items = [line.strip() for line in f if line.strip()]
    return items
