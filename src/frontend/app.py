import streamlit as st
import requests
import json
from datetime import datetime

st.set_page_config(page_title="Chatbot Ley 7/2022", layout="wide")

# Title and description
st.title("💬 Chatbot Ley 7/2022")
st.subheader("Residuos y Suelos Contaminados para una Economía Circular")

# Sidebar configuration
st.sidebar.header("⚙️ Configuración")
api_url = st.sidebar.text_input("API URL", value="http://localhost:8000")
st.sidebar.markdown("---")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "session_id" not in st.session_state:
    st.session_state.session_id = str(datetime.now().timestamp())

# Suggested questions
st.sidebar.header("❓ Preguntas Sugeridas")
suggested_questions = [
    "¿Qué obligaciones tiene un productor de residuos?",
    "¿Qué es la Responsabilidad Ampliada del Productor (RAP)?",
    "¿Cuáles son las sanciones por incumplimiento?",
    "¿Qué es un suelo contaminado?",
    "¿Cuáles son los objetivos de reciclaje?"
]

if st.sidebar.button("🗑️ Limpiar Historial"):
    st.session_state.messages = []
    st.rerun()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if "sources" in message and message["sources"]:
            st.markdown("**Fuentes:**")
            for source in message["sources"]:
                st.markdown(f"- {source}")

# Chat input
user_input = st.chat_input("Escribe tu pregunta sobre la Ley 7/2022...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Send to API
    try:
        response = requests.post(
            f"{api_url}/api/v1/chat/message",
            json={"message": user_input, "session_id": st.session_state.session_id},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            bot_response = data.get("response", "No se pudo obtener respuesta")
            sources = data.get("sources", [])
            
            # Add bot response to history
            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_response,
                "sources": sources
            })
            
            # Display bot response
            with st.chat_message("assistant"):
                st.markdown(bot_response)
                if sources:
                    st.markdown("**Fuentes:**")
                    for source in sources:
                        st.markdown(f"- {source}")
        else:
            st.error("Error al conectar con la API")
    except requests.exceptions.RequestException as e:
        st.error(f"Error de conexión: {str(e)}")