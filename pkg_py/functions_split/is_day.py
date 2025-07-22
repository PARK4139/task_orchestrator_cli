from pkg_py.pk_system_object.directories_reuseable import D_PROJECT
from dataclasses import dataclass
from base64 import b64decode


def is_day(dd):
    from datetime import datetime
    return datetime.today().day == int(dd)
