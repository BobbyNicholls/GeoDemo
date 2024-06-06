import boto3

sagemaker_client = boto3.client("sagemaker-runtime")
s3_client = boto3.client("s3")
request_data = (
    s3_client.get_object(Bucket="time-series-geo-data", Key="request_sample.libsvm")[
        "Body"
    ]
    .read()
    .decode("utf-8")
)
response = sagemaker_client.invoke_endpoint(
    EndpointName="geo-model-endpoint", ContentType="text/libsvm", Body=request_data
)
result = response["Body"].read().decode("utf-8")
print(f"Prediction: {result}")
