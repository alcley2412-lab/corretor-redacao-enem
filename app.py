import streamlit as st
import google.generativeai as genai

# 1. Configuração da Página
st.set_page_config(page_title="Corretor ENEM Nota 1000", page_icon="📝")

st.title("📝 Corretor de Redação ENEM")
st.markdown("Cole seu texto abaixo para receber uma análise baseada nas 5 competências.")

# 2. Configuração da API (COLOQUE SUA CHAVE AQUI)
CHAVE_API = "AIzaSyDXZMPnBHlQ36-LQSUEusuuW1VM7cAn_KA" 

try:
    genai.configure(api_key=CHAVE_API)
    # Usando o nome completo do modelo para evitar erros
    model = genai.GenerativeModel('models/gemini-1.5-flash')
except Exception as e:
    st.error(f"Erro na configuração da API: {e}")

# 3. Interface do Usuário
tema = st.text_input("Tema da Redação:", placeholder="Ex: O impacto das redes sociais...")
texto_aluno = st.text_area("Sua Redação:", height=300, placeholder="Comece a escrever aqui...")

# 4. Lógica do Botão
if st.button("Analisar Redação"):
    if not texto_aluno.strip():
        st.warning("Por favor, cole o conteúdo da sua redação antes de prosseguir.")
    else:
        with st.spinner('Analisando... Isso pode levar alguns segundos.'):
            try:
                # Criando o prompt que o seu GEM faria
                prompt_sistema = (
                    "Você é um corretor oficial do ENEM. Analise a redação abaixo. "
                    "Dê uma nota de 0 a 200 para cada uma das 5 competências e uma nota final. "
                    "Seja detalhista e sugira melhorias para chegar à nota 1000."
                )
                
                # Chamada da API
                response = model.generate_content(f"{prompt_sistema}\n\nTema: {tema}\n\nTexto: {texto_aluno}")
                
                # Exibindo o resultado
                st.subheader("📊 Resultado da Avaliação")
                st.markdown(response.text)
                
            except Exception as e:
                st.error("Ocorreu um erro ao processar a redação. Verifique se sua chave API está correta e ativa.")
                st.info(f"Detalhe técnico do erro: {e}")

st.divider()
st.caption("Desenvolvido para auxílio de estudantes do ENEM.")
     
