import time

# performance util
# for optimize using cpu resource
"""상태 변화 감지 및 속도 조절"""
class SpeedControlContext:
    def __init__(self):
        self.milliseconds_for_speed_control_origin = 100
        self.milliseconds_for_speed_control = self.milliseconds_for_speed_control_origin
        self.milliseconds_for_speed_control_max = 5000
        # self.milliseconds_for_speed_control_max = 3000
        self.milliseconds_for_speed_control_delta = 200
        self.state_previous = None
        self.time_changed_last = time.time()



