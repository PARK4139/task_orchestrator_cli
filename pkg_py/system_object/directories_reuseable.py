import socket
from os import environ
from pathlib import Path

HOSTNAME = environ.get('HOSTNAME', socket.gethostname())

D_PROJECT = str(Path(__file__).resolve().parent.parent.parent)
D_PROJECT_PARENTS = str(Path(D_PROJECT).parent)
D_HOME = environ.get('USERPROFILE') or environ.get('HOME')  # Windows 우선, Linux/macOS fallback
D_USERPROFILE = D_HOME 