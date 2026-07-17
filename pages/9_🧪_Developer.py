import streamlit as st

st.set_page_config(
    page_title="Developer",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Developer Console")

st.info(
    "Halaman ini digunakan untuk menguji setiap module ETL."
)

tab1, tab2, tab3, tab4 = st.tabs([
    "Database",
    "Storage",
    "Transfer",
    "Engine"
])