import openai
from app.order_parser import extract_order_from_text
from app.models import ChatRequest, Message
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(messages: list) -> str:
    """Appelle l'API OpenAI pour obtenir une réponse."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[msg.dict() for msg in messages],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

def process_chat(chat_data: ChatRequest):
    """Gère le chat et extrait une commande s'il y en a une."""

    system_message = Message(
        role="system",
        content="Tu es un assistant de commande de nourriture dans un fastfood. Ton rôle est de prendre les commandes des clients. Réponds de manière concise et amicale, tu doit faire la conversation avec le client poser des questions jusqu'à obtenir tout les details de la commande et retourne après avoir pris la commande de l'utilisateur un json structuré et demande validation. Si le client valide sa commande, confirme que la commande est enregistree."

    )

    messages_with_system = [system_message] + chat_data.messages
    reply = get_openai_response(messages_with_system)

    if "je valide" in reply.lower() or "c'est bon" in reply.lower():
        order = extract_order_from_text(reply)
        return {"response": reply, "order": order}
    return {"response": reply, "order": None}