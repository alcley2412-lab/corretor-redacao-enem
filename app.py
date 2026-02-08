import streamlit as st
import google.generativeai as genai

# 1. Configuração da Página
st.set_page_config(page_title="Corretor ENEM", page_icon="✍️")
st.title("✍️ Mentor de Redação ENEM")

# 2. Configuração da API
# DICA: Verifique se não há espaços antes ou depois da chave
CHAVE_API = "SUA_CHAVE_AQUI" 

genai.configure(api_key=CHAVE_API)

# MUDANÇA AQUI: Testando o modelo sem o prefixo 'models/' 
# e usando o 1.5-flash que é o mais compatível atualmente
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro ao carregar o modelo: {e}")

# 3. Interface
texto_aluno = st.text_area("Cole sua redação aqui:", height=300)

if st.button("Analisar Redação"):
    if texto_aluno:
        with st.spinner('Analisando...'):
            try:
                # Prompt direto e simples para testar a conexão
                response = model.generate_content(
                    f"Atue como um corretor do ENEM. Corrija o texto: {texto_aluno}"
                )
                st.markdown("### Resultado:")
                st.write(response.text)
            except Exception as e:
                # Se o erro 404 persistir, vamos tentar o modelo 1.0 Pro
                st.error(f"Erro na análise: {e}")
                st.info("Tentando uma rota alternativa... Edite o código para 'gemini-1.0-pro' se o erro persistir.")
    else:
        st.warning("O campo de texto está vazio.")
