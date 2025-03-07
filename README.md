# Chatbot com LangChain + FAISS + Hugging Face

Este repositório contém um chatbot baseado em **LangChain**, **FAISS** e **Hugging Face**, capaz de responder perguntas baseadas em um conjunto de documentos fornecidos.

## 🚀 Funcionalidades
- Carregamento de documentos locais.
- Indexação de conhecimento com **FAISS**.
- Utilização de **modelos de linguagem da Hugging Face** para responder perguntas.
- Interface simples via **Streamlit**.

## 🛠️ Requisitos
- Python 3.8+
- Conta na [Hugging Face](https://huggingface.co/)
- Token de acesso da Hugging Face com permissão de inferência

## 📦 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/chatbot-langchain-faiss.git
   cd chatbot-langchain-faiss
   ```
2. **Crie um ambiente virtual e ative:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## 🔑 Configuração da Hugging Face
1. **Obtenha seu token na Hugging Face:**
   - Acesse: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   - Gere um token com permissão de leitura e inferência.
2. **Defina o token no ambiente:**
   ```bash
   export HUGGINGFACEHUB_API_TOKEN='SEU_TOKEN_AQUI'  # No Windows: set HUGGINGFACEHUB_API_TOKEN=SEU_TOKEN_AQUI
   ```

## ⚡ Como rodar
1. **Adicione o conhecimento ao arquivo `base_de_conhecimento.txt`**
   - Este arquivo conterá as informações que o chatbot usará para responder perguntas.
2. **Inicie o chatbot:**
   ```bash
   streamlit run rag_llm_first.py
   ```
3. **Acesse o navegador** em `http://localhost:8501` e faça perguntas ao chatbot!

## 📝 Exemplo de Uso
Digite uma pergunta baseada no conteúdo do `base_de_conhecimento.txt`, e o chatbot responderá com base nas informações fornecidas.

## 🛠️ Tecnologias Utilizadas
- [LangChain](https://python.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Hugging Face Inference API](https://huggingface.co/docs/api-inference/)
- [Streamlit](https://streamlit.io/)

## 📜 Licença
Este projeto é distribuído sob a licença MIT.

---
🔗 **Contato:** Para dúvidas ou sugestões, abra uma issue ou me encontre no [LinkedIn]([https://www.linkedin.com/in/seu-perfil](https://www.linkedin.com/in/daniel-hl-fraga/)).

