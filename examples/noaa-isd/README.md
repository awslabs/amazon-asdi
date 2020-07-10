NOAA Integrated Surface Database (ISD) Example
==============================================


This example uses AWS CloudFormation to create an Amazon SageMaker Jupyter Notebook and AWS Glue tables so that it is possible to query the ISD dataset.

[![cloudformation-launch-stack](cloudformation/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=NOAAISD&templateURL=https://s3.amazonaws.com/docs.opendata.aws/cloudformation/isd.yaml)

The Jupyter notebook shows an example of how to query Amazon Athena using PyAthena enabling analysis of the ISD dataset entirely from within the notebook.
