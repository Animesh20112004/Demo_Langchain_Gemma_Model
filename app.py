import os 
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"]="true"

## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful but a bit rude and direct and thruthfull assitant. Please respond to the question asked in the most direct manner"),
        ("user","Question:{question}")
    ]
)

st.title("ChatBot made using Llama 3")
input_text=st.text_input("What do you want to ask ?")
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))