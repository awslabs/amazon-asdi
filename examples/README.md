# Amazon Sustainability Data Initiative Examples

<p align="center">
The Amazon Sustainability Data Initiative (ASDI) seeks to accelerate sustainability research and innovation by minimizing the cost and time required to acquire and analyze large sustainability datasets. ASDI supports innovators and researchers with the data, tools, and technical expertise they need to move sustainability to the next level.
</p>

This folder contains examples, and supporting material for the [Amazon Sustainability Data Initiative (ASDI)](https://amazonsdi.com/), an initiative to provide access to large datasets in the cloud to help researchers and innovators address a wide range of sustainability challenges.

## Examples 

These are examples of how to set up infrastructure on AWS for working with ASDI datasets. 

Example    | AWS Services    | ASDI Datasets    | Description
:--------- | :------------   | :--------------  | :------------
[Simple CMIP6](cmip6) | Amazon SageMaker Notebooks | CMIP6 | Example of how to filter ensemble members in CMIP6, plot a spatial map, and extract a time series of air temperature
[Fargate Dask Cluster](dask) | AWS Fargate, Amazon SageMaker Notebooks | CMIP6, ERA5, GOES-16 | Example of how to set up a Dask cluster and Jupyter notebook for scalable analysis of datasets
[GFS to Parquet Conversion](noaa-gfs-parquet) | Amazon SageMaker Notebooks, Amazon Athena, AWS Glue | GFS | Example of how to subset GFS grib2 files by variable, and convert them to the parquet file format for querying
[GHCN Growing Degree Days](noaa-ghcn-gdd) | Amazon Athena, AWS Glue | GHCN | Example of how to query the NOAA GHCN data using Amazon Athena to return the number of growing degree days
[ISD Example](noaa-isd) | Amazon SageMaker Notebooks, Amazon Athena, AWS Glue | ISD | An example of how to work with the NOAA Integrated Surface Database using Jupyter notebooks
[Julia GOES-16](goes16-precip-julia) | Amazon EC2 | GOES-16 | An example showing multi-cpu computation against the GOES-16 precipitation files using Julia
[OpenAQ Example](openaq) | Amazon Athena, AWS Glue | OpenAQ | Creates AWS Glue tables for easily querying the OpenAQ data in Amazon Athena