import os
import requests
import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub
from langchain.document_loaders import TextLoader

def ler_credenciais(caminho_arquivo):
    """Lê credenciais de um arquivo de configuração."""
    credenciais = {}
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip()  # Remove espaços em branco e quebras de linha
                if linha and '=' in linha:  # Verifica se a linha não está vazia e contém '='
                    chave, valor = linha.split('=', 1)  # Divide a linha em chave e valor
                    credenciais[chave] = valor
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
    return credenciais

caminho_arquivo = 'config.txt'
credenciais = ler_credenciais(caminho_arquivo)

hugging_face_api = credenciais.get('HUGGINGFACE_API_KEY')

# Configuração da API Hugging Face
HUGGINGFACE_API_KEY = hugging_face_api
#MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1" # Erro 503 (Serviço Temporariamente Indisponível)
MODEL_NAME = "tiiuae/falcon-7b-instruct"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACE_API_KEY

# Carregar documentos
def load_documents():
    loader = TextLoader("base_de_conhecimento.txt")  # Arquivo de texto com o conhecimento do chatbot
    documents = loader.load()
    return documents

# Criar embeddings e armazenar no FAISS
def create_vector_store(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, 
        chunk_overlap=50
        )
    texts = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(texts, embeddings)
    return vectorstore

# Criar pipeline de QA
def create_qa_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    llm = HuggingFaceHub(repo_id=MODEL_NAME, model_kwargs={"temperature": 0.1, "max_length": 512})
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff", chain_type_kwargs={"verbose": True})
    return qa_chain

# Criar UI com Streamlit
def main():
    st.title("Chatbot LangChain + FAISS")
    st.write("Faça perguntas com base no conhecimento carregado.")
    
    documents = load_documents()
    vectorstore = create_vector_store(documents)
    qa_chain = create_qa_chain(vectorstore)
    
    user_query = st.text_input("Digite sua pergunta:")
    if st.button("Perguntar") and user_query:
        response = qa_chain.run(user_query)
        st.write("### Resposta:")
        st.write(response)

if __name__ == "__main__":
    main()