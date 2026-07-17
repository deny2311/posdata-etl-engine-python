import streamlit as st

from app.engines.downloader_engine import DownloaderEngine

st.title("Downloader")

engine = DownloaderEngine()

result = engine.run()

if result.success:

    st.success(result.message)

else:

    st.error(result.message)