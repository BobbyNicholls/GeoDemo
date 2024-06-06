import json

import boto3


def lambda_handler(event, context):
    print(f"event: {json.dumps(event)}")

    body = json.loads(event.get("body", "{}"))
    origin_latitude = body.get("origin_latitude")
    origin_longitude = body.get("origin_longitude")
    destination_latitude = body.get("destination_latitude")
    destination_longitude = body.get("destination_longitude")

    s3 = boto3.client("s3")
    geo_data = (
        s3.get_object(Bucket="time-series-geo-data", Key="bustard_small.csv")["Body"]
        .read()
        .decode("utf-8")
    )
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "param1": origin_latitude,
                "param2": origin_longitude,
                "param3": destination_latitude,
                "param4": destination_longitude,
                "geo_data": geo_data,
            }
        ),
    }
