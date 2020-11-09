NOAA Global Forecast System (GFS) Conversion to Parquet Example
==============================================


This example uses AWS CloudFormation to create an Amazon SageMaker Jupyter Notebook. From the notebook, the GFS grib2 files are processed converting the 2-m air temperature into Parquet, saving them to S3, and finally querying them with Athena.

[![cloudformation-launch-stack](cloudformation/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=GFS&templateURL=https://s3.amazonaws.com/docs.opendata.aws/cloudformation/gfs-parquet.yaml)

