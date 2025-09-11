import zipfile

import win32com.client
import uuid
import time
import random
import cv2
import clipboard
from PySide6.QtWidgets import QApplication
from pynput import mouse
from sources.functions.does_pnx_exist import is_pnx_existing
from sources.objects.pk_local_test_activate import LTA
from fastapi import HTTPException
from enum import Enum
from sources.functions.get_nx import get_nx
from sources.functions.ensure_value_completed import ensure_value_completed


def copy_pnx(pnx_woking, d_dst, with_overwrite=0):
    if with_overwrite == 1:
        copy_pnx_with_overwrite(pnx_woking, d_dst)
    elif with_overwrite == 0:
        copy_pnx_without_overwrite(pnx_woking, d_dst)
