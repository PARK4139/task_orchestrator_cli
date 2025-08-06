import os
import json
import requests
import datetime
from typing import Optional, Dict, Any
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.local_test_activate import LTA
from pkg_py.system_object.map_massages import PkMessages2025
from pkg_py.system_object.files import F_OPENAI_API_KEY
from pkg_py.system_object.directories import D_PK_WORKING
from pathlib import Path

def ensure_chat_gpt_responded(prompt, api_key=None, model="gpt-3.5-turbo", max_tokens=1000):
    """ChatGPT API를 사용하여 응답을 받는 함수"""
    try:
        # Lazy import to avoid circular dependency
        try:
            from pkg_py.functions_split.ensure_printed import ensure_printed
            from pkg_py.system_object.map_massages import PkMessages2025
        except ImportError:
            print = lambda msg, **kwargs: print(msg)
            PkMessages2025 = type('PkMessages2025', (), {
                'CHATGPT_RESPONSE_COMPLETE': 'ChatGPT 응답 완료',
                'CHATGPT_API_CALL_FAILED': 'API 호출 실패',
                'CHATGPT_RESPONSE_PARSE_FAILED': '응답 파싱 실패',
                'CHATGPT_UNEXPECTED_ERROR': '예상치 못한 오류',
                'CHATGPT_CONVERSATION_SAVE_FAILED': '대화 기록 저장 실패',
                'CHATGPT_CONVERSATION_LOAD_FAILED': '대화 기록 로드 실패'
            })()

        import requests
        import json
        from datetime import datetime
        
        # API 키 설정
        if api_key is None:
            try:
                with open(F_OPENAI_API_KEY, 'r') as f:
                    api_key = f.read().strip()
            except FileNotFoundError:
                ensure_printed("OpenAI API 키 파일을 찾을 수 없습니다.", print_color="red")
                return None
        
        # API 요청 데이터
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens
        }
        
        # API 호출
        try:
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()
            
            # 응답 파싱
            try:
                result = response.json()
                if "choices" in result and len(result["choices"]) > 0:
                    chat_response = result["choices"][0]["message"]["content"]
                    ensure_printed(f"[{PkMessages2025.CHATGPT_RESPONSE_COMPLETE}] 모델={model}", print_color="green")
                    
                    # 대화 기록 저장
                    try:
                        save_conversation(prompt, chat_response, model)
                    except Exception as e:
                        ensure_printed(f"[{PkMessages2025.CHATGPT_CONVERSATION_SAVE_FAILED}] 오류={e}", print_color="yellow")
                    
                    return chat_response
                else:
                    error_msg = f"[{PkMessages2025.CHATGPT_RESPONSE_PARSE_FAILED}] 응답형식오류"
                    ensure_printed(error_msg, print_color="red")
                    return None
                    
            except json.JSONDecodeError as e:
                error_msg = f"[{PkMessages2025.CHATGPT_RESPONSE_PARSE_FAILED}] 오류={e}"
                ensure_printed(error_msg, print_color="red")
                return None
                
        except requests.exceptions.RequestException as e:
            error_msg = f"[{PkMessages2025.CHATGPT_API_CALL_FAILED}] 오류={e}"
            ensure_printed(error_msg, print_color="red")
            return None
            
    except Exception as e:
        error_msg = f"[{PkMessages2025.CHATGPT_UNEXPECTED_ERROR}] 오류={e}"
        ensure_printed(error_msg, print_color="red")
        return None


def save_conversation(prompt, response, model):
    """대화 기록을 파일에 저장"""
    try:
        conversation_dir = Path(D_PK_WORKING) / "chatgpt_conversations"
        conversation_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.json"
        file_path = conversation_dir / filename
        
        conversation_data = {
            "timestamp": timestamp,
            "model": model,
            "prompt": prompt,
            "response": response
        }
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(conversation_data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        ensure_printed(f"[{PkMessages2025.CHATGPT_CONVERSATION_SAVE_FAILED}] 오류={e}", print_color="yellow")


def load_conversation_history(limit=10):
    """대화 기록을 로드"""
    try:
        conversation_dir = Path(D_PK_WORKING) / "chatgpt_conversations"
        if not conversation_dir.exists():
            return []
        
        conversations = []
        for file_path in sorted(conversation_dir.glob("conversation_*.json"), reverse=True):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    conversation = json.load(f)
                    conversations.append(conversation)
                    
                    if len(conversations) >= limit:
                        break
                        
            except Exception as e:
                ensure_printed(f"[{PkMessages2025.CHATGPT_CONVERSATION_LOAD_FAILED}] 파일={file_path} 오류={e}", print_color="yellow")
        
        return conversations
        
    except Exception as e:
        ensure_printed(f"[{PkMessages2025.CHATGPT_CONVERSATION_LOAD_FAILED}] 오류={e}", print_color="yellow")
        return []




