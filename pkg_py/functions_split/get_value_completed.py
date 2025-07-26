# from pkg_py.functions_split.ensure_seconds_measured import ensure_seconds_measured
#
#
# @ensure_seconds_measured
def get_value_completed(key_hint, values):
    from pkg_py.functions_split.get_value_completed_v3 import get_value_completed_v3
    # return get_value_completed_v2(key_hint, values)
    return get_value_completed_v3(key_hint, values)
    # return get_value_completed_v4(key_hint, values)
