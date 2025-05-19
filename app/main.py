from fastapi import FastAPI
from .controller.topic_controller import router as topic_router
from .common.exception.exception_handler import init_exception_handlers

app = FastAPI(title="TalkPick LLM Server")

init_exception_handlers(app)

app.include_router(topic_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 