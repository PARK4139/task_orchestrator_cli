from pkg_py.functions_split.get_pk_program_language import get_pk_program_language


class PkMessages2025:
    VIA_HISTORICAL_FILE = None
    PROCESS = None
    KILL = None
    VIA_FZF = None
    ALREADY_EXIST = None
    EMERGENCY_BACKUP = None
    RETRY = None
    DRY_RUN = None
    AUTO = None
    REVERTED = None
    SATISFIED = None
    FINISHED = None
    INSERTED = None
    WORK = None
    AFTER_SERVICE = None
    ORIGIN = None
    REVERT = None
    SHUTDOWN = None
    DELETE = None
    DEFAULT = None
    JUST = None
    MODE = None
    FALSE = None
    TRUE = None
    ARE_YOU_SURE_EDIT_DONE = None
    BACKUP_DONE = None
    BACKUPED = None
    BACKUP = None
    WRITE = None
    CHECKED = None
    CLASSIFIED = None
    COMPLETE = None
    COMPRESSED = None
    DATA = None
    DETECTED = None
    DONE = None
    DUPLICATE_FUNCTION = None
    ERROR = None
    ERROR_MASSAGE = None
    MASSAGE = None
    EXECUTION = None
    TOTAL_EXCUTION_TIME = None
    TOTAL = None
    TIME = None
    TIME_LEFT = None
    fail = None
    GUIDED = None
    I_WANT_TO_DO_NEXT_TIME = None
    IF_YOU_WANT_MORE_PRESS_ENTER = None
    INFO = None
    LISTED = None
    MILLISECONDS = None
    MOUSE_MOVEMENT = None
    MOVED = None
    NEGATIVE = None
    NO = None
    NOT_PREPARED_YET = None
    OK_I_WILL_DO_IT_NOW = None
    ORGANIZED = None
    PATH_NOT_FOUND = None
    play = None
    POSITIVE = None
    PREVIEW_END = None
    PREVIEW_HEADER = None
    PREVIEW_SUMMARY = None
    PREVIEW = None
    HEADER = None
    SUMMARY = None
    END = None
    REMOVED = None
    SECONDS = None
    SKIPPED = None
    SPLIT_PLAN = None
    SPLIT_SUMMARY = None
    SPLIT = None
    PLAN = None
    STARTED = None
    STATE = None
    STOPPED = None
    success = None
    test = None
    VERSION_INFO = None
    VERSION = None
    WRITE_DONE = None
    WAITING = None
    WILL_SAVE_AS = None
    YES = None
    PAUSE = None
    ARCHIVE_CREATED = None
    IMPORTS_INSERTED = None
    IMPORTS_SKIPPED = None
    _localized_texts = {
        "PAUSE": {"kr": "잠시 멈춤", "en": "Pause"},
        "ARCHIVE_CREATED": {"kr": "압축 파일 생성 완료", "en": "Archive created"},
        "IMPORTS_INSERTED": {"kr": "import 문 삽입 완료", "en": "Imports inserted"},
        "IMPORTS_SKIPPED": {"kr": "이미 import 문 존재하여 건너뜀", "en": "Skipped (imports already exist)"},
        "YES": {"kr": "응", "en": "Yes"},
        "WRITE_DONE": {"kr": "파일 저장 완료", "en": "WRITE DONE"},
        "WRITE": {"kr": "쓰기", "en": "WRITE"},
        "WILL_SAVE_AS": {"kr": "다음 이름으로 저장 예정", "en": "WILL SAVE AS"},
        "WAITING": {"kr": "대기", "en": "WAITING"},
        "VERSION_INFO": {"kr": "버전정보", "en": "VERSION INFO"},
        "VERSION": {"kr": "버전", "en": "VERSION"},
        "INFO": {"kr": "정보", "en": "INFO"},
        "TOTAL_EXCUTION_TIME": {"kr": "프로그램 실행 시간", "en": "TOTAL EXECUTION TIME"},
        "TOTAL": {"kr": "총", "en": "TOTAL"},
        "EXECUTION": {"kr": "실행", "en": "EXECUTION"},
        "TIME": {"kr": "시간", "en": "TIME"},
        "TIME_LEFT": {"kr": "남은 시간", "en": "TIME LEFT"},
        "test": {"kr": "테스트", "en": "Test"},
        "success": {"kr": "성공", "en": "Success"},
        "STOPPED": {"kr": "중지완료", "en": "STOPPED"},
        "STATE": {"kr": "상태", "en": "STATE"},
        "STARTED": {"kr": "시작", "en": "STARTED"},
        "SPLIT_SUMMARY": {"kr": "함수 분할 요약", "en": "SPLIT SUMMARY"},
        "SPLIT_PLAN": {"kr": "분할 계획", "en": "SPLIT PLAN"},
        "SPLIT": {"kr": "분할", "en": "SPLIT"},
        "PLAN": {"kr": "계획", "en": "PLAN"},
        "SKIPPED": {"kr": "스킵", "en": "SKIPPED"},
        "SECONDS": {"kr": "초", "en": "SECONDS"},
        "REMOVED": {"kr": "삭제완료", "en": "REMOVED"},
        "PREVIEW_SUMMARY": {"kr": "미리보기 요약", "en": "PREVIEW SUMMARY"},
        "PREVIEW_HEADER": {"kr": "미리보기 대상 파일", "en": "PREVIEW HEADER"},
        "PREVIEW_END": {"kr": "미리보기 종료", "en": "PREVIEW END"},
        "PREVIEW": {"kr": "미리보기", "en": "PREVIEW"},
        "HEADER": {"kr": "헤더", "en": "HEADER"},
        "SUMMARY": {"kr": "요약", "en": "SUMMARY"},
        "END": {"kr": "종료", "en": "END"},
        "POSITIVE": {"kr": "네", "en": "Yes"},
        "play": {"kr": "재생", "en": "Play"},
        "PATH_NOT_FOUND": {"kr": "경로를 찾을 수 없음", "en": "PATH NOT FOUND"},
        "ORGANIZED": {"kr": "정돈완료", "en": "ORGANIZED"},
        "OK_I_WILL_DO_IT_NOW": {"kr": "지금할게", "en": "I'll do it now"},
        "NOT_PREPARED_YET": {"kr": "아직 준비되지 않은 서비스입니다   :)", "en": "THIS SERVICE IS NOT READY YET :)"},
        "NO": {"kr": "아니오", "en": "No"},
        "NEGATIVE": {"kr": "아니오", "en": "No"},
        "MOVED": {"kr": "이동완료", "en": "MOVED"},
        "MOUSE_MOVEMENT": {"kr": "마우스 움직임", "en": "MOUSE MOVEMENT"},
        "MILLISECONDS": {"kr": "밀리세컨즈", "en": "MILLISECONDS"},
        "LISTED": {"kr": "나열된 목록", "en": "LISTED"},
        "IF_YOU_WANT_MORE_PRESS_ENTER": {"kr": "계속하고 싶으시면 엔터를 누르세요", "en": "if you want to keep process more, press 'ENTER'"},
        "I_WANT_TO_DO_NEXT_TIME": {"kr": "다음에 할게", "en": "I'll do it next time"},
        "GUIDED": {"kr": "가이드", "en": "GUIDED"},
        "fail": {"kr": "실패", "en": "Fail"},
        "ERROR": {"kr": "에러", "en": "ERROR"},
        "ERROR_MASSAGE": {"kr": "에러 메시지", "en": "ERROR MASSAGE"},
        "MASSAGE": {"kr": "메시지", "en": "MASSAGE"},
        "DUPLICATE_FUNCTION": {"kr": "중복 함수 이름", "en": "DUPLICATE FUNCTION"},
        "DONE": {"kr": "완료", "en": "DONE"},
        "DETECTED": {"kr": "감지", "en": "DETECTED"},
        "DATA": {"kr": "데이터", "en": "DATA"},
        "COMPRESSED": {"kr": "압축됨", "en": "COMPRESSED"},
        "COMPLETE": {"kr": "완료", "en": "COMPLETE"},
        "CLASSIFIED": {"kr": "분류완료", "en": "CLASSIFIED"},
        "CHECKED": {"kr": "확인", "en": "CHECKED"},
        "BACKUPED": {"kr": "백업완료", "en": "BACKUPED"},
        "BACKUP_DONE": {"kr": "백업 완료", "en": "BACKUP DONE"},
        "BACKUP": {"kr": "백업", "en": "BACKUP"},
        "ARE_YOU_SURE_EDIT_DONE": {"kr": "편집완료 했니 ?", "en": "ARE YOU SURE EDIT DONE?"},
        "TRUE": {"kr": "설정", "en": "TRUE"},
        "FALSE": {"kr": "미설정", "en": "FALSE"},
        "JUST": {"kr": "그냥", "en": "JUST"},
        "DEFAULT": {"kr": "기본", "en": "DEFAULT"},
        "MODE": {"kr": "모드", "en": "MODE"},
        "DELETE": {"kr": "삭제", "en": "DELETE"},
        "SHUTDOWN": {"kr": "종료", "en": "SHUTDOWN"},
        "REVERT": {"kr": "복구(작업전으로)", "en": "REVERT"},
        "ORIGIN": {"kr": "원본", "en": "ORIGIN"},
        "AFTER_SERVICE": {"kr": "사후처리", "en": "AFTER SERVICE"},
        "WORK": {"kr": "작업", "en": "WORK"},
        "INSERTED": {"kr": "삽입된", "en": "INSERTED"},
        "SATISFIED": {"kr": "만족된", "en": "SATISFIED"},
        "RETRY": {"kr": "재시도", "en": "Retry"},
        "DRY_RUN": {"kr": "예행연습", "en": "Dry run"},
        "AUTO": {"kr": "자동", "en": "Auto"},
        "REVERTED": {"kr": "복구됨", "en": "Reverted"},
        "FINISHED": {"kr": "완료됨", "en": "Finished"},
        "EMERGENCY_BACKUP": {"kr": "응급 백업", "en": "EMERGENCY BACKUP"},
        "ALREADY_EXIST": {"kr": "응급 백업", "en": "ALREADY EXIST"},
        "VIA_FZF": {"kr": "FZF 로 입력", "en": "INPUT VIA FZF"},
        "KILL": {"kr": "죽이다", "en": "KILL"},
        "PROCESS": {"kr": "프로세스", "en": "PROCESS"},
        "VIA_HISTORICAL_FILE": {"kr": "파일 히스토리로 입력", "en": "INPUT VIA HISTORICAL FILE"},
    }

    @classmethod
    def set_lang(cls, lang: str):
        if lang not in ('kr', 'en'):
            raise ValueError(f"[ STATE ] Unsupported language: {lang}")
        for key, val in cls._localized_texts.items():
            setattr(cls, key, val.get(lang, f"[{key}]"))


program_language = get_pk_program_language()
PkMessages2025.set_lang(program_language)
