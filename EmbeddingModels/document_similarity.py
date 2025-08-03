from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
embedding= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents=[
    "Virat kolhi is the great batsman",
    "Rohit sharma is the best opener in the world",
    "Sachin Tendulkar is also known as the god of cricket in the world",
    "Jasprit bhumrah is currently the best fast bowler in the world"
]
query="Tell me about Sharma"
query_embed=embedding.embed_query(query)
embed_doc=embedding.embed_documents(documents)
scores=cosine_similarity([query_embed], embed_doc)[0]
index, scores=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print(scores)