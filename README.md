## Basic outline

## Changelog
- 1.0.2 added sagemaker geospatial ML model training and deployment 
- 1.0.1 added time series geo-spatial animation to map

## Things I would do if I had more time / this was not a demo
 - AWS CodePipeline to version control my lambda functions and other code, also to do CI/CD
 - Use poetry manage package versioning to ensure compatibility
 - Dockerise / containerise my deployments, integrate with poetry
 - Move from trunk development to having an intermediary 'dev' / 'development' branch, maybe even 'uat' if needed.
 - Integrate with backend databases and S3 buckets
 - Set up unit tests, ensure sufficient coverage
 - Add shift-left pipeline, or use Quodana / Sonar / etc
 - Add documentation, including docstrings in functions
 - Add architecture diagram
 - Type enforcement and assertions around the API to handle bad data / requests well
 - Host on a proper domain with sso etc
 - Model training and deployment should not be in the same repo
