

from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def guide_pk_error_mssage():
    from sources.objects.pk_map_texts import PkTexts
    from sources.objects.pk_local_test_activate import LTA
    import logging
    ensure_not_prepared_yet_guided()
