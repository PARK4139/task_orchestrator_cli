import os
import json
import requests
import datetime
from typing import Optional, Dict, Any
from pkg_py.functions_split.ensure_printed import ensure_printed
from pkg_py.system_object.local_test_activate import LTA

def ensure_chat_gpt_responded(
    question: str,
    api_key: Optional[str] = None,
    model: str = "gpt-4o-mini",
    max_tokens: int = 1000,
    temperature: float = 0.7,
    system_prompt: Optional[str] = None,
    save_conversation: bool = True,
    conversation_file: str = "chatgpt_conversation.json"
) -> str:
    """
    ChatGPT API를 사용하여 질문에 답변하는 함수
    
    Args:
        question: ChatGPT에게 물어볼 질문
        api_key: OpenAI API 키 (None이면 환경변수에서 가져옴)
        model: 사용할 모델 (gpt-4o-mini, gpt-4o, gpt-3.5-turbo 등)
        max_tokens: 최대 토큰 수
        temperature: 창의성 정도 (0.0 ~ 1.0)
        system_prompt: 시스템 프롬프트 (None이면 기본값 사용)
        save_conversation: 대화 기록 저장 여부
        conversation_file: 대화 기록 파일명
    
    Returns:
        str: ChatGPT의 답변
    """
    
    # API 키 설정
    if api_key is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API 키가 설정되지 않았습니다. 환경변수 OPENAI_API_KEY를 설정하거나 api_key 매개변수를 제공하세요.")
    
    # 기본 시스템 프롬프트
    if system_prompt is None:
        system_prompt = """당신은 도움이 되는 AI 어시스턴트입니다. 
사용자의 질문에 정확하고 유용한 답변을 제공하세요.
한국어로 답변해주세요."""
    
    # API 요청 데이터 준비
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        "max_tokens": max_tokens,
        "temperature": temperature
    }
    
    try:
        ensure_printed(f"🤖 ChatGPT API 호출 중... (모델: {model})", print_color="cyan")
        
        # API 호출
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        
        response.raise_for_status()
        result = response.json()
        
        # 답변 추출
        answer = result["choices"][0]["message"]["content"]
        
        ensure_printed(f"✅ ChatGPT 응답 완료", print_color="green")
        ensure_printed(f"📝 답변: {answer}", print_color="blue")
        
        # 대화 기록 저장
        if save_conversation:
            save_chat_conversation(question, answer, conversation_file)
        
        return answer
        
    except requests.exceptions.RequestException as e:
        error_msg = f"❌ API 호출 실패: {e}"
        ensure_printed(error_msg, print_color="red")
        raise Exception(error_msg)
    
    except KeyError as e:
        error_msg = f"❌ 응답 파싱 실패: {e}"
        ensure_printed(error_msg, print_color="red")
        raise Exception(error_msg)
    
    except Exception as e:
        error_msg = f"❌ 예상치 못한 오류: {e}"
        ensure_printed(error_msg, print_color="red")
        raise Exception(error_msg)

def save_chat_conversation(question: str, answer: str, filename: str) -> None:
    """대화 기록을 JSON 파일로 저장"""
    try:
        conversation = {
            "timestamp": str(datetime.datetime.now()),
            "question": question,
            "answer": answer
        }
        
        # 기존 대화 기록 로드
        conversations = []
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    conversations = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                conversations = []
        
        # 새 대화 추가
        conversations.append(conversation)
        
        # 파일 저장
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(conversations, f, ensure_ascii=False, indent=2)
        
        ensure_printed(f"💾 대화 기록 저장됨: {filename}", print_color="yellow")
        
    except Exception as e:
        ensure_printed(f"⚠️ 대화 기록 저장 실패: {e}", print_color="yellow")

def load_chat_conversations(filename: str = "chatgpt_conversation.json") -> list:
    """저장된 대화 기록 로드"""
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except Exception as e:
        ensure_printed(f"⚠️ 대화 기록 로드 실패: {e}", print_color="yellow")
        return []

def print_chat_history(filename: str = "chatgpt_conversation.json", limit: int = 5) -> None:
    """최근 대화 기록 출력"""
    conversations = load_chat_conversations(filename)
    
    if not conversations:
        ensure_printed("📚 저장된 대화 기록이 없습니다.", print_color="yellow")
        return
    
    ensure_printed(f"📚 최근 대화 기록 ({min(limit, len(conversations))}개):", print_color="cyan")
    
    for i, conv in enumerate(conversations[-limit:], 1):
        ensure_printed(f"\n--- 대화 {i} ---", print_color="green")
        ensure_printed(f"⏰ 시간: {conv.get('timestamp', 'N/A')}", print_color="yellow")
        ensure_printed(f"❓ 질문: {conv.get('question', 'N/A')}", print_color="blue")
        ensure_printed(f"🤖 답변: {conv.get('answer', 'N/A')}", print_color="green")




