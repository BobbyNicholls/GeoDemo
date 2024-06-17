"""functions for getting animated mapping functions"""

import pandas as pd
from folium.plugins import TimestampedGeoJson


def create_feature(feature_data: pd.DataFrame, offset):
    feature = {
        "type": "Feature",
        "geometry": {
            "type": "LineString",
            "coordinates": list(
                zip(feature_data["Longitude"], feature_data["Latitude"])
            ),
        },
        "properties": {
            "times": list((feature_data["UTC_timestamp"] - pd.DateOffset(days=offset)).astype(str)),
            "style": {"color": "Blue"},
        },
    }
    return feature


def get_time_stamped_geo_json(data: pd.DataFrame):
    dates = data["date"].unique()
    features = [
        create_feature(data[data["date"] == date], offset)
        for offset, date in enumerate(dates)
    ]
    return TimestampedGeoJson(
        {"type": "FeatureCollection", "features": features},
        period="PT1M",
        add_last_point=True,
        auto_play=True,
        loop=True,
    )
