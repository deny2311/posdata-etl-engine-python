import streamlit as st

from app.developer import (
    render_database_tab,
    render_storage_tab,
    render_transfer_tab,
    render_engine_tab,
)

st.title("🧪 Developer Console")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Database",
        "Storage",
        "Transfer",
        "Engine",
    ]
)

with tab1:
    render_database_tab()

with tab2:
    render_storage_tab()

with tab3:
    render_transfer_tab()

with tab4:
    render_engine_tab()