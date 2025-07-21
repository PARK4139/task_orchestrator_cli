from tkinter import UNDERLINE
from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE

from pkg_py.simple_module.part_014_pk_print import pk_print
from tkinter import UNDERLINE

from pkg_py.pk_system_layer_stamps import STAMP_TRY_GUIDE
from pkg_py.simple_module.part_014_pk_print import pk_print


def guide_to_manual_remedy(prompt_remedy):
    print(f'\n')
    pk_copy(working_str=prompt_remedy)
    pk_print(f'{PK_UNDERLINE}')
    pk_print(f'{STAMP_TRY_GUIDE} {prompt_remedy}')
    pk_print(f'{PK_UNDERLINE}')
