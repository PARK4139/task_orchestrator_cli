
## ElevenLabs 무료 한도 관리 시스템 완성!

### 주요 기능:

1. **SQLite 데이터베이스 관리**:
   - 남은 무료 한도 저장
   - 사용 기록 로그
   - 월별 통계

2. **자동 한도 초기화**:
   - 매월 1일 자동 초기화
   - 10,000자 무료 한도

3. **사용량 제한**:
   - 한도 초과 시 TTS 사용 차단
   - 실시간 한도 확인

4. **상세한 통계**:
   - 이번 달 사용량
   - 총 사용량
   - 사용률 표시

### 데이터베이스 구조:

```sql
-- 무료 한도 테이블
CREATE TABLE elevenlabs_quota (
    id INTEGER PRIMARY KEY,
    remaining_chars INTEGER DEFAULT 10000,
    last_reset_date TEXT,
    total_used_chars INTEGER DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);

-- 사용 기록 테이블
CREATE TABLE elevenlabs_usage_log (
    id INTEGER PRIMARY KEY,
    text_length INTEGER,
    voice_id TEXT,
    used_at TIMESTAMP
);
```

### 사용 방법:

```bash
# 한도 관리 테스트
python pkg_py/functions_split/test_elevenlabs_quota.py

# TTS 사용 (자동으로 한도 관리됨)
python pkg_py/pk_ensure_text_encoded.py
```

### 기억할 사항:

- ✅ **매월 1일 자동 초기화**: 무료 한도가 10,000자로 초기화됨
- ✅ **실시간 한도 확인**: TTS 사용 전 한도 확인
- ✅ **사용량 로그**: 모든 TTS 사용 기록 저장
- ✅ **한도 초과 차단**: 무료 한도 초과 시 사용 불가

이제 ElevenLabs API의 무료 한도를 안전하게 관리할 수 있습니다! 🛡️

def test_elevenlabs_quota():
    """
    ElevenLabs 무료 한도 관리 테스트
    """
    from pkg_py.functions_split.ensure_elevenlabs_quota_manager import ensure_elevenlabs_quota_manager
    from pkg_py.functions_split.ensure_printed import ensure_printed
    
    def test_quota_management():
        """한도 관리 테스트"""
        ensure_printed("🧪 ElevenLabs 무료 한도 관리 테스트", print_color='blue')
        
        quota_manager = ensure_elevenlabs_quota_manager()
        
        # 현재 한도 정보 표시
        quota_manager.display_quota_info()
        
        # 초기화 확인
        reset_result = quota_manager.check_and_reset_quota()
        if reset_result:
            ensure_printed("🔄 한도가 초기화되었습니다.", print_color='green')
        
        # 테스트 텍스트들
        test_texts = [
            "안녕하세요.",
            "이것은 테스트입니다.",
            "한도 관리 시스템이 작동하고 있습니다."
        ]
        
        for text in test_texts:
            text_length = len(text)
            ensure_printed(f"\n 테스트 텍스트: {text} ({text_length}자)", print_color='cyan')
            
            if quota_manager.can_use_tts(text_length):
                quota_manager.update_usage(text_length, "test_voice")
                ensure_printed("✅ 사용량 업데이트 완료", print_color='green')
            else:
                ensure_printed("❌ 한도 초과로 사용 불가", print_color='red')
                break
        
        # 최종 한도 정보 표시
        ensure_printed("\n📊 최종 한도 정보:", print_color='blue')
        quota_manager.display_quota_info()
    
    def reset_quota_for_testing():
        """테스트용 한도 초기화"""
        from pkg_py.functions_split.ensure_elevenlabs_quota_manager import ensure_elevenlabs_quota_manager
        import sqlite3
        import os
        
        quota_manager = ensure_elevenlabs_quota_manager()
        
        ensure_printed("🔄 테스트용 한도 초기화", print_color='yellow')
        
        db_path = os.path.join(os.path.expanduser("~"), ".pk_system", "elevenlabs_quota.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # 한도 초기화
        cursor.execute('''
            UPDATE elevenlabs_quota 
            SET remaining_chars = 10000, 
                total_used_chars = 0,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = (SELECT MAX(id) FROM elevenlabs_quota)
        ''')
        
        conn.commit()
        conn.close()
        
        ensure_printed("✅ 테스트용 한도 초기화 완료!", print_color='green')
        quota_manager.display_quota_info()
    
    # 메인 실행
    ensure_printed(" ElevenLabs 무료 한도 관리 테스트", print_color='blue')
    ensure_printed("1. 한도 관리 테스트", print_color='cyan')
    ensure_printed("2. 테스트용 한도 초기화", print_color='cyan')
    
    choice = input("테스트를 선택하세요 (1-2): ").strip()
    
    if choice == "1":
        test_quota_management()
    elif choice == "2":
        reset_quota_for_testing()
    else:
        ensure_printed("❌ 잘못된 선택입니다.", print_color='red') 