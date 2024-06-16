import json
from datetime import datetime
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
) -> pd.DataFrame:
    response = requests.post(url, data=json.dumps(payload))
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.json()["geo_data"]))

    raise ValueError(f"API failed with status code {response.status_code}")


st.title("Simple Map App")
st.sidebar.title("Input Lat/Longs:")
selected_date = st.sidebar.date_input("Select a date", datetime.now())

# the_downs = [51.47168, -2.62186]
# bristol = [51.4545, -2.5879]
# germany_origin = [52.20031, 12.6059]
germany_destination = [52.18538, 12.67741]

if st.sidebar.button("Submit"):
    payload = {"date": str(selected_date)}
    geo_data = get_geo_data(payload)
    geo_data["date"] = [str(pd.to_datetime(date).date()) for date in geo_data["UTC_timestamp"]]
    geo_data = geo_data[geo_data["date"] == selected_date].sort_values("UTC_timestamp")
    start_latitude = geo_data["Latitude"].iloc[0]
    start_longitude = geo_data["Longitude"].iloc[0]
    st.write("Interactive World Map")
    folium_map = folium.Map(location=[start_latitude, start_longitude], zoom_start=10)
    get_time_stamped_geo_json(pd.read_csv(StringIO(geo_data["geo_data"]))).add_to(
        folium_map
    )
    folium_static(folium_map, width=1050, height=750)

else:
    st.write("Please enter values in the sidebar and click 'Submit'.")
