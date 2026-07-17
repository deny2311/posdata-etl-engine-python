import streamlit as st
import sys
import platform

from app.core.config import Config

st.title("🔍 System Check")

st.subheader("Application")

st.write("Name :", Config.app_name())

st.write("Version :", Config.version())

st.write("Environment :", Config.env())

st.divider()

st.subheader("Python")

st.write(sys.version)

st.write(platform.platform())