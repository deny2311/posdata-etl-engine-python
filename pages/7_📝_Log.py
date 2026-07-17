from pathlib import Path

import streamlit as st

from app.core.config import Config


st.title("📝 Log")

log_path = Path(Config.get("LOG_PATH"))

if not log_path.exists():

    st.warning("Belum ada log.")

    st.stop()

files = sorted(
    log_path.glob("*.log"),
    reverse=True
)

if not files:

    st.info("Belum ada log.")

    st.stop()

latest = files[0]

st.subheader(latest.name)

text = latest.read_text(
    encoding="utf-8"
)

st.code(text)