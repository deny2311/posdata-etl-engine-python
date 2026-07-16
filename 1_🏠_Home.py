import streamlit as st

st.title("🏠 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Database",
        "Offline"
    )

with col2:
    st.metric(
        "FTP",
        "Offline"
    )

with col3:
    st.metric(
        "Download Queue",
        0
    )

with col4:
    st.metric(
        "Import Queue",
        0
    )

st.divider()

st.subheader("System Information")

st.write("Version : 0.1.0")

st.write("Environment : Development")

st.write("Python : Ready")