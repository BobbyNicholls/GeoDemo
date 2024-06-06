import boto3
import sagemaker

session = sagemaker.Session(boto3.Session(region_name="eu-west-2"))
role = sagemaker.get_execution_role()
session = sagemaker.Session()
container = sagemaker.image_uris.retrieve(
    framework="xgboost", region=session.boto_region_name, version="1.2-1"
)

xgb = sagemaker.estimator.Estimator(
    container,
    role,
    instance_count=1,
    instance_type="ml.m5.xlarge",
    output_path="s3://time-series-geo-data/model-output",
    sagemaker_session=session,
)
xgb.set_hyperparameters(objective="reg:squarederror.", num_round=3)
xgb.fit({"train": "s3://time-series-geo-data/bustard.libsvm"})
