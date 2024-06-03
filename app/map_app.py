import json
from typing import Dict

import folium
import requests
import streamlit as st
from streamlit_folium import folium_static


def get_lat_longs(
    payload: Dict[str, float],
    url: str = "https://2gs5g97rxd.execute-api.eu-west-2.amazonaws.com/sandbox",
):
    response = requests.post(url, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()

    raise ValueError(f"API failed with status code {response.status_code}")


the_downs = [51.47168, -2.62186]
bristol = [51.4545, -2.5879]
payload = {
    "origin_latitude": the_downs[0],
    "origin_longitude": the_downs[1],
    "destination_latitude": bristol[0],
    "destination_longitude": bristol[1],
}
lat_longs = get_lat_longs(payload)

st.title("Interactive World Map")
m = folium.Map(location=the_downs, zoom_start=13)
folium.Marker([lat_longs["param1"], lat_longs["param2"]], popup="Park").add_to(m)
folium.Marker([lat_longs["param3"], lat_longs["param4"]], popup="Bristol").add_to(m)

# Display the map in Streamlit
folium_static(m)
