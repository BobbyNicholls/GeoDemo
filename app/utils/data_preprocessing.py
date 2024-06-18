import pandas as pd


def clean_geo_data(df: pd.DataFrame, dates) -> pd.DataFrame:
    df["UTC_timestamp"] = pd.to_datetime(df["UTC_timestamp"])
    df["date"] = [str(timestamp.date()) for timestamp in df["UTC_timestamp"]]
    df = df[df["date"].isin(dates)].sort_values("UTC_timestamp")
    df = df[df["Latitude"] != 0]
    return df
