import socket
from os import environ
from pathlib import Path

HOSTNAME = environ.get('HOSTNAME', socket.gethostname())

D_PROJECT = str(Path(__file__).resolve().parent.parent.parent)
D_PROJECT_PARENTS = str(Path(D_PROJECT).parent)
D_HOME = environ.get('USERPROFILE') or environ.get('HOME')  # Windows 우선, Linux/macOS fallback

# 상대경로의 사용은 필연적인데, 상대경로로 경로를 설정할때 기준이 되는 절대경로 하나는 반드시 필요한 것 같다.
