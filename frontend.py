import streamlit as st
import requests

BACKEND_URL = "http://${backend_alb_dns}"  # replace with backend ALB DNS

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
