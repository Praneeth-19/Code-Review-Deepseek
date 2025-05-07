import streamlit as st
import requests

st.title("Code Review Assistant (DeepSeek)")

code_input = st.text_area("Paste your code here:", height=300)

if st.button("Get Review"):
    try:
        response = requests.post("http://localhost:8000/review/", data={"code": code_input})
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        try:
            review = response.json().get("review", "No feedback returned.")
        except requests.exceptions.JSONDecodeError:
            review = f"Error: Received invalid JSON response from backend. Raw response: {response.text}"
        
        st.subheader("Review & Suggestions:")
        st.code(review)
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to backend: {str(e)}")
        st.info("Please make sure the FastAPI backend is running on port 8000")
