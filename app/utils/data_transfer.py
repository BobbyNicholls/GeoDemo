import json
from io import StringIO
from typing import Dict

import requests


def get_geo_data(
    request_payload: Dict[str, str],
    url: str = "https://2gs5g97rxd.execute-api.eu-west-2.amazonaws.com/sandbox",
    request_from_endpoint: bool = False,
) -> pd.DataFrame:
    if request_from_endpoint:
        response = requests.post(url, data=json.dumps(request_payload))
        if response.status_code == 200:
            return pd.read_csv(StringIO(response.json()["geo_data"]))

        raise ValueError(f"API failed with status code {response.status_code}")

    return pd.read_csv("C:/dev/geo_birds/data/bustard.csv")
