import streamlit as st
import folium
from streamlit_folium import folium_static

# Set the title of the app
st.title('Interactive World Map')
the_downs = [51.47168, -2.62186]
bristol = [51.4545, -2.5879]

# Create a folium map centered at Bristol
m = folium.Map(location=the_downs, zoom_start=13)

# Add a marker at Bristol
folium.Marker(bristol, popup='Bristol').add_to(m)
folium.Marker(the_downs, popup='Park').add_to(m)

# Display the map in Streamlit
folium_static(m)
