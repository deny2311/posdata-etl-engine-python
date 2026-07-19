import streamlit as st

from app.core.storage import Storage


def render_storage_tab() -> None:
    """
    Storage developer page.
    """

    st.subheader("📂 Storage")

    storage = Storage()

    if st.button("Create Folder", key="storage_create"):

        storage.create()

        st.success("Folder checked.")

    if st.button("Health Check", key="storage_health"):

        st.json(
            storage.health_check()
        )

    if st.button("Disk Usage", key="disk_usage"):

        st.json(
            storage.disk()
        )