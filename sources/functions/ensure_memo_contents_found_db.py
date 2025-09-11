def ensure_memo_contents_found_db():
    """
    pk_memo.sqlite 데이터베이스에서 메모를 검색하는 함수
    기존 파일 기반 검색을 DB 기반 검색으로 대체
    """
    import logging, get_fzf_command, does_pnx_exist, ensure_chcp_65001, get_os_n, ensure_console_cleared
    from sources.objects.task_orchestrator_cli_files import F_MEMO_WORKING_MD
    from sources.objects.encodings import Encoding
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_LOGS
    from sources.objects.pk_local_test_activate import LTA
    import re
    import subprocess
    import sys
    import locale
    import os
    import time
    import shutil
    import threading
    from pathlib import Path
    import sqlite3

    def get_db_connection():
        """pk_memo.sqlite 데이터베이스 연결을 반환합니다."""
        db_path = Path("task_orchestrator_cli_sensitive/pk_memo.sqlite")
        if not db_path.exists():
            logging.debug(f"데이터베이스 파일이 존재하지 않습니다: {db_path}")
            return None
        
        try:
            conn = sqlite3.connect(str(db_path))
            conn.row_factory = sqlite3.Row  # 컬럼명으로 접근 가능하도록 설정
            return conn
        except Exception as e:
            logging.debug(f"데이터베이스 연결 실패: {str(e)}")
            return None

    def search_memos_in_db(conn, search_keywords):
        """데이터베이스에서 키워드로 메모를 검색합니다."""
        if not conn:
            return []
        
        try:
            cursor = conn.cursor()
            
            # 검색 쿼리 구성 (모든 키워드가 포함된 메모 검색)
            query = """
                SELECT id, title, content, tags, category, file_line_start, file_line_end, created_at, updated_at
                FROM pk_memos 
                WHERE 1=1
            """
            params = []
            
            # 각 키워드에 대해 content와 title에서 검색
            for i, keyword in enumerate(search_keywords):
                query += f" AND (content LIKE ? OR title LIKE ?)"
                params.extend([f"%{keyword}%", f"%{keyword}%"])
            
            query += " ORDER BY updated_at DESC, created_at DESC"
            
            cursor.execute(query, params)
            results = cursor.fetchall()
            
            if LTA:
                logging.debug(f"DB 검색 쿼리: {query}")
                logging.debug(f"검색 파라미터: {params}")
                logging.debug(f"검색 결과 수: {len(results)}")
            
            return results
            
        except Exception as e:
            logging.debug(f"데이터베이스 검색 오류: {str(e)}")
            return []

    def format_memo_content_for_display(memo_row):
        """메모 행을 화면 표시용으로 포맷팅합니다."""
        # 구분선 생성
        divider = "_" * 50
        
        # 메모 내용 구성
        content_parts = []
        
        # 제목
        if memo_row['title']:
            content_parts.append(memo_row['title'])
        
        # 내용
        if memo_row['content']:
            content_parts.append(memo_row['content'])
        
        # 태그
        if memo_row['tags']:
            content_parts.append(f"태그: {memo_row['tags']}")
        
        # 카테고리
        if memo_row['category']:
            content_parts.append(f"카테고리: {memo_row['category']}")
        
        # 메타데이터
        meta_info = []
        if memo_row['file_line_start'] and memo_row['file_line_end']:
            meta_info.append(f"파일 위치: {memo_row['file_line_start']}-{memo_row['file_line_end']}")
        if memo_row['created_at']:
            meta_info.append(f"생성: {memo_row['created_at']}")
        if memo_row['updated_at']:
            meta_info.append(f"수정: {memo_row['updated_at']}")
        
        if meta_info:
            content_parts.append(" | ".join(meta_info))
        
        # 구분선으로 감싸기
        formatted_content = f"{divider}\n" + "\n".join(content_parts) + f"\n{divider}"
        
        return formatted_content

    def display_search_results_db(search_results, search_keywords):
        """DB 검색 결과를 출력합니다."""
        if not search_results:
            keyword_str = " ".join(search_keywords)
            logging.debug(f"'{keyword_str}'가 모두 포함된 메모를 찾을 수 없습니다.")
            return
        
        # 검색 결과 전체 출력
        keyword_str = " ".join(search_keywords)
        logging.debug(f"=== '{keyword_str}'가 모두 포함된 메모 ({len(search_results)}개) ===")
        
        for i, memo_row in enumerate(search_results, 1):
            # 메모 ID와 제목 출력
            memo_id = memo_row['id']
            title = memo_row['title'] or "제목 없음"
            
            # 제목에 키워드 하이라이트 적용
            from sources.functions.get_keyword_colors import highlight_multiple_keywords_fast
            title_highlighted = highlight_multiple_keywords_fast(title, search_keywords)
            title_colored = f'\033[38;5;75m{title_highlighted}\033[0m'
            
            print(f"[{i:>3}] (ID: {memo_id}) {title_colored}")
            
            # 메모 내용 출력
            content = memo_row['content'] or ""
            if content:
                # 내용에 키워드 하이라이트 적용
                content_highlighted = highlight_multiple_keywords_fast(content, search_keywords)
                print(content_highlighted)
            
            # 태그와 카테고리 출력
            if memo_row['tags']:
                print(f"태그: {memo_row['tags']}")
            if memo_row['category']:
                print(f"카테고리: {memo_row['category']}")
            
            # 메타데이터 출력
            meta_parts = []
            if memo_row['file_line_start'] and memo_row['file_line_end']:
                meta_parts.append(f"파일 위치: {memo_row['file_line_start']}-{memo_row['file_line_end']}")
            if memo_row['created_at']:
                meta_parts.append(f"생성: {memo_row['created_at']}")
            if memo_row['updated_at']:
                meta_parts.append(f"수정: {memo_row['updated_at']}")
            
            if meta_parts:
                print(f"메타: {' | '.join(meta_parts)}")
            
            print()  # 빈 줄 추가

    def write_search_results_to_log_db(search_results, search_keywords, log_file_path):
        """DB 검색 결과를 로그 파일에 저장합니다."""
        try:
            with open(log_file_path, 'w', encoding=Encoding.UTF8.value) as f:
                f.write(f"=== '{' '.join(search_keywords)}' DB 검색 결과 ({len(search_results)}개) ===\n")
                f.write(f"생성 시간: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("_" * 80 + "\n\n")
                
                for i, memo_row in enumerate(search_results, 1):
                    f.write(f"[{i}] (ID: {memo_row['id']})\n")
                    f.write(f"제목: {memo_row['title'] or '제목 없음'}\n")
                    f.write(f"내용: {memo_row['content'] or ''}\n")
                    if memo_row['tags']:
                        f.write(f"태그: {memo_row['tags']}\n")
                    if memo_row['category']:
                        f.write(f"카테고리: {memo_row['category']}\n")
                    if memo_row['file_line_start'] and memo_row['file_line_end']:
                        f.write(f"파일 위치: {memo_row['file_line_start']}-{memo_row['file_line_end']}\n")
                    if memo_row['created_at']:
                        f.write(f"생성: {memo_row['created_at']}\n")
                    if memo_row['updated_at']:
                        f.write(f"수정: {memo_row['updated_at']}\n")
                    f.write("_" * 80 + "\n\n")
            
            logging.debug(f"검색 결과가 로그 파일에 저장되었습니다: {log_file_path}")
        except Exception as e:
            logging.debug(f"로그 파일 쓰기 실패: {str(e)}")

    def open_result_log_file():
        """D_TASK_ORCHESTRATOR_CLI_LOGS/ensure_pk_memo_searched.log 파일을 열고 초기화하는 함수"""
        try:
            from sources.functions.ensure_pnx_opened_by_ext import ensure_pnx_opened_by_ext
            from sources.functions.ensure_pnx_made import ensure_pnx_made
            
            # 로그 파일 경로
            log_file = Path(D_TASK_ORCHESTRATOR_CLI_LOGS) / "ensure_pk_memo_searched.log"
            log_file.parent.mkdir(parents=True, exist_ok=True)
            
            # 프로그램 시작 시 로그 파일 초기화
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            initial_content = f"=== 메모 DB 검색 로그 파일 ===\n"
            initial_content += f"프로그램 시작 시간: {current_time}\n"
            initial_content += f"로그 파일이 초기화되었습니다.\n"
            initial_content += "_" * 80 + "\n\n"
            
            # 로그 파일에 초기 내용 쓰기 (덮어쓰기)
            with open(log_file, 'w', encoding=Encoding.UTF8.value) as f:
                f.write(initial_content)
            
            logging.debug(f"로그 파일이 초기화되었습니다: {log_file}")
            
            # 파일 열기
            ensure_pnx_opened_by_ext(str(log_file))
            logging.debug(f"검색 결과 로그 파일이 열렸습니다: {log_file}")
            return str(log_file)
        except Exception as e:
            logging.debug(f"로그 파일 열기 실패: {str(e)}")
            return None

    # 프로그램 시작
    logging.debug("메모 DB 검색 시스템 초기화 ===")
    
    # 로그 파일 열기
    log_file_path = open_result_log_file()
    
    if not log_file_path:
        logging.debug("로그 파일을 열 수 없어 검색 기능이 제한됩니다.")

    if get_os_n() == 'windows':
        ensure_chcp_65001()
        # 추가 인코딩 설정
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
        # locale 설정
        try:
            locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')
        except:
            try:
                locale.setlocale(locale.LC_ALL, 'Korean_Korea.65001')
            except:
                pass

    # 데이터베이스 연결
    db_conn = get_db_connection()
    if not db_conn:
        logging.debug("데이터베이스 연결에 실패했습니다. 프로그램을 종료합니다.")
        return

    try:
        ensure_console_cleared()
        logging.debug("메모 DB 검색 시스템 ===")
        logging.debug("검색할 키워드를 입력하세요: ")
        logging.debug("Ctrl+C: 종료")
        print()  # 빈 줄 추가
        
        # 키워드 입력 받기
        search_input = input("키워드: ").strip()
        
        if not search_input:
            logging.debug("키워드가 입력되지 않았습니다.")
            return
        
        # 키워드 분리
        search_keywords = [kw.strip() for kw in search_input.split() if kw.strip()]
        
        if not search_keywords:
            logging.debug("유효한 키워드가 없습니다.")
            return
        
        logging.debug(f"검색 키워드: {' '.join(search_keywords)}")
        print()
        
        # DB에서 검색 실행
        logging.debug("데이터베이스에서 검색 중...")
        search_results = search_memos_in_db(db_conn, search_keywords)
        
        # 검색 결과 출력
        display_search_results_db(search_results, search_keywords)
        
        # 검색 결과를 로그 파일에 저장
        if log_file_path:
            write_search_results_to_log_db(search_results, search_keywords, log_file_path)
        
        # 검색 완료 메시지
        keyword_str = " ".join(search_keywords)
        if search_results:
            logging.debug(f"검색 완료: '{keyword_str}'가 모두 포함된 메모 {len(search_results)}개를 찾았습니다.")
        else:
            logging.debug(f"'{keyword_str}'가 모두 포함된 메모를 찾을 수 없습니다.")
        
        # 편집 시스템 안내
        if log_file_path:
            logging.debug("편집 시스템이 활성화되었습니다.")
            logging.debug(f"검색 결과를 편집하려면 {log_file_path} 파일을 수정하세요.")
        
    except KeyboardInterrupt:
        logging.debug("검색이 취소되었습니다.")
    except Exception as e:
        logging.debug(f"검색 중 오류 발생: {str(e)}")
    finally:
        # 데이터베이스 연결 종료
        if db_conn:
            db_conn.close()
            logging.debug("데이터베이스 연결이 종료되었습니다.")
