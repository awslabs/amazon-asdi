# Amazon Sustainability Data Initiative

<p align="center">
The Amazon Sustainability Data Initiative (ASDI) seeks to accelerate sustainability research and innovation by minimizing the cost and time required to acquire and analyze large sustainability datasets. ASDI supports innovators and researchers with the data, tools, and technical expertise they need to move sustainability to the next level.
</p>

This repo contains docs, examples, and supporting material for the [Amazon Sustainability Data Initiative (ASDI)](https://amazonsdi.com/), an initiative to provide access to large datasets in the cloud to help researchers and innovators address a wide range of sustainability challenges.

## Working with data in ASDI

### Getting started

The [Getting Started with the Amazon Sustainability Data Initiative (ASDI)](getting-started-guide.md) has information on setuping up an AWS account, relevant AWS services, accessing the datasets, and an overview of AWS basics for working with data.

### Finding ASDI datasets

Datasets from ASDI are listed on the [Registry of Open Data on AWS's ASDI collaboration page](https://registry.opendata.aws/collab/asdi/)

### ASDI workshops and events

Event  | Description
:----- | :------------
[Code Green 2019](events/code-green-2019) | Code Green is both a hackathon and workshop, originally created for re:Invent 2019, centered around exploring Amazon Sustainability Data Initiative (ASDI) datasets.
[Code Green 2021](events/code-green-2021) | Code Green is both a hackathon and workshop. This version was created for re:Invent 2021, and centers around exploring Amazon Sustainability Data Initiative (ASDI) and AWS Data Exchange (ADX) datasets.


### Examples 

These are examples of how to set up infrastructure on AWS for working with ASDI datasets. 

Example    | AWS Services    | ASDI Datasets    | Description
:--------- | :------------   | :--------------  | :------------
[Simple CMIP6](examples/cmip6) | Amazon SageMaker Notebooks | CMIP6 | Example of how to filter ensemble members in CMIP6, plot a spatial map, and extract a time series of air temperature
[Fargate Dask Cluster](examples/dask) | AWS Fargate, Amazon SageMaker Notebooks | CMIP6, ERA5, GOES-16 | Example of how to set up a Dask cluster and Jupyter notebook for scalable analysis of datasets
[GFS to Parquet Conversion](examples/noaa-gfs-parquet) | Amazon SageMaker Notebooks, Amazon Athena, AWS Glue | GFS | Example of how to subset GFS grib2 files by variable, and convert them to the parquet file format for querying
[GHCN Growing Degree Days](examples/noaa-ghcn-gdd) | Amazon Athena, AWS Glue | GHCN | Example of how to query the NOAA GHCN data using Amazon Athena to return the number of growing degree days
[ISD Example](examples/noaa-isd) | Amazon SageMaker Notebooks, Amazon Athena, AWS Glue | ISD | An example of how to work with the NOAA Integrated Surface Database using Jupyter notebooks
[Julia GOES-16](examples/goes16-precip-julia) | Amazon EC2 | GOES-16 | An example showing multi-cpu computation against the GOES-16 precipitation files using Julia
[OpenAQ Example](examples/openaq) | Amazon Athena, AWS Glue | OpenAQ | Creates AWS Glue tables for easily querying the OpenAQ data in Amazon Athena

## Contributing to ASDI

There are two main ways to contribute to the ASDI Program:

1. If you have sustainability-related data you would like to share with the Amazon Sustainability Data Initiative (ASDI), please refer to the [contribution guidelines](https://github.com/awslabs/open-data-registry/blob/master/CONTRIBUTING.md) on the Registry of Open Data GitHub repository, or contact us at [sustainability-data-initiative@amazon.com](mailto:sustainability-data-initiative@amazon.com). You may be able to offset the storage and egress costs of your data by submitting an application to the [AWS Open data Program](https://aws.amazon.com/opendata/open-data-sponsorship-program/). Check [here](https://opendata.aws/guide) for guidance on how to optimally share data in the AWS cloud. Data providers are responsible for maintaining and supporting the data that they share.

2. If you have tutorials, open code, or publications that exemplify how existing ASDI datasets can be used for sustainability related work, you can add them directly to the Registry of Open Data on AWS by clicking the link at the bottom of a dataset page named &#39;Edit this dataset entry on GitHub.&#39; For example see the link at the bottom of [this dataset](https://registry.opendata.aws/sentinel-2/).

## ASDI data for supporting research

### AWS Cloud Credits

If you would like to test a cloud-based idea for sustainability, consider requesting a cloud grant to offset the costs of experimentation. The [AWS Promotional Credit Program managed by the Amazon Sustainability Data Initiative](https://amazonsdi.com/credits) awards grants of AWS credits to support those interested in prototyping new sustainability related solutions on AWS, or transfer existing workflows from on-premise to the cloud.

### AWS Research Cloud Program

The [AWS Research Cloud Program](https://aws.amazon.com/government-education/research-and-technical-computing/research-cloud-program/) was built by scientists at AWS to enable easy use of AWS resources by their fellow researchers in the scientific community around the globe. By signing up you can receive a free copy of the AWS Researcher&#39;s Handbook, a comprehensive guide to doing research on AWS.

_For more information about the Amazon Sustainability Data Initiative, visit www.AmazonSDI.com._

## ⚠️ License

This project is licensed under the [Apache License 2.0](https://github.com/awslabs/amazon-asdi/blob/master/LICENSE).

