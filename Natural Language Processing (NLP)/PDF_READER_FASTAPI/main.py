from fastapi import FastAPI, UploadFile, File, Form 
from langchain_ollama import ChatOllama
from langchain.schema import SystemMessage, HumanMessage
from utils import process_pdf

app = FastAPI()

# Global state (örnek için bellekte tutuyoruz) böylece pdf yüklendikten sonra hafızasında embeding halini tutucak  ve ask endpointinde kullanıcının sorusuna cevap verecek
knowledge_base = None

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    global knowledge_base # Global state
    # PDF'i geçici dosyaya kaydet 
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())

    knowledge_base = process_pdf(temp_path) # PDF'i işle ve knowledge_base'i güncelle utils modülündeki fonksiyonu kullanarak yapıyoruz
    return {"status": "success", "message": f"{file.filename} yüklendi ve işlendi."}

@app.post("/ask/")
async def ask_question(question: str = Form(...)):
    global knowledge_base
    if knowledge_base is None:
        return {"error": "Önce PDF yükleyin."}

    # Retriever ile context al
    docs = knowledge_base.similarity_search(question, k=5) # en benzer 5 chunkı alıyoruz
    context = "\n\n".join([d.page_content for d in docs]) # chunkları birleştiriyoruz

    # LLM çağrısı 
    llm = ChatOllama(model="llama3.2:3b")
    messages = [
        SystemMessage(content=( # sisteme talimat veriyoruz , kullanıcıya nasıl cevap vereceği hakkında onu öğretiyoruz
            "Sen bir PDF destek asistanısın. "
            "Kullanıcılara yalnızca sağlanan PDF içeriğinden faydalanarak yanıt ver. "
            "Eğer içerikte bilgi yoksa 'Bu konuda bilgim yok' de.\n\n"
            f"Bağlam:\n{context}"
        )),
        HumanMessage(content=question) # kullanıcıdan gelen soruyu ekliyoruz,
    ]
    response = llm.invoke(messages) # llm den cevabı alıyoruz , llm cevabını beklemek için blokluyoruz


    return {"question": question, "answer": response.content}
