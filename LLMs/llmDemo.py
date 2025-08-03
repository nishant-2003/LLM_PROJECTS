from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

llm=ChatGroq(model="llama3-70b-8192", api_key=api_key)
result=llm.invoke("What is the capital of India?")
print(result)