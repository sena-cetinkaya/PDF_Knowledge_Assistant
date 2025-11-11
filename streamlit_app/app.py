import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/api"

st.title("📚 PDF Knowledge Assistant")

# Session state variables / Session state değişkenleri
if "pdf_uploaded" not in st.session_state:
    st.session_state["pdf_uploaded"] = False
if "uploaded_file_name" not in st.session_state:
    st.session_state["uploaded_file_name"] = None

# PDF Upload / PDF Yükleme
st.header("📄 PDF Upload")
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file and not st.session_state["pdf_uploaded"]:
    with st.spinner("PDF loading..."):
        response = requests.post(
            f"{API_URL}/upload_pdf",
            files={"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")},
        )

        if response.status_code == 200:
            st.session_state["pdf_uploaded"] = True
            st.session_state["uploaded_file_name"] = uploaded_file.name
            st.success(f"{uploaded_file.name} successfully uploaded ✅")
        else:
            st.error("An error occurred while loading the PDF ❌")

elif st.session_state["pdf_uploaded"]:
    st.info(f"📘 {st.session_state['uploaded_file_name']} Uploaded. Refresh the page to upload a new PDF.")

# Q&A / Soru-Cevap
st.header("💬 Ask a Question")
question = st.text_input("Type your question:")

if st.button("Ask"):
    if not st.session_state["pdf_uploaded"]:
        st.warning("You must upload a PDF first.")
    elif question.strip() == "":
        st.warning("Please write a question.")
    else:
        with st.spinner("Response is being generated..."):
            response = requests.post(f"{API_URL}/ask", json={"question": question})
            if response.status_code == 200:
                st.write("**Answer:**", response.json()["answer"])
            else:
                st.error("An error occurred, please try again.")



