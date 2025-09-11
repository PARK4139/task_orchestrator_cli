from sources.functions.print_prompt_via_colorama import print_prompt_via_colorama


def print_light_blue(prompt, flush=True, line_feed_mode=1):
    print_prompt_via_colorama(prompt, 'BRIGHT_BLUE', flush, line_feed_mode)
