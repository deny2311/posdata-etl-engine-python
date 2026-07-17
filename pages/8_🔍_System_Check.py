import streamlit as st

from app.services.system_check_service import SystemCheckService

from app.ui.render_system_check import (
    render_application,
    render_python,
    render_database,
    render_storage,
    render_disk,
)

st.title("🔎 System Check")

service = SystemCheckService()

result = service.run()

render_application(result["application"])
render_python(result["python"])
render_database(result["database"])
render_storage(result["storage"])
render_disk(result["disk"])