from datetime import datetime

import streamlit as st

from app.engines import DownloaderEngine
from app.models import DownloadJob


def render_engine_tab() -> None:
    """
    Engine developer page.
    """

    st.subheader("⚙ Engine")

    store = st.text_input(
        "Store Code",
        value="TSIS"
    )

    trx_date = st.date_input(
        "Transaction Date",
        value=datetime.today()
    )

    if st.button(
        "Run Downloader",
        key="engine_run"
    ):

        job = DownloadJob(

            store=store,

            trx_date=datetime.combine(
                trx_date,
                datetime.min.time()
            )

        )

        engine = DownloaderEngine()

        result = engine.run(job)

        if result.success:

            st.success(result.message)

        else:

            st.error(result.message)

        st.json({

            "Store": job.store,

            "Transfer": job.transfer_name,

            "Protocol": str(job.protocol),

            "Remote File": job.remote_file,

            "Local File": str(job.local_file),

            "Status": job.status.value,

            "Duration": job.duration

        })