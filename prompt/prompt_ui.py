from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st 
import os
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")
model = ChatGroq(model_name="llama3-70b-8192", api_key=api_key, temperature=1.5)

st.header("Reasearch Tool")
# user_input=st.text_area("Enter Your Prompt")
paper_input=st.selectbox('Select the paper:',["Attention Is All You Need","BERT:Pre-training for Deep Bidirectional Transformers", "GPT-3: Language Models are Few-shot Learners"])
style_input=st.selectbox('Select the explanation style:',["Biggner-Friendly","Technical","code-Oriented","Mathematical"])
length_input=st.selectbox('Select the lenght:',["short (1-2 paragraphs)","Medium (3-5) paragraph","Long (detailed Expalanation)"])
template= load_prompt("Template.json")
#fill the placeholders
# prompt=template.invoke({
#         "paper_input":paper_input,
#         "style_input":style_input,
#         "length_input":length_input
#         }
# )

if st.button("Summrize"):
    formatted_prompt=template.format(paper_input=paper_input,
        style_input=style_input,
        length_input=length_input
        )
    result=model.invoke(formatted_prompt)
    st.subheader("Summary")
    st.write(result.content)