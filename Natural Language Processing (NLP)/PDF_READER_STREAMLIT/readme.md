
# 📄 PDF Okuyucu – LangChain & Ollama ile Soru Cevaplama

Bu proje, **Streamlit** tabanlı bir web uygulamasıdır.
Kullanıcıların **PDF dosyası yüklemesine**, bu PDF’den **metin çıkarılmasına**, metnin **embedding tabanlı vektör veritabanında (FAISS)** saklanmasına ve daha sonra **Ollama tabanlı büyük dil modelleri** aracılığıyla PDF hakkında sorular sorabilmesine olanak tanır.

---

## 🚀 Özellikler

* 📑 PDF dosyası yükleme
* 🧩 Metinleri parçalara bölme (chunking)
* 🔎 FAISS ile embedding tabanlı hızlı arama
* 🤖 Ollama modelleri (ChatOllama + Embeddings) ile soru-cevap
* 💬 Sohbet geçmişi (ConversationBufferMemory) desteği
* ⏳ Gerçek zamanlı (streaming) model çıktısı

---

## ⚠️ Notlar

* Projede kullanılan modeller **Ollama** üzerinden çalışmaktadır. Dolayısıyla sisteminizde [Ollama](https://ollama.ai) kurulu olmalıdır.
* Varsayılan modeller:

  * **Embedding**: `mxbai-embed-large`
  * **Chat LLM**: `llama3.2:3b`
* Ücretsiz ve küçük modeller kullanıldığından cevapların doğruluğu ve kapsamı sınırlı olabilir. Daha büyük modellerle sonuçlar iyileştirilebilir.

---

## 🛠️ Kullanılan Teknolojiler

* **Python 3.10+**
* **Streamlit** – web arayüzü
* **PyPDF2** – PDF’den metin çıkarma
* **LangChain** – metin işleme, bellek ve mesaj akışı
* **FAISS** – vektör veritabanı
* **Ollama** – dil modeli ve embedding desteği

---

## 📦 Kurulum & Çalıştırma

### 1. Depoyu klonlayın

```bash
git clone https://github.com/kullanici/pdf-okuyucu-llm.git
cd pdf-okuyucu-llm
```

### 2. Gerekli kütüphaneleri yükleyin

```bash
pip install -r requirements.txt
```

### 3. Ollama’yı kurun

* [Resmi Ollama sayfasından](https://ollama.ai) işletim sisteminize uygun kurulumu yapın.
* İhtiyacınız olan modelleri indirin:

  ```bash
  ollama pull llama3.2:3b
  ollama pull mxbai-embed-large
  ```

### 4. Uygulamayı çalıştırın

```bash
streamlit run app.py
```

### 5. Tarayıcıdan açın

`http://localhost:8501`

---

## 📷 Ekran Görüntüsü

![alt text](image-1.png)

---



