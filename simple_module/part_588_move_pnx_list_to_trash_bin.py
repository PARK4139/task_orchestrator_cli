import traceback
import tomllib
from tkinter import UNDERLINE
from prompt_toolkit import PromptSession
from pkg_py.simple_module.part_472_load_f_video_on_losslesscut import load_f_video_on_losslesscut
from os.path import dirname
from enum import Enum
from Cryptodome.Random import get_random_bytes
from pkg_py.simple_module.part_784_kill_self_pk_program import kill_self_pk_program
from pkg_py.simple_module.part_252_does_pnx_exist import does_pnx_exist


def move_pnx_list_to_trash_bin(pnx_list):
    for pnx in pnx_list:
        if does_pnx_exist(pnx):
            move_pnx_to_pk_recycle_bin(pnx=pnx)
