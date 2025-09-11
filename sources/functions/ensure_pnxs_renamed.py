

def ensure_pnxs_renamed(d_working, mode, with_walking, debug_mode=False):
    import logging
    from sources.objects.pk_local_test_activate import LTA

    logging.debug(rf'''d="{d_working}" mode="{mode}"  {'%%%FOO%%%' if LTA else ''}''')

    ensure_pnxs_renamed_from_keywords_to_keyword_new_at_d(d=d_working, mode=mode, with_walking=with_walking)
    ensure_pnxs_renamed_from_pattern_to_pattern_new_via_routines_at_d(d=d_working, mode=mode, with_walking=with_walking)
    ensure_pnxs_renamed_from_keywords_to_keyword_new_at_d(d=d_working, mode=mode, with_walking=with_walking)
