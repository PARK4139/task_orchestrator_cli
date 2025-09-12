from functions.ensure_slept import _SetupOps
from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_pk_scheduler_enabled():
    import logging

    from functions import ensure_slept

    from sources.objects.pk_scheduler import get_pk_scheduler
    try:
        pk_scheduler = get_pk_scheduler()
        pk_scheduler.start()

        while True:  # 필요한 로직
            import time
            # ensure_slept(seconds=1)
            ensure_slept(seconds=30, setup_op=_SetupOps.SILENT)

    except KeyboardInterrupt:
        # Ctrl+C로 종료 시 스케줄러 중지
        get_pk_scheduler().stop()
        logging.debug("스케줄러가 사용자 요청으로 중지되었습니다.")
