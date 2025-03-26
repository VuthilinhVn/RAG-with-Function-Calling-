# rag/helper_functions.py
import json
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def about_booking(info):
    db = FAISS.load_local("db/booking_index", OpenAIEmbeddings(model="text-embedding-3-large"), allow_dangerous_deserialization=True)
    results = db.similarity_search(info, k=3)
    docs = [{"content": doc.page_content} for doc in results]
    return json.dumps(docs, ensure_ascii=False)

def about_products(info):
    db = FAISS.load_local("db/products_index", OpenAIEmbeddings(model="text-embedding-3-large"), allow_dangerous_deserialization=True)
    results = db.similarity_search(info, k=3)
    docs = [{"content": doc.page_content} for doc in results]
    return json.dumps(docs, ensure_ascii=False)

def reviews_search(info):
    db = FAISS.load_local("db/reviews_index", OpenAIEmbeddings(model="text-embedding-3-large"), allow_dangerous_deserialization=True)
    results = db.similarity_search(info, k=5)
    docs = [{"content": doc.page_content} for doc in results]
    return json.dumps(docs, ensure_ascii=False)
