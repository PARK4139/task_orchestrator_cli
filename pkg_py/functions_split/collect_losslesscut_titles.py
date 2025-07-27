import time
from pkg_py.functions_split.get_window_title_list import get_window_title_list

def collect_losslesscut_titles(output_file="losslesscut_titles.log", interval=1.0):
    seen = set()
    with open(output_file, "a", encoding="utf-8") as f:
        while True:
            titles = get_window_title_list()
            for title in titles:
                if "LosslessCut" in title and title not in seen:
                    f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {title}\n")
                    f.flush()
                    print(title)
                    seen.add(title)
            time.sleep(interval)

# 사용 예시
# collect_losslesscut_titles() 