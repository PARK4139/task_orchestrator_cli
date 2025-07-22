from pkg_py.functions_split.pk_print import pk_print


def print_data_from_csv(f_csv_path, preview_rows=10):
    import pandas as pd
    import os

    if not os.path.exists(f_csv_path):
        pk_print(f"❌ 파일이 존재하지 않습니다: {f_csv_path}", print_color='red')
        return
    try:
        df = pd.read_csv(f_csv_path)
        pk_print(f"📄 파일 로드 성공: {f_csv_path}", print_color="green")
        pk_print(f"🔢 총 {len(df)}행 × {len(df.columns)}열", print_color="blue")
        pk_print(df)

    except Exception as e:
        pk_print(f"⚠️ CSV 파일 읽기 실패: {e}", print_color='red')
