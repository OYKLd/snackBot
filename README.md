# snackBot
snackbot/
│
├── app/                             # Code de l'application principale
│   ├── __init__.py
│   ├── main.py                      # Point d'entrée API FastAPI
│   ├── chat.py                      # Logique de gestion de la conversation avec OpenAI
│   ├── order_parser.py              # Extraction des données de commande
│   └── models.py                    # Modèles Pydantic
│
├── frontend/                        # Interface utilisateur Streamlit
│   ├── app.py                       # Interface Streamlit
│
├── requirements.txt                # Dépendances Python
└── README.md   