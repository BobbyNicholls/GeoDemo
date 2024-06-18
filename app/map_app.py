import folium
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
from utils.data_transfer import get_geo_data
from utils.geo_animation import get_time_stamped_geo_json

st.title("Bustard Map App")
st.sidebar.title(
    "Input date you want to review and the number of consecutive days to compare it with:"
)
selected_date = st.sidebar.date_input(
    "Select a date", pd.to_datetime("2020-03-01").date()
)
number_of_days = st.sidebar.number_input("Number of days", min_value=1, max_value=30)

if st.sidebar.button("Submit"):
    selected_dates = pd.date_range(
        start=selected_date, periods=number_of_days, freq="D"
    ).astype(str)
    payload = {"date": str(selected_dates[0])}
    geo_data = get_geo_data(payload)
    geo_data["UTC_timestamp"] = pd.to_datetime(geo_data["UTC_timestamp"])
    geo_data["date"] = [
        str(timestamp.date()) for timestamp in geo_data["UTC_timestamp"]
    ]
    geo_data = geo_data[geo_data["date"].isin(selected_dates)].sort_values(
        "UTC_timestamp"
    )
    if len(geo_data) > 0:
        start_latitude = geo_data["Latitude"].iloc[0]
        start_longitude = geo_data["Longitude"].iloc[0]
        st.write(f"Movements on {', '.join(selected_dates)}")
        folium_map = folium.Map(
            location=[start_latitude, start_longitude], zoom_start=16
        )
        get_time_stamped_geo_json(geo_data).add_to(folium_map)
        folium_static(folium_map, width=1050, height=750)
    else:
        st.write("Could not find data for that date")

else:
    st.write("Please enter values in the sidebar and click 'Submit'.")
