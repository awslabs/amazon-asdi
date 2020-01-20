NOAA Integrated Surface Database (ISD) Example
==============================================


This example uses AWS CloudFormation to create an Amazon SageMaker Jupyter Notebook and AWS Glue tables so that it is possible to query the ISD dataset. The example currently creates partitions for the years 2018 and 2019 but is extensible to the entire dataset.


The Jupyter notebook shows an example of how to query Amazon Athena using PyAthena enabling analysis of the ISD dataset entirely from within the notebook.