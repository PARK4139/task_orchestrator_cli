from pkg_py.functions_split.print_prompt_via_colorama import print_prompt_via_colorama


def print_green(prompt, flush=True, line_feed_mode=1):
    from pkg_py.pk_system_object.color_map import ColormaColorMap

    print_prompt_via_colorama(prompt, ColormaColorMap.LIGHTGREEN_EX, flush, line_feed_mode)
