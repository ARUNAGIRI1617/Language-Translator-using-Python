#Translator
from google_trans_new import google_translator

import streamlit as st

translator = google_translator()

st.title("Language Translator")

text = st.text_input("Enter a text")

translate = translator.translate(text, lang_tgt='de')# you can give any country code eg:"fr","en","th",etc...

st.write(translate)
