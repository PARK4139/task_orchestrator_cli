def ensure_text_decoded():
    """
    보안 강화 텍스트 복호화 함수
    1. 사용자 입력으로 text와 마스터 패스워드를 받음
    2. 마스터 패스워드로 메타데이터 복호화
    3. 다단계 복호화 수행 (Base64 + AES + XOR + Caesar Cipher)
    4. print decoded text
    5. 클립보드에 복사
    6. return decoded text
    """
    from pkg_py.functions_split.ensure_printed import ensure_printed
    from base64 import b64decode
    from Cryptodome.Cipher import AES
    import hashlib
    import pyperclip
    import json
    import os
    
    # 1. 사용자 입력으로 text와 마스터 패스워드를 받음
    ensure_printed(" 복호화할 텍스트를 입력하세요:", print_color='blue')
    text = input("텍스트 입력: ").strip()
    
    if not text:
        ensure_printed("❌ 텍스트가 입력되지 않았습니다.", print_color='red')
        return None
    
    ensure_printed(" 마스터 패스워드를 입력하세요:", print_color='blue')
    master_password = input("마스터 패스워드(5th sym pw): ").strip()
    
    if not master_password:
        ensure_printed("❌ 마스터 패스워드가 입력되지 않았습니다.", print_color='red')
        return None
    
    # 2. 다단계 복호화 수행
    try:
        # 키 파생 함수
        def derive_key_from_password(password, salt):
            return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        
        # 메타데이터 복호화 함수
        def decrypt_metadata(encrypted_metadata, password):
            try:
                # Salt 추출 (처음 16바이트)
                salt = encrypted_metadata[:16]
                encrypted_data = encrypted_metadata[16:]
                
                key = derive_key_from_password(password, salt)
                cipher = AES.new(key, AES.MODE_ECB)
                
                decrypted = cipher.decrypt(encrypted_data)
                # null 패딩 제거
                metadata_json = decrypted.rstrip(b'\0').decode('utf-8')
                return json.loads(metadata_json)
            except Exception as e:
                ensure_printed(f"❌ 메타데이터 복호화 실패: {str(e)}", print_color='red')
                return None
        
        # 보안 형식 확인
        if not text.startswith("SECURE_"):
            ensure_printed("❌ 보안 암호화 형식이 아닙니다.", print_color='red')
            return None
        
        # 데이터 분리
        parts = text.split("_", 2)
        if len(parts) != 3:
            ensure_printed("❌ 잘못된 암호화 형식입니다.", print_color='red')
            return None
        
        encrypted_metadata_b64 = parts[1]
        encrypted_data = parts[2]
        
        # 메타데이터 복호화
        encrypted_metadata = b64decode(encrypted_metadata_b64)
        metadata = decrypt_metadata(encrypted_metadata, master_password)
        
        if metadata is None:
            ensure_printed("❌ 마스터 패스워드가 잘못되었습니다.", print_color='red')
            return None
        
        caesar_shift = metadata['caesar_shift']
        xor_key = metadata['xor_key']
        aes_key = metadata['aes_key']
        
        ensure_printed(f" 메타데이터 복호화 성공: Caesar={caesar_shift}, XOR={xor_key}, AES={aes_key}", print_color='cyan')
        
        # 단계 1: Base64 디코딩
        def base64_decode(text):
            return b64decode(text)
        
        # 단계 2: AES 복호화
        def aes_decrypt(encrypted_data, key):
            key_hash = hashlib.sha256(key.encode()).digest()
            cipher = AES.new(key_hash, AES.MODE_ECB)
            decrypted = cipher.decrypt(encrypted_data)
            # null 패딩 제거
            return decrypted.rstrip(b'\0').decode('utf-8')
        
        # 단계 3: XOR 복호화
        def xor_decrypt(text, key):
            key_bytes = key.encode('utf-8')
            result = ""
            for i, char in enumerate(text):
                result += chr(ord(char) ^ key_bytes[i % len(key_bytes)])
            return result
        
        # 단계 4: Caesar Cipher 복호화
        def caesar_decrypt(text, shift):
            result = ""
            for char in text:
                if char.isalpha():
                    ascii_offset = ord('A') if char.isupper() else ord('a')
                    result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
                else:
                    result += char
            return result
        
        # 복호화 과정
        ensure_printed("🔄 복호화 진행 중...", print_color='yellow')
        
        # 1단계: Base64 디코딩
        step1 = base64_decode(encrypted_data)
        ensure_printed(f"📝 1단계 (Base64 디코딩): {len(step1)} bytes", print_color='cyan')
        
        # 2단계: AES 복호화
        step2 = aes_decrypt(step1, aes_key)
        ensure_printed(f"🔑 2단계 (AES 복호화): {step2}", print_color='cyan')
        
        # 3단계: XOR 복호화
        step3 = xor_decrypt(step2, xor_key)
        ensure_printed(f"🔒 3단계 (XOR 복호화): {step3}", print_color='cyan')
        
        # 4단계: Caesar Cipher 복호화
        final_decoded = caesar_decrypt(step3, caesar_shift)
        
        # 3. print decoded text
        ensure_printed(f"✅ 최종 복호화 완료!", print_color='green')
        ensure_printed(f"🔓 복호화된 텍스트: {final_decoded}", print_color='green')
        
        # 4. 클립보드에 복사
        try:
            pyperclip.copy(final_decoded)
            ensure_printed("📋 클립보드에 복사되었습니다! (Ctrl+V로 붙여넣기 가능)", print_color='green')
        except Exception as e:
            ensure_printed(f"⚠️ 클립보드 복사 실패: {str(e)}", print_color='yellow')
        
        # 5. return decoded text
        return final_decoded
        
    except Exception as e:
        ensure_printed(f"❌ 복호화 중 오류 발생: {str(e)}", print_color='red')
        return None 