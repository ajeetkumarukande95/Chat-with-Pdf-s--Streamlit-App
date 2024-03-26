import streamlit as st
from dotenv import load_dotenv
from templates.html_templates import css, bot_template, user_template
from helpers import get_pdf_text, get_text_chunks, get_vectorstore, get_conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.format(MSG=message.content, USER_SYMBOL="👤"), unsafe_allow_html=True)
        else:
            st.write(bot_template.format(MSG=message.content, BOT_SYMBOL="🤖"), unsafe_allow_html=True)
     
def main():
    load_dotenv()
    st.set_page_config(page_title="Ask Anything about Provided Document", page_icon=":books:", layout="wide")
    
    st.title("Chat with Provided PDFs :books:")
    st.markdown('<div class="title-container"><div class="title-text">Ask Anything about Provided Pdf</div></div>', unsafe_allow_html=True)
    st.write("Developed by Ajeetkumar Ukande", unsafe_allow_html=True)

    if "conversation" not in st.session_state or st.session_state.conversation is None:
        st.session_state.conversation = None
        st.session_state.chat_history = None

    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        if st.session_state.conversation is not None:
            handle_userinput(user_question)
        else:
            st.write("Conversation not initialized. Please process PDFs first.")

    col1, col2 = st.columns([1, 4])
    with col1:
        pass  

    with col2:
        with st.sidebar:
            st.subheader("Your documents")
            pdf_docs = st.file_uploader(
                "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
            if st.button("Process"):
                with st.spinner("Processing"):
                    # get pdf text
                    raw_text = get_pdf_text(pdf_docs)

                    # get the text chunks
                    text_chunks = get_text_chunks(raw_text)

                    # create vector store
                    vectorstore = get_vectorstore(text_chunks)

                    # create conversation chain
                    st.session_state.conversation = get_conversation_chain(
                        vectorstore)

if __name__ == '__main__':
    main()
