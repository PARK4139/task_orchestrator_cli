




from sources.objects.encodings import Encoding

import logging


def move_memo_lines_containing_keywords_to_f(f_from, f_to, keyword):
    import os
    import inspect
    import tempfile
    try:
        with tempfile.NamedTemporaryFile('w', delete=False, encoding=Encoding.UTF8.value) as f_temp:
            f_temp_n = f_temp.name
            moved_count = 0
            with open(file=f_from, mode='r', encoding=Encoding.UTF8.value) as f_original:
                for line in f_original:
                    if keyword in line:
                        with open(file=f_to, mode='a', encoding=Encoding.UTF8.value) as f_hashed:
                            f_hashed.write(line)
                        moved_count += 1
                    else:
                        f_temp.write(line)

        # 원본 f을 임시 f로 교체합니다.
        os.replace(f_temp_n, f_from)
        from functions.get_caller_n import get_caller_n
        func_n = get_caller_n()
        logging.debug(f"[{func_n}]{moved_count} 개의 줄 이동 fron '{f_from}' to '{f_to}'")

    except FileNotFoundError as e:
        logging.debug(f"오류: f을 찾을 수 없습니다 - {e.filename}")
    except Exception as e:
        logging.debug(f"예상치 못한 오류가 발생했습니다: {e}")
