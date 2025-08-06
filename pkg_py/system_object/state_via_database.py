import threading


class PkSqlite3DB:
    from typing import Any
    from typing import Optional

    from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    @ensure_seconds_measured
    def __init__(self):

        from pkg_py.system_object.files import F_PK_SYSTEM_SQLITE
        import sqlite3

        self.sqlite3 = sqlite3

        self.pk_db_pnx = F_PK_SYSTEM_SQLITE
        self.ensure_pk_db(self.pk_db_pnx)
        self.pk_db_connection = sqlite3.connect(self.pk_db_pnx)
        self.ensure_pk_db_table()

    def ensure_pk_db(self, pk_db_pnx):
        import os

        # sqlite3 는 file 기반이다. file 이 있어야 한다.
        if not os.path.exists(pk_db_pnx):
            os.makedirs(os.path.dirname(pk_db_pnx), exist_ok=True)

    def ensure_pk_db_table(self):
        cur = self.pk_db_connection.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS pk_table_state (
                id TEXT PRIMARY KEY,
                question TEXT,
                options_json TEXT,
                answer TEXT
            )
        """)
        self.pk_db_connection.commit()

    def save_answer(
            self,
            db_id: str,
            question: str,
            options: list[str],
    ) -> str:

        from pkg_py.functions_split.get_value_completed import get_value_completed
        import json
        answer = get_value_completed(
            key_hint=f'{question} ',
            values=options
        )

        cur = self.pk_db_connection.cursor()
        cur.execute("""
            INSERT INTO pk_table_state (id, question, options_json, answer)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                question=excluded.question,
                options_json=excluded.options_json,
                answer=excluded.answer
        """, (db_id, question, json.dumps(options), answer))
        self.pk_db_connection.commit()
        return answer

    def get_v1(self, db_id: str) -> Optional[str]:

        from pkg_py.system_object.local_test_activate import LTA
        # db 에서 상태를 가져옴
        cur = self.pk_db_connection.cursor()
        cur.execute("SELECT answer FROM pk_table_state WHERE id = ?", (db_id,))
        row = cur.fetchone()
        value = row[0] if row else None
        print(f'''db_id=value : {db_id}={value} {'%%%FOO%%%' if LTA else ''}''')
        return value

    def default_input_func(self, message: str, answer_options: list[str]) -> str:

        print(message)
        for i, opt in enumerate(answer_options):
            print(f"{i + 1}. {opt}")
        choice = input("선택: ")
        try:
            idx = int(choice.strip()) - 1
            return answer_options[idx]
        except:
            return answer_options[0]

    def reset_values(self, db_id: str):

        # TBD : reset_key() 도 있으면 좋겠다

        # pk db 초기화
        cur = self.pk_db_connection.cursor()
        cur.execute("UPDATE pk_table_state SET answer = NULL WHERE id = ?", (db_id,))
        self.pk_db_connection.commit()
        print(f"db_id({db_id}) is reset")

    def set_values(self, db_id: str, values: Any):

        self.set_values_v2(db_id, values)

    def set_values_v1(self, db_id: str, values):

        """
        # value 가 str 인 경우는 처리가능
        # TBD value 가 list 인 경우도 처리 가능하도록
        주어진 db_id에 대해 answer 값을 설정합니다.
        값이 이미 존재하면 업데이트하고, 없다면 새로 추가합니다.
        """
        cur = self.pk_db_connection.cursor()

        # 먼저 해당 id가 존재하는지 확인
        cur.execute("SELECT COUNT(*) FROM pk_table_state WHERE id = ?", (db_id,))
        exists = cur.fetchone()[0] > 0

        if exists:
            cur.execute("UPDATE pk_table_state SET answer = ? WHERE id = ?", (values, db_id))
        else:
            cur.execute("INSERT INTO pk_table_state (id, answer) VALUES (?, ?)", (db_id, values))

        self.pk_db_connection.commit()

    def set_values_v2(self, db_id: str, values: Any):
        import json

        """
        주어진 db_id에 대해 answer 값을 설정합니다.
        value가 str, list, dict 등인 경우 모두 JSON으로 직렬화하여 저장합니다.
        """
        cur = self.pk_db_connection.cursor()

        # value를 JSON 문자열로 직렬화 (ensure_ascii=False → 한글 깨짐 방지)
        serialized_value = json.dumps(values, ensure_ascii=False)

        # 해당 id가 존재하는지 확인
        cur.execute("SELECT COUNT(*) FROM pk_table_state WHERE id = ?", (db_id,))
        exists = cur.fetchone()[0] > 0

        if exists:
            cur.execute("UPDATE pk_table_state SET answer = ? WHERE id = ?", (serialized_value, db_id))
        else:
            cur.execute("INSERT INTO pk_table_state (id, answer) VALUES (?, ?)", (db_id, serialized_value))

        self.pk_db_connection.commit()

    def get_values(self, db_id: str) -> Optional[Any]:

        # return self.get_values_v1(db_id)
        return self.get_values_v2(db_id)

    def get_values_v1(self, db_id: str) -> Optional[Any]:
        import json

        from pkg_py.system_object.local_test_activate import LTA
        """
        주어진 db_id에 대한 answer 값을 가져옵니다.
        JSON 문자열이면 자동으로 역직렬화하여 원래 Python 객체로 반환합니다.
        """

        cur = self.pk_db_connection.cursor()
        cur.execute("SELECT answer FROM pk_table_state WHERE id = ?", (db_id,))
        row = cur.fetchone()
        raw_value = row[0] if row else None

        # JSON 역직렬화 시도
        try:
            value = json.loads(raw_value) if raw_value is not None else None
        except (json.JSONDecodeError, TypeError):
            value = raw_value  # JSON 형식이 아니면 원본 그대로 반환

        print(f'''db_id={db_id}, value={value} {'%%%FOO%%%' if LTA else ''}''')
        return value

    def get_values_v2(self, db_id: str) -> Optional[Any]:
        import json

        from pkg_py.system_object.local_test_activate import LTA
        """
        주어진 db_id에 대한 answer 값을 가져옵니다.
        JSON 문자열이면 자동으로 역직렬화하여 원래 Python 객체로 반환합니다.
        실패 시 문자열 값("True", "False", "null" 등)을 파이썬 타입으로 보정해줍니다.
        """

        cur = self.pk_db_connection.cursor()
        cur.execute("SELECT answer FROM pk_table_state WHERE id = ?", (db_id,))
        row = cur.fetchone()
        raw_value = row[0] if row else None

        if raw_value is None:
            value = None
        else:
            try:
                value = json.loads(raw_value)
            except (json.JSONDecodeError, TypeError):
                # 문자열 보정 처리
                lowered = str(raw_value).strip().lower()
                if lowered == "true":
                    value = True
                elif lowered == "false":
                    value = False
                elif lowered in ("null", "none"):
                    value = None
                elif lowered.isdigit():
                    value = int(lowered)
                else:
                    value = raw_value  # fallback 그대로 반환
        print(f'''[get_values_v2] db_id={db_id}, value={value}, type={type(value)}, repr={repr(value)} {'%%%FOO%%%' if LTA else ''}''')
        return value

    def get_db_id(self, key_name, func_n) -> str:

        self.db_id = rf"{key_name}_via_{func_n}"
        return self.db_id

    def close(self):

        self.pk_db_connection.close()
