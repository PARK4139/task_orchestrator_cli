# TODO : DEPRECATE THIS FILE
import socket
from enum import Enum
from os import environ


HOSTNAME = environ.get('HOSTNAME', socket.gethostname())  #

WSL_PK_DISTRO_N = 'wsl_pk_ubuntu_24_04'
pk_ = 'pk_'


class PkFilter(Enum):  # TODO : will deprecate
    url_like = 'url_like'
    url_false = 'url_false'

PK_DEBUG_LINE = "PK_DEBUG " * 22
PK_USERLESS_LINE = "USELESS " * 22
PK_BLANK = " "
PK_UNDERLINE_HALF = '_' * 33
PK_UNDERLINE = PK_UNDERLINE_HALF * 2 + rf"{PK_BLANK}"  # task_orchestrator_cli_option # python pep8 최대권장길이(79)를 기준으로 13 자 내외로 제목작성을 작성을 최대한 준수
PK_DIVIDER = PK_UNDERLINE  # task_orchestrator_cli_option
PK_UNDERLINESHORT = '_' * 6  # task_orchestrator_cli_option
pk_INDENTATION_PROMISED = ' ' * 5  # task_orchestrator_cli_option
PK_BLANK = ' '  # task_orchestrator_cli_option

COUNTS_FOR_GUIDE_TO_SLEEP = []

ROUTINES = [
    '물 한컵', # 오전작업전준비
    '선풍기로 방환기 1분 이상', # 오전작업전준비
    '세수',    # 오전작업전준비
    '로션',    # 오전작업전준비
    '아침식사',# 오전작업전준비
    "프로폴리스 한알", # 오전작업전준비
    '물가글(혹시 구내염 있으시면 가글양치)', # 오전작업전준비
    '양치 WITHOUT TOOTH PASTE', # 오전작업전준비
    '양치 WITH TOOTH PASTE', # 오전작업전준비
    '양치 WITH GARGLE', # 오전작업전준비
    '물가글', # 오후작업전준비


    '물가글(혹시 구내염 있으시면 가글양치)', # 오후주간작업전준비
    '양치 WITHOUT TOOTH PASTE', # 오후주간작업전준비
    '양치 WITH TOOTH PASTE', # 오후주간작업전준비
    '양치 WITH GARGLE', # 오후주간작업전준비
    '물가글', # 오후주간작업전준비
    '스트레칭 밴드 V 유지 런지 30개', # 오후주간작업전준비
    '계단 스쿼트 30 개', # 오후주간작업전준비
    '푸쉬업 30 개', # 오후주간작업전준비
    '점심식사', # 오후주간작업전준비

    '저녁식사', # 오후야간작업전준비
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
