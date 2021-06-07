import streamlit as st
import os
import pandas as pd
import chardet
import base64

"""
## Tech Challenge by Team 2 :
#  Fix CSV encoding 
"""


def get_table_download_link(df):
    csv = df.to_csv(encoding='utf-8-sig', index=False)
    # encoding the processed CSV with utf-8-sig and making it available for download
    enc = csv.encode('utf-8-sig').decode()
    href = f'<a href="data:file/csv;enc,{enc}" download="fixedCSV.csv" target="_blank"><button style="padding: 5px; color: white; background: #73bcf0; border: 1px white; outline: 1px white;">DOWNLOAD FIXED CSV FILE</button></a>'
    return href


inputCSV = st.file_uploader("Upload CSV", type=[
                            'csv'], accept_multiple_files=False, key="inputCSV", help="Input CSV file to fix encoding issues")
if inputCSV is not None:

    st.write("### Uploaded File : ", inputCSV.name)

    # after-encoding
    df = pd.read_csv(inputCSV, encoding='utf-8')
    st.write("## Fixed CSV File :")
    st.table(df)
    #df.to_csv("fixedCSV.csv", encoding='utf-8-sig', index=False)
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
