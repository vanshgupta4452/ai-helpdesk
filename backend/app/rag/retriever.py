from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def get_answer(query):
    db = FAISS.load_local("faiss_index", OpenAIEmbeddings())
    docs = db.similarity_search(query)
    return docs[0].page_content