# This is a simple chatbot with langchain and Gemini
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os
import google.generativeai as genai
load_dotenv()

apikey = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=apikey)


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

st.title("💬 Chat avec Gemini (LangChain)")

question = st.text_input("Pose ta question :")

if question:
    response = llm([HumanMessage(content=question)])
    st.write("**Gemini :**", response.content)