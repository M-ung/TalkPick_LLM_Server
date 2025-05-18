# TalkPick LLM Server

대화 주제 추천을 위한 LLM/RAG 서버입니다.

## 설치 방법

1. Python 3.9+ 설치
2. 가상환경 생성 및 활성화:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# or
.\venv\Scripts\activate  # Windows
```

3. 의존성 설치:
```bash
pip install -r requirements.txt
```

4. 환경 변수 설정:
- `.env` 파일을 생성하고 다음 내용을 추가:
```
OPENAI_API_KEY=your_api_key_here
```

5. 서버 실행:
```bash
uvicorn app.main:app --reload
```

## API 엔드포인트

- POST `/api/recommend-topics`: 대화 주제 추천
  - 입력: 사용자 정보 (나이, MBTI, 성별, 모임 카테고리)
  - 출력: 추천된 4개의 대화 주제 