import json
from typing import Dict

import folium
import requests
import streamlit as st
from streamlit_folium import folium_static

from utils.geo_animation import get_time_stamped_geo_json


def get_lat_longs(
    payload: Dict[str, float],
    url: str = "https://2gs5g97rxd.execute-api.eu-west-2.amazonaws.com/sandbox",
):
    response = requests.post(url, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()

    raise ValueError(f"API failed with status code {response.status_code}")


st.title("Simple Map App")
st.sidebar.title("Input Lat/Longs:")
origin_latitude = st.sidebar.text_input("Enter origin latitude:", "")
origin_longitude = st.sidebar.text_input("Enter origin longitude:", "")
destination_latitude = st.sidebar.text_input("Enter destination latitude:", "")
destination_longitude = st.sidebar.text_input("Enter destination longitude:", "")

# the_downs = [51.47168, -2.62186]
# bristol = [51.4545, -2.5879]
# germany_origin = [52.20031, 12.6059]
# germany_destination = [52.18538, 12.67741]

if st.sidebar.button("Submit"):
    payload = {
        "origin_latitude": origin_latitude,
        "origin_longitude": origin_longitude,
        "destination_latitude": destination_latitude,
        "destination_longitude": destination_longitude,
    }
    lat_longs = get_lat_longs(payload)
    origin = [lat_longs["param1"], lat_longs["param2"]]
    destination = [lat_longs["param3"], lat_longs["param4"]]
    st.title("Interactive World Map")
    folium_map = folium.Map(location=origin, zoom_start=10)
    folium.Marker(origin, popup="Origin").add_to(folium_map)
    folium.Marker(destination, popup="Destination").add_to(folium_map)
    get_time_stamped_geo_json().add_to(folium_map)
    folium_static(folium_map)

else:
    st.write("Please enter values in the sidebar and click 'Submit'.")
