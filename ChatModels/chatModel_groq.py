from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
cont='Y'
while(cont != 'N'):
    api_key=os.getenv("GROQ_API_KEY")

    load_dotenv()
    model=ChatGroq(model="llama3-70b-8192", api_key=api_key)
    result=model.invoke(str(input()))
    print(result.content)
    cont=str(input("Y/N"))