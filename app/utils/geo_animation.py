"""functions for getting animated mapping functions"""

import pandas as pd
from folium.plugins import TimestampedGeoJson


def create_feature(bird_data: pd.DataFrame):
    birds = bird_data["device_id"].unique()
    colors = [
        "red",
        "blue",
        "green",
        "orange",
        "purple",
        "darkred",
        "darkblue",
        "darkgreen",
        "cadetblue",
        "gray",
    ]
    color_map = {bird: colors[i % len(colors)] for i, bird in enumerate(birds)}
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": list(zip(bird_data["Longitude"], bird_data["Latitude"])),
        },
        "properties": {
            "times": list(bird_data["UTC_timestamp"]),
            "style": {"color": color_map[bird_data["device_id"].iloc[0]]},
        },
    }
    return feature


def get_time_stamped_geo_json(data: pd.DataFrame):
    birds = data["device_id"].unique()
    features = [create_feature(data[data["device_id"] == bird]) for bird in birds]
    return TimestampedGeoJson(
        {"type": "FeatureCollection", "features": features},
        period="PT1M",
        add_last_point=True,
        auto_play=True,
        loop=True,
    )
