from fastapi import FastAPI
from .controller.topic_controller import router as topic_router
from .config.database import engine, Base

app = FastAPI(title="TalkPick LLM Server")

Base.metadata.create_all(bind=engine)
app.include_router(topic_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 