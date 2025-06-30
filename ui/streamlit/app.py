import streamlit as st
import os
from pymilvus import connections, Collection
import requests

# --- Configuration ---
MILVUS_HOST = os.getenv("MILVUS_HOST", "vectordb-milvus.milvus.svc.cluster.local")
MILVUS_PORT = os.getenv("MILVUS_PORT", "19530")
COLLECTION_NAME = os.getenv("MILVUS_COLLECTION", "pdf_collection")
LLM_ENDPOINT = os.getenv("LLM_ENDPOINT", "http://vllm.vllm.svc.cluster.local:8000/v1")
EMBEDDING_SERVER_URL = os.getenv("EMBEDDING_SERVER_URL", "http://embedding-server:8000/embed")

PROMPT_TEMPLATE = """<s>[INST] <<SYS>>
You are a helpful, respectful and honest assistant named HatBot answering questions.
You will be given a question you need to answer, and a context to provide you with information. You must answer the question based as much as possible on this context.
Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
<</SYS>>

Context: 
{context}

Question: {question} [/INST]"""

st.set_page_config(page_title="Simple LLM RAG Demo", layout="centered")
st.title("Simple LLM RAG Demo (Milvus + LLM)")

@st.cache_resource
def get_milvus_collection():
    connections.connect(host=MILVUS_HOST, port=MILVUS_PORT)
    return Collection(COLLECTION_NAME)

def get_embedding(text):
    response = requests.post(
        EMBEDDING_SERVER_URL,
        json={"text": text},
        timeout=30
    )
    response.raise_for_status()
    return response.json()["embedding"]

def search_context(question, top_k=3):
    embedding = get_embedding(question)
    collection = get_milvus_collection()
    results = collection.search(
        data=[embedding],
        anns_field="embedding",
        param={"metric_type": "L2", "params": {"nprobe": 10}},
        limit=top_k,
        output_fields=["text"]
    )
    context = "\n".join([hit.entity.get("text", "") for hit in results[0]])
    return context

def query_llm(context, question):
    prompt = PROMPT_TEMPLATE.format(context=context, question=question)
    response = requests.post(
        LLM_ENDPOINT,
        json={"prompt": prompt},
        timeout=60
    )
    if response.status_code == 200:
        # Adjust this if your LLM server returns a different key
        return response.json().get("answer", response.text)
    else:
        return f"Error from LLM: {response.text}"

question = st.text_input("Ask a question:", help="Enter your question for the LLM.")

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching context and querying LLM..."):
            try:
                context = search_context(question)
                if not context:
                    st.error("No relevant context found in Milvus.")
                else:
                    answer = query_llm(context, question)
                    st.markdown("**Context:**")
                    st.code(context)
                    st.markdown("**Answer:**")
                    st.success(answer)
            except Exception as e:
                st.error(f"Error: {e}")

st.markdown("---")
st.caption("Deployable on OpenShift. Set MILVUS_HOST, MILVUS_PORT, LLM_ENDPOINT, and EMBEDDING_SERVER_URL as environment variables.")