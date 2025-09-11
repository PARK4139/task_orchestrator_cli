

def get_str_replaced_from_pattern_to_patternless(str_working, pattern):
    import re
    return re.sub(pattern, "", str_working)
