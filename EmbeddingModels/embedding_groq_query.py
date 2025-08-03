from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text=[
    "My name is Nishant Kumar Jha",
    "I am the only one here"
]
vector=embedding.embed_documents(text)
print(str(vector))
