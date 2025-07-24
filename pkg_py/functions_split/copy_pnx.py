import zipfile

import win32com.client
import uuid
import time
import random
import cv2
import clipboard
from PySide6.QtWidgets import QApplication
from pynput import mouse
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist
from pkg_py.system_object.local_test_activate import LTA
from fastapi import HTTPException
from enum import Enum
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.get_value_completed import get_value_completed


def copy_pnx(pnx_woking, d_dst, with_overwrite=0):
    if with_overwrite == 1:
        copy_pnx_with_overwrite(pnx_woking, d_dst)
    elif with_overwrite == 0:
        copy_pnx_without_overwrite(pnx_woking, d_dst)
