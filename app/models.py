from pydantic import BaseModel
from typing import List, Dict

class Message(BaseModel):
    role: str  # "user" ou "assistant"
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class Order(BaseModel):
    items: List[Dict[str, str]]
    total_price: float
    confirmation_required: bool = True