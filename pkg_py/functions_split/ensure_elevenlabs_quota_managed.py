def ensure_elevenlabs_quota_managed():
    """
    ElevenLabs API 무료 한도 관리 시스템
    - 남은 무료 한도를 SQLite에 저장
    - 무료 한도 초기화 일자 확인
    - 한도 초과 시 사용 제한
    """
    import sqlite3
    import os
    import requests
    from datetime import datetime, date, timedelta
    from pkg_py.functions_split.ensure_printed import ensure_printed
    
    class ElevenLabsQuotaManager:
        def __init__(self):
            self.db_path = os.path.join(os.path.expanduser("~"), ".pk_system", "elevenlabs_quota.db")
            self.ensure_db_exists()
        
        def ensure_db_exists(self):
            """데이터베이스 및 테이블 생성"""
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 기존 테이블 구조 확인
            cursor.execute("PRAGMA table_info(elevenlabs_quota)")
            columns = [column[1] for column in cursor.fetchall()]
            
            # 한도 테이블 생성 (기존 테이블이 없으면)
            if 'elevenlabs_quota' not in [table[0] for table in cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]:
                cursor.execute('''
                    CREATE TABLE elevenlabs_quota (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        remaining_chars INTEGER DEFAULT 10000,
                        total_used_chars INTEGER DEFAULT 0,
                        reset_date DATE,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
            else:
                # 기존 테이블에 reset_date 컬럼 추가 (없으면)
                if 'reset_date' not in columns:
                    cursor.execute('ALTER TABLE elevenlabs_quota ADD COLUMN reset_date DATE')
                    ensure_printed("🔧 데이터베이스 스키마 업데이트: reset_date 컬럼 추가", print_color='blue')
            
            # 사용 로그 테이블 생성
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS elevenlabs_usage_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    text_length INTEGER,
                    voice_id TEXT,
                    used_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # 초기 데이터가 없으면 생성
            cursor.execute('SELECT COUNT(*) FROM elevenlabs_quota')
            if cursor.fetchone()[0] == 0:
                current_date = date.today()
                next_month = current_date.replace(day=1) + timedelta(days=32)
                next_month = next_month.replace(day=1)
                
                cursor.execute('''
                    INSERT INTO elevenlabs_quota (remaining_chars, total_used_chars, reset_date)
                    VALUES (?, ?, ?)
                ''', (10000, 0, next_month.isoformat()))
            else:
                # 기존 데이터에 reset_date가 없으면 업데이트
                cursor.execute('SELECT reset_date FROM elevenlabs_quota ORDER BY id DESC LIMIT 1')
                result = cursor.fetchone()
                if result and result[0] is None:
                    current_date = date.today()
                    next_month = current_date.replace(day=1) + timedelta(days=32)
                    next_month = next_month.replace(day=1)
                    
                    cursor.execute('''
                        UPDATE elevenlabs_quota 
                        SET reset_date = ?
                        WHERE id = (SELECT MAX(id) FROM elevenlabs_quota)
                    ''', (next_month.isoformat(),))
                    ensure_printed(" 기존 데이터에 reset_date 업데이트", print_color='blue')
            
            conn.commit()
            conn.close()
        
        def get_quota_info(self):
            """현재 한도 정보 조회"""
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT remaining_chars, total_used_chars, reset_date
                FROM elevenlabs_quota 
                ORDER BY id DESC LIMIT 1
            ''')
            
            result = cursor.fetchone()
            conn.close()
            
            if result:
                return {
                    'remaining_chars': result[0],
                    'total_used_chars': result[1],
                    'reset_date': result[2]
                }
            return None
        
        def check_and_reset_quota(self):
            """한도 초기화 확인 및 실행"""
            quota_info = self.get_quota_info()
            if not quota_info:
                return False
            
            reset_date = datetime.strptime(quota_info['reset_date'], '%Y-%m-%d').date()
            current_date = date.today()
            
            if current_date >= reset_date:
                # 한도 초기화
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                
                # 다음 달 1일 계산
                next_month = current_date.replace(day=1) + timedelta(days=32)
                next_month = next_month.replace(day=1)
                
                cursor.execute('''
                    UPDATE elevenlabs_quota 
                    SET remaining_chars = 10000,
                        reset_date = ?,
                        updated_at = CURRENT_TIMESTAMP
                    WHERE id = (SELECT MAX(id) FROM elevenlabs_quota)
                ''', (next_month.isoformat(),))
                
                conn.commit()
                conn.close()
                
                ensure_printed("✅ ElevenLabs 무료 한도가 초기화되었습니다! (10,000자)", print_color='green')
                return True
            
            return False
        
        def check_quota(self, text_length):
            """한도 확인 (별칭 메서드)"""
            return self.can_use_tts(text_length)
        
        def can_use_tts(self, text_length):
            """TTS 사용 가능 여부 확인"""
            self.check_and_reset_quota()  # 초기화 확인
            
            quota_info = self.get_quota_info()
            if not quota_info:
                return False
            
            remaining = quota_info['remaining_chars']
            can_use = remaining >= text_length
            
            if can_use:
                ensure_printed(f"✅ TTS 사용 가능: {text_length}자 사용 예정, 남은 한도: {remaining}자", print_color='green')
            else:
                ensure_printed(f"❌ TTS 사용 불가: {text_length}자 필요, 남은 한도: {remaining}자", print_color='red')
                ensure_printed(" 다음 달 1일에 무료 한도가 초기화됩니다.", print_color='yellow')
            
            return can_use
        
        def update_usage(self, text_length, voice_id=None):
            """사용량 업데이트"""
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 사용 기록 추가
            cursor.execute('''
                INSERT INTO elevenlabs_usage_log (text_length, voice_id)
                VALUES (?, ?)
            ''', (text_length, voice_id or "unknown"))
            
            # 남은 한도 감소
            cursor.execute('''
                UPDATE elevenlabs_quota 
                SET remaining_chars = remaining_chars - ?,
                    total_used_chars = total_used_chars + ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = (SELECT MAX(id) FROM elevenlabs_quota)
            ''', (text_length, text_length))
            
            conn.commit()
            conn.close()
            
            ensure_printed(f"📊 사용량 업데이트: {text_length}자 사용됨", print_color='blue')
        
        def get_usage_statistics(self):
            """사용 통계 조회"""
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # 이번 달 사용량
            current_month = date.today().replace(day=1).isoformat()
            cursor.execute('''
                SELECT SUM(text_length) FROM elevenlabs_usage_log 
                WHERE strftime('%Y-%m', used_at) = strftime('%Y-%m', 'now')
            ''')
            monthly_usage = cursor.fetchone()[0] or 0
            
            # 총 사용량
            cursor.execute('SELECT total_used_chars FROM elevenlabs_quota ORDER BY id DESC LIMIT 1')
            total_usage = cursor.fetchone()[0] or 0
            
            # 남은 한도
            quota_info = self.get_quota_info()
            remaining = quota_info['remaining_chars'] if quota_info else 0
            
            conn.close()
            
            return {
                'monthly_usage': monthly_usage,
                'total_usage': total_usage,
                'remaining': remaining,
                'monthly_limit': 10000
            }
        
        def display_quota_info(self):
            """한도 정보 표시"""
            quota_info = self.get_quota_info()
            stats = self.get_usage_statistics()
            
            if quota_info:
                ensure_printed("📊 ElevenLabs 무료 한도 정보", print_color='blue')
                ensure_printed(f" 이번 달 사용량: {stats['monthly_usage']:,}자", print_color='cyan')
                ensure_printed(f" 총 사용량: {stats['total_usage']:,}자", print_color='cyan')
                ensure_printed(f" 남은 한도: {stats['remaining']:,}자", print_color='green')
                ensure_printed(f" 월 무료 한도: {stats['monthly_limit']:,}자", print_color='yellow')
                
                # 사용률 계산
                usage_rate = (stats['monthly_usage'] / stats['monthly_limit']) * 100
                ensure_printed(f" 사용률: {usage_rate:.1f}%", print_color='blue')
                
                # 다음 초기화일 표시
                if quota_info['reset_date']:
                    reset_date = datetime.strptime(quota_info['reset_date'], '%Y-%m-%d').date()
                    ensure_printed(f" 다음 초기화일: {reset_date.strftime('%Y년 %m월 %d일')}", print_color='yellow')
            else:
                ensure_printed("❌ 한도 정보를 가져올 수 없습니다.", print_color='red')
    
    return ElevenLabsQuotaManager() 