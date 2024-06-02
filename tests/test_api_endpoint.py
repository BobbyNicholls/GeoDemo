import requests
import json

url = "https://2gs5g97rxd.execute-api.eu-west-2.amazonaws.com/sandbox"
payload = {
    "param1": "first",
    "param2": "second",
    "param3": "third",
    "param4": "fourth"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print("Status Code:", response.status_code)
print("Response Body:", response.json())
