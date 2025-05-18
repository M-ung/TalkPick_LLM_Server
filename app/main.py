from fastapi import FastAPI
from .controller.topic_controller import router as topic_router
from .config.database import engine, Base

app = FastAPI(title="TalkPick LLM Server")

# 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(topic_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 