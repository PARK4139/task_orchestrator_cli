import speech_recognition as sr
from sources.functions.ensure_task_orchestrator_cli_wrapper_suicided import ensure_task_orchestrator_cli_wrapper_suicided
from sources.functions.get_pnx_unix_style import get_pnx_unix_style


def is_number_v2(prompt: str):
    try:
        float(prompt)  # 숫자 형태로 변환을 시도
        return 1
    except ValueError:
        return 0
