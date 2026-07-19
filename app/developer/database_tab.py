import streamlit as st

from app.core.database import Database


def render_database_tab() -> None:
    """
    Database developer page.
    """

    st.subheader("🗄 Database")

    if st.button("Test Database", key="db_test"):

        db = Database()

        result = db.health_check()

        if result["connected"]:

            st.success("Database Connected")

        else:

            st.error("Database Failed")

        st.json(result)