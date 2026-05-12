import streamlit as st

st.title("🎥 YouTube Q&A Bot")

url=st.text_input("Paste YouTube URL")
if url:
  st.write(url)
  