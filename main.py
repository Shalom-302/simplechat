# # This is a simple chatbot with langchain and Gemini
# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.schema import HumanMessage
# from dotenv import load_dotenv
# import os
# import google.generativeai as genai
# load_dotenv()

# apikey = os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=apikey)


# llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# st.title("💬 Chat avec Gemini (LangChain)")

# question = st.text_input("Pose ta question :")

# if question:
#     response = llm([HumanMessage(content=question)])
#     st.write("**Gemini :**", response.content)

#####################################################

import streamlit as st
import google.generativeai as genai
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=apikey)

# Configuration du modèle Gemini Vision
model = genai.GenerativeModel('gemini-1.5-pro')

st.title("🖼️ Application OCR avec Gemini Vision")

uploaded_file = st.file_uploader("Télécharge une image...", type=["png", "jpg", "jpeg"])
prompt_template = st.text_area("Prompt pour l'extraction d'informations:",
                                value="Extraire toutes les informations textuelles pertinentes de cette image. Sois précis et inclus toutes les données importantes.")

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Image téléchargée.", use_container_width=True)

    if st.button("Lancer l'OCR"):
        if prompt_template:
            try:
                response = model.generate_content(
                    [prompt_template, image],
                    stream=False
                )
                response.resolve()
                st.subheader("Résultat de l'OCR:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Une erreur s'est produite : {e}")
        else:
            st.warning("Veuillez entrer un prompt pour l'extraction.")