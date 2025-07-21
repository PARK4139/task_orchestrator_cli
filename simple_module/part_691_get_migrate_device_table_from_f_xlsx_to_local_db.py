from pkg_py.simple_module.part_014_pk_print import pk_print


def get_migrate_device_table_from_f_xlsx_to_local_db():
    """함수 호출 주의 sqlite/table overiwte 됨"""

    import pandas as pd
    import sqlite3

    # 1. 엑셀 파일 로드
    excel_path = f"{D_PROJECT_RELEASE_SERVER}\\영상처리제어기 업무현황.xlsx"
    sheet_name = "업무현황"
    df_raw = pd.read_excel(excel_path, sheet_name=sheet_name)

    # 2. 첫 번째 행을 컬럼으로 설정하고 불필요한 행 remove
    df_raw.columns = df_raw.iloc[0]
    df = df_raw[1:].copy()

    # 3. 필요한 컬럼만 선택
    df = df[[
        "장비식별자", "스티커라벨코드", "Nvidia Serial", "용도",
        "AI fraework 배포파일 버전", "위치", "업무트래킹", "최신업무트래킹"
    ]]
    df = df.dropna(subset=["장비식별자"])

    # 4. SQLite DB로 저장
    db_path = "xc_status.db"
    conn = sqlite3.connect(db_path)
    df.to_sql("xc_status", conn, if_exists="replace", index=False)

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM xc_status;")
    total_rows = cursor.fetchone()[0]
    pk_print(f"xc_status 테이블 총 {total_rows}행 저장됨", print_color='blue')

    pk_print("저장된 데이터 미리보기:", print_color='blue')
    preview_df = pd.read_sql("SELECT * FROM xc_status LIMIT 5", conn)
    print(preview_df)

    pk_print("테이블 컬럼 구조:", print_color='blue')
    cursor.execute("PRAGMA table_info(xc_status);")
    for col in cursor.fetchall():
        print(f"- {col[1]} ({col[2]})")

    conn.close()
    pk_print("마이그레이션 완료: xc_status.db (테이블명: xc_status)", print_color='green')
