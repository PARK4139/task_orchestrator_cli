from enum import Enum

# pk_ : pk_ prefix means somthing customed by jung hoon park
# ____________________________________________________________________________________
PK_WSL_DISTRO_N = 'wsl_pk_ubuntu_24_04'
pk_ = 'pk_'


# ____________________________________________________________________________________
# def __init__(self):
#     try:
#         os.system('chcp 65001 >nul')
#         Friday.PYCHARM64_EXE = rf'{os.environ.get("PyCharm Community Edition").replace(";", "")}/pycharm64.exe'
#     except AttributeError:
#         pass
#     except Exception:
#         print_light_black(f"{traceback.format_exc()}")
class PkFilter(Enum):
    url_like = 'url_like'
    url_false = 'url_false'


# ____________________________________________________________________________________
PK_UNDERLINE = '_' * 59 + " "  # 제목작성 시 앞부분에 적용되는 기준인데 pep8 최대권장길이(79)를 기준으로 20 자 내외로 제목작성을 작성을 최대한 준수
PK_UNDERLINESHORT = '_' * 6
pk_INDENTATION_PROMISED = ' ' * 5
PK_BLANK = ' '

COUNTS_FOR_GUIDE_TO_SLEEP = []
ROUTINES = [
    '즐거운일 1개',
    '음악틀기',
    '물 한컵',
    '선풍기로 방환기 1분 이상',
    '세수',
    '로션',
    '아침식사',
    "프로폴리스 한알",
    '물가글(혹시 구내염 있으시면 가글양치)',
    '양치 WITHOUT TOOTH PASTE',
    '양치 WITH TOOTH PASTE',
    '양치 WITH GARGLE',
    '물가글',
    '스트레칭 밴드 V 유지 런지 30개',
    '계단 스쿼트 30 개',
    '푸쉬업 30 개',
    '점심식사',
    '저녁식사',
]
VIDEO_IDS_ALLOWED = [
    '617', '616', '625', '620', '614', '609', '606',
    '315', '313', '303', '302', '308',
    '248', '247', '244', '137', '136', '133',
]
AUDIO_IDS_ALLOWED = [
    '234', '140-2', '140-1', '251', '249', '233', '140', '139',
    # '250',
]

pi = 3.141592
# ____________________________________________________________________________________


# hope to deprecate
members = []  # 리스트에 저장, 런타임 중에만 저장이 유지됨, 앱종료 시 데이터 삭제
todos = []  # 리스트에 저장, 런타임 중에만 저장이 유지됨, 앱종료 시 데이터 삭제
click_detected = False  # 클릭 감지 상태를 저장하는 클래스 변수 # 1 곳에서만 호출됨 # todo : 확인해서 필요없는 기능이면 추후 삭제
NO = "그냥 닫아"
YES = "응"
PYGLET_PLAYER = None  # context 로 state 저장하는 것이 나을 듯.
BIGGEST_PNXS = []  # 300 MB 이상 백업대상
SMALLEST_PNXS = []
PLAYING_SOUNDS = []
PREVIOUS_MP3_LENGTH_USED_IN_SPEAK_AS_ASYNC = 0
