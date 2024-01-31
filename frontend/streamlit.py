import streamlit as st
import pandas as pd
import requests

# Define the Flask API endpoints
degree_api_url = "http://localhost:5000/degree"
timestamp_api_url = "http://localhost:5000/timestamp"

# Fetch data from the API
degree_data = requests.get(degree_api_url).json()
timestamp_data = requests.get(timestamp_api_url).json()


# Streamlit app
st.title("Data Visualization")
st.header(degree_data)
st.header(timestamp_data)