

# import win32process
from tkinter import UNDERLINE

# from project_database.test_project_database import MySqlUtil
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.pk_print import pk_print


def print_and_write_schedule_template_cyclic_non_to_f_memo_todo_txt(stamp_custom, todo_task_name_str, f_txt, specific_year=None, specific_day=None, specific_month=None):
    str_list = []
    # 요일 딕셔너리
    weekday_dict = {0: "월", 1: "화", 2: "수", 3: "목", 4: "금", 5: "토", 6: "일"}

    # 시작과 끝 구분선 추가
    str_list.append(UNDERLINE)
    section_str = rf"# [non cycle]"
    str_list.append(section_str)

    # 태스크 이름에 주기 정보 추가
    todo_task_name_str = rf"{todo_task_name_str:50s}{stamp_custom}"

    from datetime import datetime
    start_date = datetime(specific_year, specific_month, specific_day)

    task_name = todo_task_name_str
    weekday = weekday_dict[start_date.weekday()]

    # 스케줄 조건 확인
    add_schedule = False
    period = "non"
    if period == "non":
        add_schedule = True

    # 조건에 맞는 경우 태스크 추가
    if add_schedule:
        if start_date.weekday() < 5:  # 근무일 (월 ~ 금)
            task_name = rf"{task_name}[근무일]"
        else:  # 휴일 (토, 일)
            task_name = rf"{task_name}[휴일]"

        if period == "last_day_of_month":  # 말일 처리
            task_name = rf"{task_name}[말일]"
        elif period == "yearly" and specific_month is not None and specific_day is not None:
            task_name = rf"{task_name}[연간]"

        str_list.append(rf'mkr_{start_date.strftime("%Y-%m-%d")} ({weekday}) __:__ "{task_name}"')

    str_list.append(UNDERLINE)

    # 디버깅 출력
    pk_print(working_str="\n".join(str_list))

    pk_print("f에 저장을 원하면 enter를 눌러주세요", print_color='blue')
    input(":")

    # f에 저장
    write_list_to_f(working_list=str_list, f=f_txt, mode='a')

    return 1
