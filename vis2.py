import streamlit as st
import pandas as pd
import numpy as np

st.title("Simple Sales Data Dashbpard - by Peter")

DATA_URL = pd.read_csv('sales_data.csv')


st.write(DATA_URL)

st.bar_chart(DATA_URL, x='Region', y='Sales')
