NOAA Integrated Surface Database (ISD) Example
==============================================


This example uses AWS CloudFormation to create an Amazon SageMaker Jupyter Notebook with Julia v1.4.2.

[![cloudformation-launch-stack](cloudformation/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=NOAAISD&templateURL=https://s3.amazonaws.com/docs.opendata.aws/cloudformation/julia-1.4.2-notebook.yaml)

The Jupyter notebook shows an example of how to efficiently sum values stored in a large number of NetCDF files housed on Amazon S3 using the [Julia programming language](https://julialang.org/).
