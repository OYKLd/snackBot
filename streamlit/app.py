import streamlit as st
import requests
import uuid

API_URL = "http://localhost:8000/chat/"

st.set_page_config(page_title="SnackBot 🍔", layout="centered")
st.title("SnackBot 🍔")

# Initialise la session si nécessaire
if "conversations" not in st.session_state:
    st.session_state.conversations = {}

if "current_conv_id" not in st.session_state:
    new_id = str(uuid.uuid4())
    st.session_state.conversations[new_id] = []
    st.session_state.current_conv_id = new_id

# Fonctions utiles
def start_new_conversation():
    new_id = str(uuid.uuid4())
    st.session_state.conversations[new_id] = []
    st.session_state.current_conv_id = new_id

def select_conversation(conv_id):
    st.session_state.current_conv_id = conv_id

# Barre latérale
st.sidebar.header("📚 Conversations")
for conv_id in st.session_state.conversations:
    button_label = f"Conversation {conv_id[:6]}"
    if st.sidebar.button(button_label, key=conv_id):
        select_conversation(conv_id)

if st.sidebar.button("🆕 Nouvelle conversation"):
    start_new_conversation()

# Zone d'entrée utilisateur
user_input = st.chat_input("Que souhaitez-vous commander ?")

# Affichage des messages de la conversation sélectionnée
messages = st.session_state.conversations[st.session_state.current_conv_id]
for msg in messages:
    st.chat_message(msg["role"]).write(msg["content"])

if user_input:
    messages.append({"role": "user", "content": user_input})
    try:
        response = requests.post(API_URL, json={"messages": messages})
        response.raise_for_status()
        result = response.json()

        messages.append({"role": "assistant", "content": result["response"]})
        st.chat_message("assistant").write(result["response"])

        if result.get("order"):
            st.success("Commande détectée ✅")
            st.json(result["order"])

    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de requête : {e}")
    except ValueError as e:
        st.error(f"Erreur de décodage JSON : {e}")
    except Exception as e:
        st.error(f"Une erreur inattendue s'est produite : {e}")