Coupled Model Intercomparison Project Phase 6 (CMIP6) Examples
==============================================


These example use AWS CloudFormation to create an Amazon SageMaker Jupyter Notebook instance with the appropriate Python libraries installed (zarr, xarray, dask, intake) for working with the CMIP6 datasets.

[![cloudformation-launch-stack](cloudformation/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=us-west-2#/stacks/new?stackName=CMIP6&templateURL=https://s3.amazonaws.com/docs.opendata.aws/cloudformation/cmip6.yaml)

The Jupyter notebook `cmip6_airtemperature.ipynb` shows an example of how to query the intake-esm catalog for CMIP6 and select the appropriate ensemble members for a specific institution. Then it plots the mean difference in temperature at the end of one of the scenarios from the beginning showing how the temperature is changing over the 100 year period. The notebook also shows how to extract the time series of temperature at a location for all of the scenarios and plot that as well. 
