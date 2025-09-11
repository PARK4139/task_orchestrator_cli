from sources.functions.print_prompt_via_colorama import print_prompt_via_colorama


def print_light_yellow(prompt, flush=True, line_feed_mode=1):
    print_prompt_via_colorama(prompt, 'BRIGHT_YELLOW', flush, line_feed_mode)
