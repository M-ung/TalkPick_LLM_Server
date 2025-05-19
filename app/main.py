from fastapi import FastAPI
from .controller.topic_controller import router as topic_router

app = FastAPI(title="TalkPick LLM Server")

app.include_router(topic_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 