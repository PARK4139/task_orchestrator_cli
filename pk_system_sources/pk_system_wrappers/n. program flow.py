import logging

from pk_system_functions import ensure_spoken

step = 1     # 이거는 어디에 넣어둘까?
total_step = 100



def _speak(msg):
    print(rf"[{step}/{total_step}]")
    ensure_spoken(msg)

def _guide_to_press_enter():
    keep_going_guide_msg = f"계속 진행하려면 엔터를 눌러주세요"
    _speak(keep_going_guide_msg)

def _divide_contents(text):
    _line_spliter = "================="
    print(f"{_line_spliter} {text} {_line_spliter} ")


def _print(text):
    print(text)

_guide_to_press_enter()

_print("================= 강사 소개 및 인사 ================= ")
_speak(f"안녕하세요 저는 비전공자 개발자 출신 박정훈입니다.")
_speak(f"제 파이썬 수업에 오신걸 환영해요.")
_speak(f"제 목표는 chatGPT 에게 물어보는고 방법을 얻고 피드백을 내 프로그램에 적용하고")
_speak(f"거두절미하고, 일반인들을 위한 강의를 바로 시작합니다.")



_guide_to_press_enter()


_speak(f"흐름제어")  # 주석

'''
    이곳이 어떤것을 작성하여도 프로그램에 영향을 주지않아요.
'''

_speak(f"프로그램을 만드는 도구")  # IDE 기본사용.   inspection 기능으로 학습효율 극대화
_guide_to_press_enter()

_speak(f"흐름끊기")  # 주석
_guide_to_press_enter()

_speak(f"직선흐름")  # print  psutil
_guide_to_press_enter()

_speak(f"둥근흐름")  # for / while # loop 문
_guide_to_press_enter()

_speak(f"흐름들")
_guide_to_press_enter()





_speak(f"프로그램 흐름 예측해보기")
_guide_to_press_enter()

_speak(f"프로그램 의도 파악하여 복붙해보기")
_guide_to_press_enter()

_speak(f"프로그램 흐름 복붙하여 실험해보기")
_guide_to_press_enter()

_speak(f"프로그램 흐름 실험해보기")
_guide_to_press_enter()

_speak(f"프로그램 흐름 실험결과 비교")  # 로깅





_speak(f"일반인들을 위한 강의 시작합니다.")




_speak("프로그램 만들기")  # 학습자의 컴퓨터 자동화 루틴 만르기
_guide_to_press_enter()





_print("================= 강사 끝인사 ================= ")
_speak(f"cli 인터페이스.")
_speak(f"업무자동화.")
_print(f"수업도 cli기반 자동화로 만들었습니다 ㅎㅎ")
_speak(f"제 수업은 귀납적인 탑다운 방식의 수업입니다. 실험/결과비교 순으로 진행이 됩니다.")
_speak(f"수업도 cli기반 자동화로 만들었습니다 하하")



# TODO :  ver_cpp  ver_arduino 도 필요
# 프로그램 흐름 만들기
# for idx, _ in enumerate([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
#     print()

# minutes = ensure_value_completed(key_hint='minutes=', values=[1, 3, 5])

# +
# 핫리로더 사용해보도록, 핫리로더 주의사항.
