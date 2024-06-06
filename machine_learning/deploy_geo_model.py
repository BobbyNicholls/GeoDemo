import boto3
import sagemaker
from sagemaker.model import Model

region_name = "eu-west-2"
role = sagemaker.get_execution_role()
session = sagemaker.Session(boto3.Session(region_name=region_name))
model_artifact = "s3://time-series-geo-data/model-output/sagemaker-xgboost-2024-06-05-19-21-30-670/output/model.tar.gz"
container = sagemaker.image_uris.retrieve("xgboost", region_name, version="1.2-1")

model = Model(
    image_uri=container, model_data=model_artifact, role=role, sagemaker_session=session
)
predictor = model.deploy(
    initial_instance_count=1,
    instance_type="ml.t2.medium",
    endpoint_name="geo-model-endpoint",
)
