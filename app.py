import streamlit as st
import google.generativeai as genai

# Configuração da Página
st.set_page_config(page_title="Corretor ENEM", page_icon="✍️")
st.title("✍️ Mentor de Redação ENEM")

# CHAVE API - Use uma chave NOVA se possível
CHAVE_API = "SUA_CHAVE_AQUI" 

# Configuração da API
genai.configure(api_key=CHAVE_API)

# Interface
tema = st.text_input("Tema da Redação:")
texto_aluno = st.text_area("Cole sua redação aqui:", height=300)

if st.button("Analisar Redação"):
    if texto_aluno:
        with st.spinner('Analisando...'):
            try:
                # O segredo: Usar apenas 'gemini-1.5-flash' sem o prefixo 'models/'
                # Isso resolve o conflito da versão v1beta
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"Corrija esta redação para o tema '{tema}' seguindo os critérios do ENEM: {texto_aluno}"
                
                response = model.generate_content(prompt)
                st.markdown("### Resultado da Avaliação:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Erro na análise: {e}")
                st.info("Se o erro persistir, tente criar uma chave API em 'Create API key in new project' no Google AI Studio.")
    else:
        st.warning("Por favor, preencha o texto.")
