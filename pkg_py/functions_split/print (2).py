import traceback

from pkg_py.functions_split.get_time_as_ import get_time_as_
from pkg_py.functions_split.get_txt_highlighted import get_txt_highlighted
from pkg_py.functions_split.print_green import print_green
from pkg_py.functions_split.print_light_black import print_light_black
from pkg_py.functions_split.print_light_blue import print_light_blue
from pkg_py.functions_split.print_light_white import print_light_white
from pkg_py.functions_split.print_magenta import print_magenta
from pkg_py.functions_split.print_red import print_red
from pkg_py.functions_split.print_yellow import print_yellow
from pkg_py.system_object.stamps import STAMP_DEBUG, STAMP_INTERACTIVE, STAMP_SUCCEEDED, STAMP_INFO, STAMP_TEST, STAMP_ERROR


def print(str_working, flush=True, print_color='', line_feed_mode=1, STAMP=None, mode_verbose=1, highlight_config_dict=None):
    try:
        STAMP_TIME = f"[ {get_time_as_('now')} ]"
        print_color = print_color.strip()
        default_stamp_by_color = {
            'red': STAMP_ERROR,
            'yellow': STAMP_TEST,
            'blue': STAMP_INFO,
            'green': STAMP_SUCCEEDED,
            'white': STAMP_INTERACTIVE,
            'grey': STAMP_DEBUG,
            '': STAMP_DEBUG,
        }
        stamp_to_use = STAMP if STAMP is not None else default_stamp_by_color.get(print_color, STAMP_DEBUG)

        if mode_verbose == 1:
            if print_color == 'white':
                print_light_white(f"{STAMP_TIME} {stamp_to_use} {str_working}", line_feed_mode, flush)
            elif print_color == 'magenta':
                print_magenta(f"{STAMP_TIME} {str_working}", line_feed_mode, flush)
            else:
                config = {
                    'red': {'red': [stamp_to_use, str_working], 'grey': [STAMP_TIME]},
                    'yellow': {'yellow': [stamp_to_use], 'white': [str_working], 'grey': [STAMP_TIME]},
                    'blue': {'blue': [stamp_to_use], 'white': [str_working], 'grey': [STAMP_TIME]},
                    'green': {'green': [stamp_to_use], 'white': [str_working], 'grey': [STAMP_TIME]},
                    'grey': {'grey': [STAMP_TIME, stamp_to_use, str_working]},
                    '': {'grey': [STAMP_TIME, stamp_to_use, str_working]},
                }.get(print_color, {'grey': [STAMP_TIME, stamp_to_use, str_working]})
                print(get_txt_highlighted(f"{STAMP_TIME} {stamp_to_use} {str_working}", config))

        elif mode_verbose == 0:
            {
                'grey': print_light_black,
                'red': print_red,
                'yellow': print_yellow,
                'blue': print_light_blue,
                'green': print_green,
                'white': print_light_white,
                'magenta': print_magenta,
                '': print_light_black,
            }.get(print_color, print_light_black)(str_working, line_feed_mode, flush)

    except Exception:

        print_light_black(f"[EXCEPTION in ensure_printed] {traceback.format_exc()} ")
