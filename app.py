import streamlit as st
import google.generativeai as genai

# Título do site
st.set_page_config(page_title="Corretor ENEM")
st.title("✍️ Corretor de Redação")

# Configuração da Chave (Substitua pela sua chave entre as aspas)
genai.configure(api_key="SUA_CHAVE_AQUI")

# Interface
texto_aluno = st.text_area("Cole sua redação aqui:")

if st.button("Analisar"):
    if texto_aluno:
        model = genai.GenerativeModel('gemini-1.5-flash')
        # Prompt simplificado para teste
        response = model.generate_content(f"Corrija esta redação para o ENEM: {texto_aluno}")
        st.write(response.text)
    else:
        st.error("Escreva algo antes!")
