import streamlit as st
import requests


def fetch_message():
    response = requests.get('https://2gs5g97rxd.execute-api.eu-west-2.amazonaws.com/sandbox')
    if response.status_code == 200:
        return response.json()
    return "Error fetching data"


st.title("Message from Serverless API")
message = fetch_message()
st.write(message)
