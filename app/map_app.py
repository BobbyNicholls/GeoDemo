import json
from io import StringIO
from typing import Dict

import folium
import pandas as pd
import requests
import streamlit as st
from streamlit_folium import folium_static
from utils.geo_animation import get_time_stamped_geo_json


def get_geo_data(
    payload: Dict[str, str],
    url: str = "https://2gs5g97rxd.execute-api.eu-west-2.amazonaws.com/sandbox",
    request_from_endpoint: bool = False,
) -> pd.DataFrame:
    if request_from_endpoint:
        response = requests.post(url, data=json.dumps(payload))
        if response.status_code == 200:
            return pd.read_csv(StringIO(response.json()["geo_data"]))

        raise ValueError(f"API failed with status code {response.status_code}")

    return pd.read_csv("C:/dev/geo_birds/data/bustard.csv")


st.title("Bustard Map App")
st.sidebar.title("Input date you want to review:")
selected_date = str(
    st.sidebar.date_input("Select a date", pd.to_datetime("2020-03-01").date())
)

if st.sidebar.button("Submit"):
    payload = {"date": str(selected_date)}
    geo_data = get_geo_data(payload)
    geo_data["date"] = [
        str(pd.to_datetime(timestamp).date()) for timestamp in geo_data["UTC_timestamp"]
    ]
    geo_data = geo_data[geo_data["date"] == selected_date].sort_values("UTC_timestamp")
    if len(geo_data) > 0:
        start_latitude = geo_data["Latitude"].iloc[0]
        start_longitude = geo_data["Longitude"].iloc[0]
        st.write("Interactive World Map")
        folium_map = folium.Map(location=[start_latitude, start_longitude], zoom_start=16)
        get_time_stamped_geo_json(geo_data).add_to(folium_map)
        folium_static(folium_map, width=1050, height=750)
    else:
        st.write("Could not find data for that date")

else:
    st.write("Please enter values in the sidebar and click 'Submit'.")
