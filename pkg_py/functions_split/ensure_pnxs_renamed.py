

def ensure_pnxs_renamed(d_working, mode, with_walking, debug_mode=False):
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from pkg_py.system_object.local_test_activate import LTA

    ensure_printed(str_working=rf'''d="{d_working}" mode="{mode}"  {'%%%FOO%%%' if LTA else ''}''')

    ensure_pnxs_renamed_from_keywords_to_keyword_new_at_d(d=d_working, mode=mode, with_walking=with_walking)
    ensure_pnxs_renamed_from_pattern_to_pattern_new_via_routines_at_d(d=d_working, mode=mode, with_walking=with_walking)
    ensure_pnxs_renamed_from_keywords_to_keyword_new_at_d(d=d_working, mode=mode, with_walking=with_walking)
