import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Mentor de Redação ENEM", page_icon="✍️")
st.title("✍️ Corretor de Redação Nota 1.000")

# Conectando com a API
genai.configure(api_key="SUA_CHAVE_API_AQUI")
model = genai.GenerativeModel('gemini-1.5-flash')

# Área de texto para o aluno
tema = st.text_input("Qual o tema da redação?")
texto_aluno = st.text_area("Cole sua redação aqui:", height=300)

if st.button("Corrigir Agora"):
    if texto_aluno:
        with st.spinner('Analisando competências...'):
            # Aqui entra a lógica do seu Gem
            prompt_completo = f"Instrução: [SUA INSTRUÇÃO DO GEM AQUI]. Tema: {tema}. Redação: {texto_aluno}"
            response = model.generate_content(prompt_completo)
            st.markdown("### 📝 Sua Avaliação:")
            st.write(response.text)
    else:
        st.warning("Por favor, cole seu texto antes de corrigir.")
