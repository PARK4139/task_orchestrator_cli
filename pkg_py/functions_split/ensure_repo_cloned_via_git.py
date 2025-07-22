import winreg
import webbrowser
import uuid
import colorama
from tkinter import UNDERLINE
from prompt_toolkit import PromptSession
from pkg_py.functions_split.write_list_to_f import write_list_to_f
from pkg_py.functions_split.set_pk_context_state import set_pk_context_state
from pkg_py.pk_system_object.etc import PkFilter
from cryptography.hazmat.primitives import padding
from bs4 import ResultSet
from base64 import b64decode
from pkg_py.functions_split.get_nx import get_nx
from pkg_py.functions_split.is_d import is_d
from pkg_py.functions_split.is_f import is_f

from pkg_py.pk_system_object.Local_test_activate import LTA
from pkg_py.functions_split.pk_print import pk_print
from pkg_py.functions_split.get_d_working import get_d_working


def ensure_repo_cloned_via_git(repo_url: str, d_dst: str):
    import subprocess

    subprocess.run(["git", "clone", repo_url, d_dst], check=True)
    pk_print(f'''git cloned {repo_url} at {d_dst} {'%%%FOO%%%' if LTA else ''}''')
