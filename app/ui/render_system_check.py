import platform

import streamlit as st

from app.core.config import Config
from app.core.database import Database
from app.core.storage import Storage


def render_application() -> None:
    """
    Application information.
    """

    st.subheader("📦 Application")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("App", Config.app_name())

    with col2:
        st.metric("Version", Config.version())

    with col3:
        st.metric("Environment", Config.env())


def render_python() -> None:
    """
    Python runtime information.
    """

    st.subheader("🐍 Python")

    st.json({
        "Version": platform.python_version(),
        "Platform": platform.platform(),
    })


def render_database() -> None:
    """
    Database information.
    """

    st.subheader("🗄 Database")

    db = Database()

    try:
        result = db.health_check()

        if result.get("connected"):
            st.success("Database Connected")
        else:
            st.error("Database Disconnected")

        st.json(result)

    except Exception as ex:
        st.exception(ex)


def render_storage() -> None:
    """
    Storage information.
    """

    st.subheader("📁 Storage")

    storage = Storage()

    try:
        result = storage.health_check()

        st.json(result)

    except Exception as ex:
        st.exception(ex)


def render_disk() -> None:
    """
    Disk usage.
    """

    st.subheader("💾 Disk")

    storage = Storage()

    try:
        result = storage.disk()

        st.json(result)

    except Exception as ex:
        st.exception(ex)