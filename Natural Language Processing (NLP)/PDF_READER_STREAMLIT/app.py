import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage, HumanMessage, AIMessage

def main():

    # Session state initialization
    if "memory" not in st.session_state:
        st.session_state.memory = ConversationBufferMemory(return_messages=True)
    if "knowledge_base" not in st.session_state:
        st.session_state.knowledge_base = None

    st.set_page_config(page_title="PDF Okuyucu", page_icon="📄")
    st.header("📄 PDF Okuyucu ve Soru Cevaplama (Streaming Destekli)")
    st.markdown("PDF yükleyin, embedding tabanlı arama ile sorular sorun.")

    # PDF upload
    pdf = st.file_uploader("PDF dosyasını yükleyin", type=["pdf"])
    if pdf is not None and st.session_state.knowledge_base is None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"

        # Chunking
        text_splitter = CharacterTextSplitter(
            separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Embeddings + FAISS
        embeddings = OllamaEmbeddings(model="mxbai-embed-large")
        st.session_state.knowledge_base = FAISS.from_texts(chunks, embeddings)

    # Streaming LLM
    llm = ChatOllama(model="llama3.2:3b", streaming=True)

    # Kullanıcı input
    user_input = st.chat_input("PDF hakkında bir soru sorun")
    if user_input and st.session_state.knowledge_base:
        st.session_state.memory.chat_memory.add_user_message(user_input)

        # take context by Retriever  
        docs = st.session_state.knowledge_base.similarity_search(user_input, k=5)
        context = "\n\n".join([d.page_content for d in docs])

        # Preparing to the Messeages
        messages = [
            SystemMessage(content=(
                "Sen bir PDF destek asistanısın. "
                "Kullanıcılara yalnızca sağlanan PDF içeriğinden faydalanarak yanıt ver. "
                "Eğer içerikte bilgi yoksa 'Bu konuda bilgim yok' de.\n\n"
                f"Bağlam:\n{context}"
            ))
        ] + st.session_state.memory.load_memory_variables({})["history"] + [HumanMessage(content=user_input)]

        # Streaming output
        with st.chat_message("Asistan (AI)"):
            placeholder = st.empty()
            response_text = ""
            for chunk in llm.stream(messages):
                response_text += chunk.content or ""
                placeholder.markdown(response_text)

            # Save the response to in Memory
            st.session_state.memory.chat_memory.add_ai_message(response_text)

    # Print the Chat History
        for msg in st.session_state.memory.chat_memory.messages:
            if isinstance(msg, HumanMessage):
                with st.chat_message("Kullanıcı"):
                    st.markdown(msg.content)
            elif isinstance(msg, AIMessage):
                with st.chat_message("Asistan (AI)"):
                    st.markdown(msg.content)


            
if __name__ == "__main__":
    main()
