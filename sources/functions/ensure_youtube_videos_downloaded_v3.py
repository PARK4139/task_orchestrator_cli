def ensure_youtube_videos_downloaded_v3(urls, output_dir=None, max_workers=3):
    from sources.functions.download_single_youtube_video import download_single_youtube_video
    import inspect

    from asyncio import as_completed
    from concurrent.futures import ThreadPoolExecutor
    from pathlib import Path
    import logging
    from sources.objects.pk_map_texts import PkTexts
    from sources.functions.ensure_youtube_cookies_created import ensure_youtube_cookies_created
    from functions.get_caller_n import get_caller_n
    func_n = get_caller_n()

    try:
        # YouTube 쿠키 설정
        try:
            ensure_youtube_cookies_created()
        except Exception as e:
            logging.debug(f"[{PkTexts.YOUTUBE_COOKIES_SETUP_FAILED_CONTINUE}] {e}")

        # PotPlayer 시작 (함수가 정의되지 않았으므로 주석 처리)
        # try:
        #     ensure_pot_player_enabled()
        # except Exception as e:
        #     logging.debug(f"[{PkTexts.POTPLAYER_START_FAILED_CONTINUE}] {e}")

        # URL 처리
        if isinstance(urls, str):
            urls = [urls]

        if not urls:
            logging.debug("URL 목록이 비어있습니다.")
            return []

        # 출력 디렉토리 설정
        if output_dir is None:
            from sources.objects.task_orchestrator_cli_directories import D_PK_WORKING
            output_dir = D_PK_WORKING / f"downloaded_via_{func_n}"

        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # 병렬 다운로드 실행
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for url in urls:
                if url.strip() and not url.strip().startswith('#'):
                    future = executor.submit(download_single_youtube_video, url.strip(), output_dir)
                    futures.append(future)

            # 결과 수집
            results = []
            for future in as_completed(futures):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    logging.debug(f"[{PkTexts.EXCEPTION_OCCURRED}] {e}")
                    results.append(None)

        return results

    except Exception as e:
        logging.debug(f"[{PkTexts.EXCEPTION_OCCURRED}] {e}")
        return []
