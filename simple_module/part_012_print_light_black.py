

from pkg_py.pk_system_layer_color_map import ColormaColorMap
from pkg_py.simple_module.part_003_print_prompt_via_colorama import print_prompt_via_colorama


def print_light_black(prompt, flush=True, line_feed_mode=1):
    print_prompt_via_colorama(prompt, ColormaColorMap.LIGHTBLACK_EX, flush, line_feed_mode)
