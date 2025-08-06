def download_youtube_videos(urls, output_dir=None, max_workers=3):
    """YouTube 비디오 다운로드 (병렬 처리)"""
    try:
        # Lazy import to avoid circular dependency
        try:
            from pkg_py.functions_split.ensure_printed import ensure_printed
            from pkg_py.system_object.map_massages import PkMessages2025
        except ImportError:
            print = lambda msg, **kwargs: print(msg)
            PkMessages2025 = type('PkMessages2025', (), {
                'YOUTUBE_COOKIES_SETUP_FAILED_CONTINUE': 'YouTube 쿠키 설정 실패, 계속 진행',
                'POTPLAYER_START_FAILED_CONTINUE': 'PotPlayer 시작 실패, 계속 진행',
                'METADATA_EXTRACTION_FAILED_SKIP': '메타데이터 추출 실패, 건너뜀',
                'DEBUG_METADATA_EXT': 'DEBUG: 확장자',
                'DEBUG_OUTPUT_FILENAME': 'DEBUG: 출력 파일명',
                'POTPLAYER_PLAYLIST_ADD_FAILED': 'PotPlayer 플레이리스트 추가 실패',
                'EXCEPTION_OCCURRED': '예외 발생'
            })()

        # YouTube 쿠키 설정
        try:
            from pkg_py.functions_split.ensure_youtube_cookies_set import ensure_youtube_cookies_set
            ensure_youtube_cookies_set()
        except Exception as e:
            ensure_printed(f"[{PkMessages2025.YOUTUBE_COOKIES_SETUP_FAILED_CONTINUE}] {e}", print_color="yellow")

        # PotPlayer 시작
        try:
            from pkg_py.functions_split.ensure_pot_player_enabled import ensure_pot_player_enabled
            ensure_pot_player_enabled()
        except Exception as e:
            ensure_printed(f"[{PkMessages2025.POTPLAYER_START_FAILED_CONTINUE}] {e}", print_color="yellow")

        # URL 처리
        if isinstance(urls, str):
            urls = [urls]
        
        if not urls:
            ensure_printed("URL 목록이 비어있습니다.", print_color="red")
            return []

        # 출력 디렉토리 설정
        if output_dir is None:
            from pkg_py.system_object.directories import D_PK_WORKING
            output_dir = Path(D_PK_WORKING) / "youtube_downloads"
        
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # 병렬 다운로드 실행
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for url in urls:
                if url.strip() and not url.strip().startswith('#'):
                    future = executor.submit(download_single_video, url.strip(), output_dir)
                    futures.append(future)

            # 결과 수집
            results = []
            for future in as_completed(futures):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    ensure_printed(f"[{PkMessages2025.EXCEPTION_OCCURRED}] {e}", print_color="red")
                    results.append(None)

        return results

    except Exception as e:
        ensure_printed(f"[{PkMessages2025.EXCEPTION_OCCURRED}] {e}", print_color="red")
        return []


def download_single_video(url, output_dir):
    """단일 비디오 다운로드"""
    try:
        # Lazy import to avoid circular dependency
        try:
            from pkg_py.functions_split.ensure_printed import ensure_printed
            from pkg_py.system_object.map_massages import PkMessages2025
        except ImportError:
            print = lambda msg, **kwargs: print(msg)
            PkMessages2025 = type('PkMessages2025', (), {
                'METADATA_EXTRACTION_FAILED_SKIP': '메타데이터 추출 실패, 건너뜀',
                'DEBUG_METADATA_EXT': 'DEBUG: 확장자',
                'DEBUG_OUTPUT_FILENAME': 'DEBUG: 출력 파일명',
                'POTPLAYER_PLAYLIST_ADD_FAILED': 'PotPlayer 플레이리스트 추가 실패',
                'EXCEPTION_OCCURRED': '예외 발생'
            })()

        # 메타데이터 추출
        try:
            from pkg_py.functions_split.download_youtube_video_via_yt_dlp_v2 import download_youtube_video_via_yt_dlp_v2
            metadata = download_youtube_video_via_yt_dlp_v2(url, output_dir, extract_only=True)
            
            if not metadata:
                ensure_printed(f"[{PkMessages2025.METADATA_EXTRACTION_FAILED_SKIP}] {url}", print_color="yellow")
                return None
                
            title = metadata.get('title', 'unknown')
            clip_id = metadata.get('id', 'unknown')
            ext = metadata.get('ext', 'mp4')
            
            # 디버그 정보
            ensure_printed(f"[{PkMessages2025.DEBUG_METADATA_EXT}] = '{ext}' (타입: {type(ext)})", print_color="yellow")
            ensure_printed(f"DEBUG: title = '{title}'", print_color="yellow")
            ensure_printed(f"DEBUG: clip_id = '{clip_id}'", print_color="yellow")
            
            # 출력 파일명 생성
            safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            output_filename = f"{safe_title}_{clip_id}.{ext}"
            output_path = output_dir / output_filename
            
            ensure_printed(f"[{PkMessages2025.DEBUG_OUTPUT_FILENAME}] = '{output_filename}'", print_color="yellow")
            
            # 실제 다운로드
            ensure_printed(f"DEBUG: download_youtube_video_via_yt_dlp_v2 호출 - ext='{ext}'", print_color="yellow")
            result = download_youtube_video_via_yt_dlp_v2(url, output_dir, output_filename=output_filename)
            
            if result and output_path.exists():
                # PotPlayer 플레이리스트에 추가
                try:
                    from pkg_py.functions_split.ensure_pot_player_playlist_added import ensure_pot_player_playlist_added
                    ensure_pot_player_playlist_added(str(output_path))
                except Exception as e:
                    ensure_printed(f"[{PkMessages2025.POTPLAYER_PLAYLIST_ADD_FAILED}] {e}", print_color="yellow")
                
                # 파일명 정규화 확인
                normalized_filename = output_path.name
                ensure_printed(f"DEBUG: 정규화된 파일명 = '{normalized_filename}'", print_color="yellow")
                ensure_printed(f"DEBUG: clip_id 검색 = '[{clip_id}]'", print_color="yellow")
                
                return {
                    'url': url,
                    'title': title,
                    'clip_id': clip_id,
                    'output_path': str(output_path),
                    'success': True
                }
            else:
                return {
                    'url': url,
                    'success': False,
                    'error': 'Download failed'
                }
                
        except Exception as e:
            ensure_printed(f"[{PkMessages2025.EXCEPTION_OCCURRED}] {url}\n{traceback.format_exc()}", print_color="red")
            return {
                'url': url,
                'success': False,
                'error': str(e)
            }
            
    except Exception as e:
        ensure_printed(f"[{PkMessages2025.EXCEPTION_OCCURRED}] {e}", print_color="red")
        return None
