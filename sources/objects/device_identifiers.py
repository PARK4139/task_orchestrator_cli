import logging
from abc import ABC
from enum import Enum, auto

from functions.get_caller_n import get_caller_n


class DeviceState(Enum):
    DISCONNECTED = auto()
    CONNECTED = auto()
    BUSY = auto()
    ERROR = auto()
    UNKNOWN = auto()


class PkDeviceIdentifiers(Enum):
    asus_desktop = "asus_desktop"
    jetson_agx_xavier = "jetson_agx_xavier"
    esp32_dev = "esp32_dev"
    arduino_nano = "arduino_nano(Atmege328P)"
    arduino_nano_esp32 = "arduino_nano_esp32"
    jetson_nano = "jetson_nano"
    ras_berry_pi_4_b_plus = "ras_berry_pi_4_b_plus"
    undefined = "undefined"


class PkDevice(ABC):
    def __init__(self, identifier: "PkDeviceIdentifiers", nick_name=None):
        """
        공통 속성 초기화
        :param identifier: 디바이스의 고유 식별자
        :param nick_name: 디바이스의 이름
        """
        self._identifier = identifier
        self._nick_name = nick_name
        self._state = DeviceState.DISCONNECTED
        caller_n = get_caller_n()
        logging.debug(f'{caller_n} initiallized')

    @property  # getter
    def identifier(self) -> "PkDeviceIdentifiers":
        """디바이스의 고유 식별자를 가져옵니다."""
        return self._identifier

    @property
    def nick_name(self) -> str:
        """디바이스의 별명을 가져옵니다."""
        return self._nick_name

    @nick_name.setter  # setter
    def nick_name(self, value: str):
        """디바이스의 별명을 설정합니다."""
        self._nick_name = value

    @property
    def state(self) -> DeviceState:
        """현재 디바이스 상태를 반환합니다."""
        return self._state

    @state.setter
    def state(self, new_state: DeviceState):
        """디바이스의 상태를 업데이트하고 로그를 남깁니다."""
        if self._state != new_state:
            logging.debug(f"상태 변경: {self._state.name} -> {new_state.name}")
            self._state = new_state

    # @abstractmethod  # 자식 클래스에서 반드시 구현강제(메소드 오버라이딩 강제)
    # def connect(self) -> bool:
    #     """디바이스에 연결합니다"""
    #     pass
    #
    # @abstractmethod
    # def disconnect(self) -> bool:
    #     """디바이스 연결을 해제합니다"""
    #     pass
    #
    # @abstractmethod
    # def get_status(self) -> dict:
    #     """디바이스의 현재 상태 정보를 반환합니다"""
    #     pass

    # TODO : 아래 함수들은 상속해서 사용할 함수들
    def __str__(self):
        return f"{self.nick_name} (ID: {self.identifier}, State: {self.state.name})"

    @classmethod
    def to_str(self):
        # TODO  :
        return self.__str__()

    @classmethod
    def to_list(cls):
        return [value for key, value in cls.__dict__.items() if not key.startswith("__")]

    def to_dict(self):
        result = {}
        for key, value in self.__class__.__dict__.items():
            if not key.startswith("__") and isinstance(value, str):
                result[key] = getattr(self, key, value)
        result.update(
            {
                key: value
                for key, value in self.__dict__.items()
                if not key.startswith("__")
            }
        )
        return result

    def to_json(cls):
        pass
