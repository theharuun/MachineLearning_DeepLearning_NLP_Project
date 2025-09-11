from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings

def process_pdf(pdf_path: str):
    """PDF'den metin çıkar ve FAISS vektör deposu oluştur."""
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        extracted_text = page.extract_text()
        if extracted_text:
            text += extracted_text + "\n"

    if not text.strip():
        raise ValueError("PDF'den metin çıkarılamadı.")

    # Chunking (Parçalama) yani metni küçük parçalara bölüyoruz çünkü tam metin çok büyük olabilir ve token limitini aşabilir bu yüzden 1000 tokenlık chunklara bölüyoruz ve 200 token overlap (artık) bırakıyoruz
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    chunks = text_splitter.split_text(text)

    # Embeddings + FAISS oluşturma
    embeddings = OllamaEmbeddings(model="mxbai-embed-large")
    knowledge_base = FAISS.from_texts(chunks, embeddings) # chunkları kullanarak FAISS vektör deposu oluşturuyoruz 

    return knowledge_base
