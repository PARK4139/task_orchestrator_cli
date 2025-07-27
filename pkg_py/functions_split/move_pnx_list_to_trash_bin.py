import traceback
import tomllib
from tkinter import UNDERLINE
from prompt_toolkit import PromptSession
from pkg_py.functions_split.ensure_f_video_loaded_on_losslesscut import ensure_f_video_loaded_on_losslesscut
from os.path import dirname
from enum import Enum
from Cryptodome.Random import get_random_bytes
from pkg_py.functions_split.ensure_pk_program_suicided import ensure_pk_program_suicided
from pkg_py.functions_split.does_pnx_exist import does_pnx_exist


def move_pnx_list_to_trash_bin(pnx_list):
    for pnx in pnx_list:
        if does_pnx_exist(pnx):
            move_pnx_to_pk_recycle_bin(pnx=pnx)
