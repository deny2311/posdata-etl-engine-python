import streamlit as st

from app.repositories import TransferRepository
from app.services.transfer import TransferFactory


def render_transfer_tab() -> None:
    """
    Transfer developer page.
    """

    st.subheader("🌐 Transfer")

    store = st.text_input(
        "Store",
        value="TSIS"
    )

    if st.button(
        "Connect",
        key="transfer_connect"
    ):

        try:

            repo = TransferRepository()

            config = repo.get(store)

            service = TransferFactory.create(
                config
            )

            service.connect()

            st.success("Connected")

            st.write("Transfer")

            st.json({

                "Name": config.name,

                "Protocol": str(config.protocol),

                "Host": config.host,

                "User": config.username,

                "Remote Path": config.remote_path

            })

            service.disconnect()

        except Exception as ex:

            st.exception(ex)