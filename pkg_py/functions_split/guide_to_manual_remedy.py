from tkinter import UNDERLINE
from pkg_py.system_object.stamps import STAMP_TRY_GUIDE

from pkg_py.functions_split.pk_print import pk_print
from tkinter import UNDERLINE

from pkg_py.system_object.stamps import STAMP_TRY_GUIDE
from pkg_py.functions_split.pk_print import pk_print


def guide_to_manual_remedy(prompt_remedy):
    print(f'\n')
    pk_copy(str_working=prompt_remedy)
    pk_print(f'{PK_UNDERLINE}')
    pk_print(f'{STAMP_TRY_GUIDE} {prompt_remedy}')
    pk_print(f'{PK_UNDERLINE}')
