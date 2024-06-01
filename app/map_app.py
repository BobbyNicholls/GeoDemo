import streamlit as st
import folium
from streamlit_folium import folium_static

# Set the title of the app
st.title('Interactive World Map')
avon_way = [51.48068, -2.64217]
bristol = [51.4545, -2.5879]
# Create a folium map centered at Bristol
m = folium.Map(location=avon_way, zoom_start=13)

# Add a marker at Bristol
folium.Marker(bristol, popup='Bristol').add_to(m)
folium.Marker(avon_way, popup='Me').add_to(m)


# Display the map in Streamlit
folium_static(m)
