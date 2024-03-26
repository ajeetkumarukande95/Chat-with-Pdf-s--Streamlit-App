import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from templates.html_templates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub

def get_pdf_text(pdf_docs):
    """
    for examples:
    Loading PDFs...
    PDF Text: Streamlit is a Python library that makes it easy to create and share web apps. 
    With Streamlit, you can turn data scripts into shareable web apps in minutes, without having to write any front-end code. 
    It's designed to be intuitive and simple to use, allowing data scientists and developers to focus on building interactive and engaging applications...
    """
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    """
    Extracting text chunks...
    Text Chunks: ['Streamlit is a Python library that makes it easy to create and share web apps.', 
    'With Streamlit, you can turn data scripts into shareable web apps in minutes, without having to write any front-end code.', 
    'It's designed to be intuitive and simple to use, allowing data scientists and developers to focus on building interactive and engaging applications.']
    """"
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    """
    Vector Store:
    - Text Chunk 1:
      Vector: [0.12, 0.45, ..., 0.78]  # Example vector representation of dimension 512
    - Text Chunk 2:
      Vector: [0.25, 0.68, ..., 0.92]
    - Text Chunk 3:
      Vector: [0.31, 0.74, ..., 0.85]
    """
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation_chain(vectorstore):
    """
    Initializing conversation chain...
    Conversation Chain:
    - Language Model: ChatOpenAI
    - Retriever: FAISS VectorStore Retriever
    - Memory: Conversation Buffer Memory
    """
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
