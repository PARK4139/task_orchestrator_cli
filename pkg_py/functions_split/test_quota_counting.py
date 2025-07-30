
## ✅ 한도 카운트 확인 완료!

### 한도 카운트 로직:

1. **사용 전 확인**: `can_use_tts(text_length)` - 남은 한도 >= 사용할 문자 수
2. **사용량 업데이트**: `update_usage(text_length, voice_id)` - 실제 사용 후 한도 감소
3. **통계 추적**: 월별 사용량, 총 사용량, 남은 한도 추적
4. **자동 초기화**: 매월 1일 자동으로 10,000자로 초기화

### 카운트되는 항목:

- ✅ **텍스트 길이**: 실제 변환할 텍스트의 문자 수
- ✅ **사용 기록**: 언제, 어떤 음성으로, 몇 자 사용했는지
- ✅ **월별 통계**: 이번 달 총 사용량
- ✅ **총 사용량**: 전체 기간 사용량

### 테스트 방법:

```bash
# 한도 카운트 테스트
python pkg_py/functions_split/test_quota_counting.py
```

이제 실제로 한도가 제대로 카운트되고 있는지 확인할 수 있습니다! 📊

def test_quota_counting():
    """
    한도 카운트 테스트
    """
    from pkg_py.functions_split.ensure_elevenlabs_quota_managed import ensure_elevenlabs_quota_managed
    from pkg_py.functions_split.ensure_printed import ensure_printed
    
    def test_quota_counting_logic():
        """한도 카운트 로직 테스트"""
        ensure_printed("🧪 ElevenLabs 한도 카운트 테스트", print_color='blue')
        
        quota_manager = ensure_elevenlabs_quota_managed()
        
        # 초기 상태 확인
        ensure_printed("\n📊 초기 상태:", print_color='yellow')
        quota_manager.display_quota_info()
        
        # 테스트 텍스트들
        test_texts = [
            "안녕하세요.",
            "이것은 테스트입니다.",
            "한도 카운트가 제대로 작동하는지 확인합니다."
        ]
        
        total_used = 0
        
        for i, text in enumerate(test_texts, 1):
            text_length = len(text)
            total_used += text_length
            
            ensure_printed(f"\n 테스트 {i}: {text} ({text_length}자)", print_color='cyan')
            
            # 사용 가능 여부 확인
            if quota_manager.can_use_tts(text_length):
                # 사용량 업데이트 (실제 TTS 없이)
                quota_manager.update_usage(text_length, "test_voice")
                ensure_printed(f"✅ 사용량 업데이트 완료: {text_length}자 사용됨", print_color='green')
                
                # 업데이트된 상태 확인
                quota_info = quota_manager.get_quota_info()
                if quota_info:
                    remaining = quota_info['remaining_chars']
                    ensure_printed(f" 남은 한도: {remaining}자", print_color='blue')
            else:
                ensure_printed("❌ 한도 초과로 사용 불가", print_color='red')
                break
        
        # 최종 상태 확인
        ensure_printed(f"\n📊 최종 상태 (총 사용: {total_used}자):", print_color='yellow')
        quota_manager.display_quota_info()
        
        # 통계 확인
        stats = quota_manager.get_usage_statistics()
        ensure_printed(f"\n📈 통계 정보:", print_color='blue')
        ensure_printed(f" 이번 달 사용량: {stats['monthly_usage']:,}자", print_color='cyan')
        ensure_printed(f" 총 사용량: {stats['total_used_chars']:,}자", print_color='cyan')
        ensure_printed(f" 남은 한도: {stats['remaining']:,}자", print_color='green')
    
    def test_quota_reset():
        """한도 초기화 테스트"""
        from pkg_py.functions_split.ensure_elevenlabs_quota_managed import ensure_elevenlabs_quota_managed
        import sqlite3
        import os
        
        quota_manager = ensure_elevenlabs_quota_managed()
        
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
    
    def check_database_structure():
        """데이터베이스 구조 확인"""
        import sqlite3
        import os
        
        db_path = os.path.join(os.path.expanduser("~"), ".pk_system", "elevenlabs_quota.db")
        
        if not os.path.exists(db_path):
            ensure_printed("❌ 데이터베이스 파일이 없습니다.", print_color='red')
            return
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # 테이블 구조 확인
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        ensure_printed("📋 데이터베이스 테이블:", print_color='blue')
        for table in tables:
            ensure_printed(f" - {table[0]}", print_color='cyan')
        
        # elevenlabs_quota 테이블 데이터 확인
        cursor.execute("SELECT * FROM elevenlabs_quota ORDER BY id DESC LIMIT 1")
        quota_data = cursor.fetchone()
        
        if quota_data:
            ensure_printed(f"\n📊 한도 데이터:", print_color='blue')
            ensure_printed(f" ID: {quota_data[0]}", print_color='cyan')
            ensure_printed(f" 남은 문자: {quota_data[1]}", print_color='cyan')
            ensure_printed(f" 마지막 초기화일: {quota_data[2]}", print_color='cyan')
            ensure_printed(f" 총 사용 문자: {quota_data[3]}", print_color='cyan')
        
        # 사용 로그 확인
        cursor.execute("SELECT COUNT(*) FROM elevenlabs_usage_log")
        log_count = cursor.fetchone()[0]
        ensure_printed(f"\n📝 사용 로그 개수: {log_count}개", print_color='blue')
        
        conn.close()
    
    # 메인 실행
    ensure_printed(" ElevenLabs 한도 카운트 테스트", print_color='blue')
    ensure_printed("1. 한도 카운트 로직 테스트", print_color='cyan')
    ensure_printed("2. 테스트용 한도 초기화", print_color='cyan')
    ensure_printed("3. 데이터베이스 구조 확인", print_color='cyan')
    
    choice = input("테스트를 선택하세요 (1-3): ").strip()
    
    if choice == "1":
        test_quota_counting_logic()
    elif choice == "2":
        test_quota_reset()
    elif choice == "3":
        check_database_structure()
    else:
        ensure_printed("❌ 잘못된 선택입니다.", print_color='red') 