

from pkg_py.system_object.color_map import ColormaColorMap
from pkg_py.functions_split.print_prompt_via_colorama import print_prompt_via_colorama


def print_red(prompt, flush=True, line_feed_mode=1):
    print_prompt_via_colorama(prompt, ColormaColorMap.RED, flush, line_feed_mode)
