import folium
import requests
import streamlit as st
from streamlit_folium import folium_static


def fetch_message():
    response = requests.get('https://2gs5g97rxd.execute-api.eu-west-2.amazonaws.com/sandbox/get')
    if response.status_code == 200:
        return response.json()["body"]
    return "Error fetching data"


st.title('Interactive World Map')
st.write(fetch_message())
the_downs = [51.47168, -2.62186]
bristol = [51.4545, -2.5879]

m = folium.Map(location=the_downs, zoom_start=13)
folium.Marker(bristol, popup='Bristol').add_to(m)
folium.Marker(the_downs, popup='Park').add_to(m)

# Display the map in Streamlit
folium_static(m)
