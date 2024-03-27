import streamlit as st
from functions import run_soda_scan
import pandas as pd

scan_df = run_soda_scan('snowflake', 'test_scan')
st.dataframe(scan_df, hide_index=True)