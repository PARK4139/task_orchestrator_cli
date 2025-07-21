

def set_pk_context_state_milliseconds_for_speed_control_forcely(pk_context_state, value: int):
    """
    milliseconds_for_speed_control 값을 강제로 설정합니다.
    자동 상태 변화 조정 로직과 무관하게 직접 제어할 때 사용합니다.
    """
    value = max(0, min(value, pk_context_state.milliseconds_for_speed_control_max))
    pk_context_state.milliseconds_for_speed_control = value
