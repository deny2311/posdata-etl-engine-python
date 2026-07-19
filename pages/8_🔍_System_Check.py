import streamlit as st

from app.ui.render_system_check import (
    render_application,
    render_python,
    render_database,
    render_storage,
    render_disk,
)

st.title("🔎 System Check")

render_application()
render_python()
render_database()
render_storage()
render_disk()