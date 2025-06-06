import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()

# python run.py 실행 방법
if __name__ == "__main__":
    uvicorn.run("app.main:app", 
                host=os.getenv("HOST", "0.0.0.0"),
                port=int(os.getenv("PORT", "8000")),
                reload=True) 