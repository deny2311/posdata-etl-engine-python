from datetime import datetime

import streamlit as st

from app.engines import DownloaderEngine
from app.models import DownloadJob


def render() -> None:
    """
    Render Downloader page.
    """

    st.title("📥 Downloader")

    st.caption(
        "Download POS data from remote transfer server."
    )

    st.divider()

    # =====================================================
    # INPUT
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        store = st.text_input(
            "Store",
            value="TSIS"
        )

    with col2:

        trx_date = st.date_input(
            "Transaction Date",
            value=datetime.today()
        )

    st.divider()

    # =====================================================
    # ACTION
    # =====================================================

    if st.button(
        "🚀 Start Download",
        type="primary",
        use_container_width=True
    ):

        job = DownloadJob(
            store=store.strip().upper(),
            trx_date=datetime.combine(
                trx_date,
                datetime.min.time()
            )
        )

        engine = DownloaderEngine()

        with st.spinner("Running downloader..."):

            result = engine.run(job)

        if result.success:

            st.success(result.message)

        else:

            st.error(result.message)

        st.divider()

        st.subheader("Download Job")

        c1, c2 = st.columns(2)

        with c1:

            st.metric(
                "Store",
                job.store
            )

            st.metric(
                "Status",
                job.status.value
            )

            st.metric(
                "Transfer",
                job.transfer_name or "-"
            )

            st.metric(
                "Protocol",
                str(job.protocol or "-")
            )

        with c2:

            st.text_input(
                "Remote File",
                value=job.remote_file,
                disabled=True
            )

            st.text_input(
                "Local File",
                value=str(job.local_file or ""),
                disabled=True
            )

            st.metric(
                "Duration",
                f"{job.duration:.2f} sec"
            )

        if job.error_message:

            st.error(job.error_message)