import pandas as pd

import requests
import json
from io import StringIO

url = "https://2gs5g97rxd.execute-api.eu-west-2.amazonaws.com/sandbox"
payload = {
    "origin_latitude": 51.47168,
    "origin_longitude": -2.62186,
    "destination_latitude": 51.4545,
    "destination_longitude": -2.5879,
}
# headers = {
#     "Content-Type": "application/json"
# }

# response = requests.post(url, headers=headers, data=json.dumps(payload))
response = requests.post(url, data=json.dumps(payload))
print("Status Code:", response.status_code)
print("Response Body:", response.json())

df = pd.read_csv(StringIO(response.json()["geo_data"]))
