from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
model = ChatGroq(model_name="llama3-70b-8192", api_key=api_key, temperature=1.5)
messages=[
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]

result=model.invoke(messages)
messages.append(AIMessage(result.content))
print(messages)