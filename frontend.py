import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL")

st.title("Frontend (Streamlit)")

if st.button("Check Backend Health"):
    try:
        r = requests.get(f"{BACKEND_URL}/")
        st.json(r.json())
    except Exception as e:
        st.error(f"Error: {e}")

if st.button("Check NAT Gateway"):
    try:
        r = requests.get(f"{BACKEND_URL}/check_nat")
        st.json(r.json())
    except Exception as e:
        st.error(f"Error: {e}")
