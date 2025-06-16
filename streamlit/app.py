import streamlit as st
import requests

API_URL = "http://localhost:8000/chat/"

st.title("SnackBot 🍔")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Que souhaitez-vous commander ?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    try:
        response = requests.post(API_URL, json={"messages": st.session_state.messages})
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        result = response.json()

        st.session_state.messages.append({"role": "assistant", "content": result["response"]})

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if result["order"]:
            st.success("Commande détectée ✅")
            st.json(result["order"])

    except requests.exceptions.RequestException as e:
        st.error(f"Erreur de requête : {e}")
    except ValueError as e:
        st.error(f"Erreur de décodage JSON : {e}")
    except Exception as e:
        st.error(f"Une erreur inattendue s'est produite : {e}")