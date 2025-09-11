def print_light_black(prompt, flush=True, line_feed_mode=1):
    from sources.functions.print_prompt_via_colorama import print_prompt_via_colorama
    print_prompt_via_colorama(prompt, 'BRIGHT_BLACK', flush, line_feed_mode)
