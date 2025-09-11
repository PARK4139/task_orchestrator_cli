def ensure_memo_sample_display():
    """DB에 들어간 메모 내용을 랜덤으로 3개 출력하는 함수"""
    from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
    import logging
    from sources.objects.task_orchestrator_cli_files import F_PK_MEMO_SQLITE
    import sqlite3
    from pathlib import Path
    import random
    
    try:
        db_path = F_PK_MEMO_SQLITE
        
        if not db_path.exists():
            logging.debug("메모 DB 파일이 존재하지 않습니다.")
            return False
        
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()
        
        # 전체 메모 수 확인
        cursor.execute("SELECT COUNT(*) FROM pk_memos")
        total_count = cursor.fetchone()[0]
        logging.debug(f"전체 메모 수: {total_count}개")
        
        # 랜덤으로 3개 메모 선택
        random_ids = random.sample(range(1, total_count + 1), min(3, total_count))
        
        logging.debug(f"랜덤 선택된 메모 ID: {random_ids}")
        logging.debug("=" * 80)
        
        for i, memo_id in enumerate(random_ids, 1):
            try:
                cursor.execute("""
                    SELECT id, title, content, tags, category, created_at, updated_at 
                    FROM pk_memos 
                    WHERE id = ?
                """, (memo_id,))
                
                memo = cursor.fetchone()
                if memo:
                    memo_id, title, content, tags, category, created_at, updated_at = memo
                    
                    logging.debug(f"\n 샘플 메모 {i}:")
                    logging.debug(f"🆔 ID: {memo_id}")
                    logging.debug(f"제목: {title}")
                    logging.debug(f"️ 태그: {tags if tags else '없음'}")
                    logging.debug(f"카테고리: {category}")
                    logging.debug(f"생성일: {created_at}")
                    logging.debug(f"수정일: {updated_at}")
                    logging.debug(f"내용 길이: {len(content)}자")
                    logging.debug(f"내용:")
                    
                    # 내용을 줄별로 출력 (긴 내용은 잘라서 표시)
                    content_lines = content.split('\n')
                    for line_num, line in enumerate(content_lines[:10], 1):  # 최대 10줄까지만 표시
                        if line.strip():
                            logging.debug(f"{line_num:2d}: {line[:100]}{'...' if len(line) > 100 else ''}")
                    
                    if len(content_lines) > 10:
                        logging.debug(f"... (총 {len(content_lines)}줄 중 10줄만 표시)")
                    
                    logging.debug("-" * 60)
                else:
                    logging.debug(f"ID {memo_id} 메모를 찾을 수 없습니다.")
                    
            except Exception as e:
                logging.debug(f"메모 {memo_id} 조회 실패: {str(e)}")
        
        cursor.close()
        conn.close()
        
        logging.debug(" 메모 샘플 출력 완료")
        return True
        
    except Exception as e:
        logging.debug(f"메모 샘플 출력 실패: {str(e)}")
        return False

if __name__ == "__main__":
    ensure_memo_sample_display()
