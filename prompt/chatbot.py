from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import PromptTemplate
import streamlit as st 
import os
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
model = ChatGroq(model_name="llama3-70b-8192", api_key=api_key, temperature=1.5)
chat_history=[
    SystemMessage(content="You are a helpful AI assitant")
]
while True:
    user_input=input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input=='exit':
        break
    result= model.invoke(user_input)
    print('AI: ', result.content)
    chat_history.append(AIMessage(content=result.content))
print(chat_history)