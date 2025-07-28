from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.pk_ensure_memo_contents_found import ensure_memo_contents_found

def ensure_memo_contents_found_loop():
    ensure_printed("반복 검색 모드입니다. 종료하려면 'q' 또는 'quit'를 입력하세요.", print_color="green")
    while True:
        user_input = input("\n계속 검색하려면 Enter, 종료하려면 'q' 입력: ").strip().lower()
        if user_input in ("q", "quit", "exit"):
            ensure_printed("검색 반복을 종료합니다.", print_color="yellow")
            break
        try:
            ensure_memo_contents_found()
        except Exception as e:
            ensure_printed(f"검색 중 오류 발생: {e}", print_color="red") 