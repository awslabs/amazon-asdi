NOAA Integrated Surface Database (ISD) Example
==============================================


This example uses AWS CloudFormation to create an Amazon SageMaker Jupyter Notebook and AWS Glue tables so that it is possible to query the ISD dataset. The example currently creates partitions for the years 2018 and 2019 but is extensible to the entire dataset.

[![cloudformation-launch-stack](cloudformation/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=NOAAISD&templateURL=hhttps://s3.amazonaws.com/docs.opendata.aws/cloudformation/isd.yaml)

The Jupyter notebook shows an example of how to query Amazon Athena using PyAthena enabling analysis of the ISD dataset entirely from within the notebook.