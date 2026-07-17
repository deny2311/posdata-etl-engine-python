import streamlit as st


def render_application(data):

    st.header("Application")

    col1, col2, col3 = st.columns(3)

    col1.metric("Application", data["name"])
    col2.metric("Version", data["version"])
    col3.metric("Environment", data["environment"])


def render_python(data):

    st.divider()

    st.header("Python")

    col1, col2 = st.columns(2)

    col1.metric("Version", data["version"])
    col2.metric("Platform", data["platform"])

    with st.expander("Detail"):
        st.code(data["detail"])


def render_database(data):

    st.divider()

    st.header("Database")

    if data["connected"]:

        st.success("🟢 Connected")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Host")
            st.write(data["host"])

            st.write("Database")
            st.write(data["database"])

            st.write("User")
            st.write(data["user"])

        with col2:
            st.write("Version")
            st.write(data["version"])

            st.write("Charset")
            st.write(data["charset"])

    else:

        st.error(data["error"])


def render_storage(data):

    st.divider()

    st.header("Storage")

    col1, col2 = st.columns(2)

    items = list(data.items())

    half = (len(items)+1)//2

    for name, value in items[:half]:

        icon = "🟢" if value["exists"] and value["write"] else "🔴"

        col1.write(f"{icon} {name}")

    for name, value in items[half:]:

        icon = "🟢" if value["exists"] and value["write"] else "🔴"

        col2.write(f"{icon} {name}")


def render_disk(data):

    st.divider()

    st.header("Disk")

    gb = 1024**3

    total = data["total"]/gb
    used = data["used"]/gb
    free = data["free"]/gb

    col1, col2, col3 = st.columns(3)

    col1.metric("Total", f"{total:.2f} GB")
    col2.metric("Used", f"{used:.2f} GB")
    col3.metric("Free", f"{free:.2f} GB")

    st.progress(used/total)