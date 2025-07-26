from tkinter import UNDERLINE
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

from pkg_py.functions_split.ensure_printed import ensure_printed
from tkinter import UNDERLINE

from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.functions_split.ensure_printed import ensure_printed


def guide_to_manual_remedy(prompt_remedy):
    print(f'\n')
    ensure_copied(str_working=prompt_remedy)
    ensure_printed(f'{PK_UNDERLINE}')
    ensure_printed(f'{STAMP_TRY_GUIDE} {prompt_remedy}')
    ensure_printed(f'{PK_UNDERLINE}')
