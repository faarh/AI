from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrivalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

import streamlit as st

from watsonxlangchain import LangChainInterface
st.title('Ask watsonx')
prompt = st.chat_input('Pass your prompt here: ')

if prompt: 
    st.chat_message('user').markdown()