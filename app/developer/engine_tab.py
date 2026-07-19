from datetime import datetime

import streamlit as st

from app.engines import (
    DownloaderEngine,
    ExtractorEngine,
)
from app.models import DownloadJob


def render_engine_tab() -> None:

    st.subheader("⚙ Engine")

    store = st.text_input(
        "Store Code",
        value="TSIS"
    )

    trx_date = st.date_input(
        "Transaction Date",
        value=datetime.today()
    )

    #
    # Create Job
    #

    job = DownloadJob(

        store=store,

        trx_date=datetime.combine(
            trx_date,
            datetime.min.time()
        )

    )

    #
    # Downloader
    #

    if st.button(
        "Run Downloader",
        key="run_downloader"
    ):

        engine = DownloaderEngine()

        result = engine.run(job)

        if result.success:
            st.success(result.message)
        else:
            st.error(result.message)

        st.json({
            "Remote File": job.remote_file,
            "Local File": str(job.local_file),
            "Status": job.status.value,
            "Duration": job.duration,
        })

    #
    # Extractor
    #

    if st.button(
        "Run Extractor",
        key="run_extractor"
    ):

        engine = ExtractorEngine()

        result = engine.run(job)

        if result.success:
            st.success(result.message)
        else:
            st.error(result.message)

        st.write(result.data)