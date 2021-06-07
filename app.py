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
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="fixedCSV.csv" target="_blank"><button style="padding: 5px; color: white; background: #73bcf0; border: 1px white; outline: 1px white;">DOWNLOAD FIXED CSV FILE</button></a>'
    return href

inputCSV =  st.file_uploader("Upload CSV", type=['csv'], accept_multiple_files=False, key="inputCSV", help="Input CSV file to fix encoding issues")
if inputCSV is not None:
    
    st.write("### Uploaded File : ",inputCSV.name)
    df = pd.read_csv(inputCSV)
    st.write("## File as CSV: ")
    st.write(df)
    st.write("## File as a Streamlit Table:")
    st.table(df)
    st.markdown(get_table_download_link(df), unsafe_allow_html=True)
    