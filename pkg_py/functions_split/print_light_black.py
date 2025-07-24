def print_light_black(prompt, flush=True, line_feed_mode=1):
    from pkg_py.system_object.color_map import ColormaColorMap

    from pkg_py.functions_split.print_prompt_via_colorama import print_prompt_via_colorama
    print_prompt_via_colorama(prompt, ColormaColorMap.LIGHTBLACK_EX, flush, line_feed_mode)
