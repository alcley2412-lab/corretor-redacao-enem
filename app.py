import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Corretor ENEM", page_icon="✍️")
st.title("✍️ Mentor de Redação ENEM")

# Chave API - Substitua apenas o que está entre aspas
CHAVE_API = "AIzaSyDEz_e9-R7usMGg9UTLvVp6dXCJhF_mmlA" 

# Configuração robusta
try:
    genai.configure(api_key=CHAVE_API)
    # Usamos 'gemini-1.5-flash' sem nenhum prefixo. 
    # Se falhar, o código tentará o 'gemini-pro'.
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro de configuração: {e}")

texto_aluno = st.text_area("Cole sua redação aqui:", height=300)

if st.button("Analisar Redação"):
    if texto_aluno:
        with st.spinner('Analisando...'):
            try:
                # Tentativa 1: Flash
                response = model.generate_content(f"Corrija para o ENEM: {texto_aluno}")
                st.markdown(response.text)
            except Exception:
                try:
                    # Tentativa 2: Rota de emergência com modelo Pro
                    model_alt = genai.GenerativeModel('gemini-pro')
                    response = model_alt.generate_content(f"Corrija para o ENEM: {texto_aluno}")
                    st.markdown(response.text)
                except Exception as e2:
                    st.error(f"Erro persistente: {e2}")
                    st.info("Dica: Vá ao Google AI Studio e crie uma NOVA chave API em um 'New Project'.")
    else:
        st.warning("O campo está vazio.")
