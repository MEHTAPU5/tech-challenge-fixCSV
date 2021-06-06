import streamlit as st
import os
import pandas as pd

"""
## Tech Challenge by Team 2 :
#  Fix CSV encoding 
"""
inputCSV =  st.file_uploader("Upload CSV", type=['csv','xlsx'], accept_multiple_files=False, key="inputCSV", help="Input CSV file to fix encoding issues")
if inputCSV is not None:
    
    st.write("### Uploaded File : ",inputCSV.name)
    df = pd.read_csv(inputCSV, encoding='Windows-1252')
    st.write("## File as CSV: ")
    st.write(df)
    st.write("## File as a Streamlit Table:")
    
    st.table(df)