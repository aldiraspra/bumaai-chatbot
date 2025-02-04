"""
This module contains the code for the Admin app of the Chat with your data Solution Accelerator.
"""

import os
import logging
import sys
import streamlit as st
from azure.monitor.opentelemetry import configure_azure_monitor

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

logging.captureWarnings(True)
logging.basicConfig(level=os.getenv("LOGLEVEL", "INFO").upper())
# Raising the azure log level to WARN as it is too verbose
# https://github.com/Azure/azure-sdk-for-python/issues/9422
logging.getLogger("azure").setLevel(os.environ.get("LOGLEVEL_AZURE", "WARN").upper())
# We cannot use EnvHelper here as Application Insights needs to be configured first
# for instrumentation to work correctly
if os.getenv("APPLICATIONINSIGHTS_ENABLED", "false").lower() == "true":
    configure_azure_monitor()

logger = logging.getLogger(__name__)
logger.debug("Starting Web")


st.set_page_config(
    page_title="BUMA AI",
    page_icon=os.path.join("images", "images.jpg"),
    layout="wide",
    menu_items=None,
)


def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Load the common CSS
load_css("pages/common.css")


col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.image(os.path.join("images", "buma.png"))

st.write("#BUMA AI")

st.write(
    """
         * If you want to ingest data, then use the `Ingest Data` tab
         """
)
