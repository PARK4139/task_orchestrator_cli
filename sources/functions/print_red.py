

from sources.functions.print_prompt_via_colorama import print_prompt_via_colorama


def print_red(prompt, flush=True, line_feed_mode=1):
    print_prompt_via_colorama(prompt, 'RED', flush, line_feed_mode)
