import streamlit as st
import sys
import platform

from app.core.config import Config
from app.core.database import Database

st.title("🔎 System Check")

# ======================================
# APPLICATION
# ======================================

st.header("Application")

st.write("**Name :**", Config.app_name())
st.write("**Version :**", Config.version())
st.write("**Environment :**", Config.env())

st.divider()

# ======================================
# PYTHON
# ======================================

st.header("Python")

st.write(sys.version)

st.write(platform.platform())

st.divider()

# ======================================
# DATABASE
# ======================================

st.header("Database")

db = Database()

status = db.health_check()

if status["connected"]:

    st.success("Database Connected")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Host**")
        st.write(status["host"])

        st.write("**Database**")
        st.write(status["database"])

        st.write("**User**")
        st.write(status["user"])

    with col2:

        st.write("**Version**")
        st.write(status["version"])

        st.write("**Charset**")
        st.write(status["charset"])

else:

    st.error("Database Failed")

    st.exception(status["error"])