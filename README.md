# 📚 PDF Knowledge Assistant (FastAPI + LangChain + Streamlit + Llama)

Bu proje, kullanıcıların yükledikleri PDF belgeleri hakkında **doğal dilde soru sorup yanıt almasını** sağlayan bir yapay zeka destekli asistan uygulamasıdır.  
Model, **Llama (Mistral-7B)** tabanlıdır ve **LangChain + ChromaDB** altyapısı ile bilgi tabanı oluşturur.

---

## 🚀 Özellikler

- 🧠 Llama (Mistral-7B) tabanlı metin anlayışı
- 📄 PDF yükleme ve içerik vektörleştirme (LangChain + ChromaDB)
- 💬 Doğal dilde soru-cevap (ConversationalRetrievalChain)
- 🌐 FastAPI tabanlı REST API
- 🎨 Streamlit kullanıcı arayüzü
- ⚙️ GPU / CPU destekli Torch entegrasyonu
- 🧩 Modüler yapı (services, routes, utils, streamlit_app)

---

## 🗂️ Proje Yapısı

pdf_assistant/

│

├── app/

│ ├── main.py # FastAPI uygulama giriş noktası

│ ├── routes/

│ │ ├── upload_routes.py # PDF yükleme endpoint’i

│ │ └── qa_routes.py # Soru-cevap endpoint’i

│ ├── services/

│ │ ├── pdf_service.py # PDF işleme, embedding ve Chroma veritabanı

│ │ └── qa_service.py # Llama modeli ile QA zinciri

│ ├── utils/

│ │ └── config.py # Model yolu, cihaz, embedding ayarları

│

├── streamlit_app/

│ └── app.py # Streamlit kullanıcı arayüzü

│

├── mistral-7b-openorca.Q4_0.gguf # Llama model dosyası

├── requirements.txt

└── vector_db/ # (Çalışma sırasında oluşturulur)


---

## ⚙️ Kurulum

### 1️⃣ Ortamı Hazırla
```
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

2️⃣ FastAPI Sunucusunu Başlat
```
uvicorn app.main:app --reload
```
3️⃣ Streamlit Arayüzünü Başlat
```
streamlit run streamlit_app/app.py
```
---

💡 Kullanım

1️⃣ Bir PDF dosyası yükleyin.

2️⃣ Model, PDF içeriğini ChromaDB veritabanına dönüştürür.

3️⃣ Ardından doğal dilde sorularınızı sorun:

---


Örneğin: “Bu belgede hangi şirketten bahsediliyor?”

✅ Uygulama, PDF’ten öğrenilen bilgilerle yanıt üretir.

---

🧠 Teknolojiler

FastAPI – Backend API

Streamlit – Kullanıcı arayüzü

LangChain – Bilgi alma zinciri

Llama (Mistral-7B) – Dil modeli

ChromaDB – Vektör tabanlı arama

SentenceTransformers – Embedding modeli

Torch – GPU hızlandırma

---

🧪 API Örnekleri

📄 PDF Yükleme

POST /api/upload_pdf
```
curl -X POST "http://127.0.0.1:8000/api/upload_pdf" \
  -F "file=@example.pdf"
```
💬 Soru Sorma

POST /api/ask
```
{
  "question": "PDF belgesinin ana konusu nedir?"
}
```
Response:
```
{
  "answer": "Belge, yapay zekanın endüstrideki kullanım alanlarını anlatmaktadır."
}
```

---

📃 Gereksinimler
requirements.txt
```
torch~=2.9.0
fastapi~=0.121.1
pydantic~=2.12.4
langchain~=0.2.16
streamlit~=1.51.0
requests~=2.32.5
```

---

📃 Lisans: MIT Lisansı

👩‍💻 Geliştirici: Sena Çetinkaya

🌐 GitHub: [https://github.com/sena-cetinkaya](https://github.com/sena-cetinkaya)
