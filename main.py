import streamlit as st
import pandas as pd
from datetime import datetime
from datetime import timedelta
from soda.scan import Scan
from functions import run_soda_scan


tab1, tab2, tab3 = st.tabs(["All Apps", "Snowflake", "Postgres"])

#App home page
with tab1:
    st.title("Data Quality Checks Using Soda Core :white_check_mark:")
    st.caption("Select a dataset on the left to get started")
    st.header("Showing data quality checks against all applications")
    current_logs = pd.read_csv('soda_logs.csv')
    st.dataframe(current_logs, hide_index=True)

#Snowflake checks
with tab2:
    st.header("Run data quality checks against Snowflake")
    snowflake_button = st.button('Click here to run Snowflake checks')
    if snowflake_button:
        scan_df = run_soda_scan('snowflake', 'test_scan')
        filtered_df = scan_df[scan_df['application'] == 'snowflake']
        st.dataframe(filtered_df, hide_index=True)
    else:
        current_logs = pd.read_csv('soda_logs.csv')
        df = current_logs[(current_logs['application'] == 'snowflake')]
        st.dataframe(df, hide_index=True)

#Postgres checks
with tab3:
    st.header("Run data quality checks against Postgres")
    postgres_button = st.button('Click here to run Postgres checks')
    if postgres_button:
        scan_df = run_soda_scan('postgres', 'test_scan')
        filtered_df = scan_df[scan_df['application'] == 'postgres']
        st.dataframe(filtered_df, hide_index=True)
    else:
        current_logs = pd.read_csv('soda_logs.csv')
        df = current_logs[(current_logs['application'] == 'postgres')]
        st.dataframe(df, hide_index=True)


