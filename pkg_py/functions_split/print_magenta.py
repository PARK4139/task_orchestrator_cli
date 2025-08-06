from pkg_py.functions_split.print_prompt_via_colorama import print_prompt_via_colorama
from pkg_py.system_object.color_map import ColormaColorMap


def print_magenta(prompt, flush=True, line_feed_mode=1):
    print_prompt_via_colorama(prompt, ColormaColorMap.LIGHTMAGENTA_EX, flush, line_feed_mode)
