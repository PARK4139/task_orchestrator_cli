from sources.functions.ensure_seconds_measured import ensure_seconds_measured


@ensure_seconds_measured
def ensure_pk_scheduler_enabled():
    import logging

    from functions import ensure_slept

    from sources.objects.pk_scheduler import get_scheduler
    try:
        scheduler = get_scheduler()
        scheduler.start()

        while True: # 필요한 로직
            import time
            # ensure_slept(seconds=1)
            ensure_slept(seconds=30)

    except KeyboardInterrupt:
        # Ctrl+C로 종료 시 스케줄러 중지
        get_scheduler().stop()
        logging.debug("스케줄러가 사용자 요청으로 중지되었습니다.")
