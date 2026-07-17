import streamlit as st

from app.core.version import APP_NAME
from app.core.version import APP_VERSION
from app.core.logger import Logger

Logger.info("Application Started")

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🚀 " + APP_NAME)

st.caption("Version " + APP_VERSION)

st.success("Sprint 2.2")