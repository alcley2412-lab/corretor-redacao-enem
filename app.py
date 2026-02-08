import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Corretor ENEM", page_icon="✍️")
st.title("✍️ Mentor de Redação ENEM")

# Coloque sua CHAVE API aqui
CHAVE_API = "AIzaSyDEz_e9-R7usMGg9UTLvVp6dXCJhF_mmlA"

genai.configure(api_key=CHAVE_API)

def buscar_modelo():
    """Busca o primeiro modelo disponível que suporta geração de conteúdo"""
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                # Retorna o nome do modelo (ex: models/gemini-1.5-flash)
                return m.name
    except Exception as e:
        st.error(f"Erro ao acessar a API: {e}")
    return None

nome_do_modelo = buscar_modelo()

if nome_do_modelo:
    st.success(f"Conectado com sucesso ao modelo: {nome_do_modelo}")
    
    texto_aluno = st.text_area("Cole sua redação aqui:", height=300)
    
    if st.button("Analisar Redação"):
        if texto_aluno:
            with st.spinner('Analisando...'):
                try:
                    model = genai.GenerativeModel(nome_do_modelo)
                    response = model.generate_content(f"Corrija para o ENEM: {texto_aluno}")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Erro na análise: {e}")
        else:
            st.warning("O campo está vazio.")
else:
    st.error("Nenhum modelo disponível encontrado. Verifique se sua chave API é nova e foi criada em 'Create API key in NEW project'.")
