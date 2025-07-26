import streamlit as st
import sys
from openai import OpenAI

client = OpenAI(api_key="")

st.title("Upload and Clean XML/CSV with AI")

uploaded_file = st.file_uploader("Choose a CSV or XML file", type=["csv", "xml"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("File Content", content, height=300)

    if st.button("Clean File"):
        prompt = f"""
        You are a helpful assistant. Clean and fix this data file if there are errors or malformed content:

        {content}
        """
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful data cleaning assistant."},
                {"role": "user", "content": prompt}
            ],
        )
        cleaned = response.choices[0].message.content
        st.text_area("Cleaned Output", cleaned, height=300)

if st.button("Exit App"):
    st.write("Exiting app...")
    sys.exit()
