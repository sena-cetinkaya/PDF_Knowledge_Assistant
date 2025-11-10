import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api"

st.title("📚 PDF Knowledge Assistant")

# Session state değişkenleri
if "pdf_uploaded" not in st.session_state:
    st.session_state["pdf_uploaded"] = False
if "uploaded_file_name" not in st.session_state:
    st.session_state["uploaded_file_name"] = None

# PDF Yükleme
st.header("📄 PDF Yükle")
uploaded_file = st.file_uploader("Bir PDF yükleyin", type=["pdf"])

if uploaded_file and not st.session_state["pdf_uploaded"]:
    with st.spinner("PDF yükleniyor..."):
        response = requests.post(
            f"{API_URL}/upload_pdf",
            files={"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")},
        )

        if response.status_code == 200:
            st.session_state["pdf_uploaded"] = True
            st.session_state["uploaded_file_name"] = uploaded_file.name
            st.success(f"{uploaded_file.name} başarıyla yüklendi ✅")
        else:
            st.error("PDF yüklenirken bir hata oluştu ❌")

elif st.session_state["pdf_uploaded"]:
    st.info(f"📘 {st.session_state['uploaded_file_name']} yüklendi. Yeni PDF yüklemek için sayfayı yenileyin.")

# Soru-Cevap
st.header("💬 Soru Sor")
question = st.text_input("Sorunuzu yazın:")

if st.button("Sor"):
    if not st.session_state["pdf_uploaded"]:
        st.warning("Önce bir PDF yüklemelisiniz.")
    elif question.strip() == "":
        st.warning("Lütfen bir soru yazın.")
    else:
        with st.spinner("Yanıt üretiliyor..."):
            response = requests.post(f"{API_URL}/ask", json={"question": question})
            if response.status_code == 200:
                st.write("**Cevap:**", response.json()["answer"])
            else:
                st.error("Bir hata oluştu, lütfen tekrar deneyin.")


