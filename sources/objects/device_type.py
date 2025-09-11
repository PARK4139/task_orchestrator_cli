from enum import Enum, auto
import dataclasses

@dataclasses.dataclass
class DeviceType(Enum):
    board_model_name = auto()
