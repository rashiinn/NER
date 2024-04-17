import streamlit as st
import spacy
import requests
from bs4 import BeautifulSoup
import en_core_web_sm

st.title("NER Demo")

nlp = en_core_web_sm.load()

text1 = st.text_area("Enter URL")
text2 = st.text_area("Enter a paragraph")

if st.button("Analyse"):
    if text1:
        try:
            response = requests.get(text1)
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            doc = nlp(text)
            entities = [(X.text, X.label_) for X in doc.ents]
            st.success(entities)
        except:
            st.error("Error opening URL. Please make sure it's valid.")
    elif text2:
        doc = nlp(text2)
        entities = [(X.text, X.label_) for X in doc.ents]
        st.success(entities)
    else:
        st.warning("Please enter a URL or a paragraph.")
