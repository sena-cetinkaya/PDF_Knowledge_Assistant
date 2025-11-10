from functools import lru_cache
from langchain_community.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import LlamaCpp
from app.utils.config import *

@lru_cache(maxsize=1)
def get_qa_chain():
    llm = LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.75,
        top_p=1,
        f16_kv=True,
        verbose=False,
        n_ctx=4096,
    )
    vector_store = Chroma(persist_directory=CHROMA_DB_DIR)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
    )
    return qa_chain

def ask_question(question: str):
    # Chroma veritabanını güncel haliyle yeniden yükle
    vector_store = Chroma(persist_directory=CHROMA_DB_DIR)
    qa_chain = get_qa_chain()
    qa_chain.retriever = vector_store.as_retriever()

    response = qa_chain.run({"question": question})
    return response


"""def ask_question(question: str):
    qa_chain = get_qa_chain()
    response = qa_chain.run({"question": question})
    return response"""





"""from langchain_community.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import LlamaCpp
from app.utils.config import *

def get_qa_chain():
    llm = LlamaCpp(
        streaming=True,
        model_path=MODEL_PATH,
        temperature=0.75,
        top_p=1,
        f16_kv=True,
        verbose=False,
        n_ctx=4096
    )

    vector_store = Chroma(persist_directory=CHROMA_DB_DIR)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return qa_chain

qa_chain = get_qa_chain()

def ask_question(question: str):
    response = qa_chain.run({"question": question})
    return response"""
