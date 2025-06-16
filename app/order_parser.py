import re
from typing import List, Dict

def extract_order_from_text(text: str) -> Dict:
    """
    Extraire une commande depuis le texte final de la conversation.
    Ceci est un exemple simplifié — à adapter selon les réponses du LLM.
    """
    items = re.findall(r"(\d+)x (\w+)", text)
    parsed_items = [{"item": item, "quantity": qty} for qty, item in items]
    return {
        "items": parsed_items,
        "total_price": len(parsed_items) * 5.0,
        "confirmation_required": True
    }