from fastapi import FastAPI, HTTPException
from app.models import ChatRequest
from app.chat import process_chat
import traceback

app = FastAPI(title="Snackbot API")

@app.post("/chat/")
async def chat_with_bot(chat_request: ChatRequest):
    try:
        result = process_chat(chat_request)
        return result
    except Exception as e:
        error_message = f"Internal Server Error: {e}\n{traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_message)