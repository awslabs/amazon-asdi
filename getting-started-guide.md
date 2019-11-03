# Getting Started with the Amazon Sustainability Data Initiative (ASDI)

* [Getting Started With the Amazon Sustainability Data Initiative (ASDI)](#getting-started)

* [AWS Basics](#aws-basics)
  
  * [Setting up an AWS account](#setting-up-an-aws-account)
  * [AWS Storage](#aws-storage)
  * [AWS Compute](#aws-compute)
  * [AWS Notifications](#aws-notifications)
  

* [Working with ASDI Data](#working-with-asdi-data)

  * [Available datasets](#available-datasets)
  * [Accessing datasets](#accessing-datasets)
  * [Querying and analyzing data](#querying-and-analyzing-data)
  * [AWS compute options](#aws-compute-options)
  * [SDK & CLI access](#sdk--cli-access)
  
* [Additional Resources](#additional-resources)


## Getting Started

The [Amazon Sustainability Data Initiative](https://www.aboutamazon.com/sustainability/amazon-sustainability-data-initiative) (ASDI) provides a collection of freely available datasets for use by researchers, developers and innovators working in sustainability. This guide provides an overview of how to get started with ASDI: what kinds of data are available, examples of ways to work with data in the cloud, and an overview of some of the resources and libraries well-suited for ASDI data.

## AWS Basics

ASDI data is hosted on the Amazon Web Services (AWS) Cloud.  You can find a general overview of cloud computing [here](https://aws.amazon.com/what-is-cloud-computing/).

An advantage of storing data in the cloud is that it makes it virtually accessible from anywhere in the world. Another is the ability of anyone to leverage the scalable infrastructure and run analysis and computing on-demand, in close proximity to where the data is stored. AWS offers a wide range of both storage and compute services; this guide will focus on those most relevant to working with ASDI data.

### Setting up an AWS account

To work with the ASDI data in the cloud and leverage AWS services, you need to create an AWS account, which you can learn how to do [here](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/). If you&#39;re new to AWS or want to make sure your account is set up correctly, please see this [guide to AWS account best practices](https://aws.amazon.com/blogs/startups/how-to-get-started-on-aws-from-a-dead-standstill/).

### AWS Storage

ASDI data is stored on [Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/). S3 is an object storage service that can store any volume of data, of any type, and which allows data to be made public or private, at the owner&#39;s discretion. S3 data is stored in _buckets_ and a _bucket_ can hold anything from a single zero byte file to billions of objects and petabytes of data.

You can view S3 documentation [here](https://docs.aws.amazon.com/s3/index.html), and a 10-minute &#39;getting started with S3&#39; tutorial [here](https://aws.amazon.com/getting-started/tutorials/backup-files-to-amazon-s3/).

AWS also offers traditional relational databases via the [Amazon Relational Database Service (RDS)](https://aws.amazon.com/rds/), NoSQL databases like [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon DocumentDB (MongoDB compatible)](https://aws.amazon.com/documentdb/), and file system storage through the [Amazon Elastic File System](https://aws.amazon.com/efs/) service and [Lustre compatible](https://aws.amazon.com/fsx/lustre/) filesytems.

This guide will cover the basics of interacting with S3, with a focus on ASDI data. Follow these links for more information on the full range of [AWS storage](https://aws.amazon.com/products/storage/) and [AWS database](https://aws.amazon.com/products/databases/) offerings.

### AWS Compute

AWS offers a number of compute options, including Linux or Windows server instances, container-based services, and event-driven computing. See AWS compute options in the following section for more details on using AWS compute services with ASDI data, or click [here](https://aws.amazon.com/products/compute/) for a full overview of all AWS compute services.

### AWS Notifications

[Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) is a managed notification service, using a [pub/sub model](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern), which some ASDI dataset managers use to notify subscribers of updates to their datasets. Details are listed in the &#39;Resources on AWS&#39; section of dataset pages that support notifications. See the [GOES datase](https://registry.opendata.aws/noaa-goes/)[t](https://registry.opendata.aws/noaa-goes/) for an example.

## Working with ASDI Data

Each ASDI dataset is stored in its own S3 bucket, which is managed by a Data Provider (e.g., NOAA, NASA, UK Met Office). Most ASDI data is available without commercial restriction--license details are available with each dataset. There may be costs associated with querying ASDI data, or running compute resources on AWS to take advantage of it. There is an [AWS free tier](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-limits.html) that covers some limited usage. You can also apply for a [cloud grant](https://aws.amazon.com/earth/research-credits/) to offset the costs of experimentation.

### Available datasets

ASDI datasets are hosted through the [AWS Public Dataset Program](https://aws.amazon.com/opendata/public-datasets/), which covers the storage and egress costs for publicly available, high-value datasets. The data can be discoverable through the [Registry of Open Data on AWS](https://registry.opendata.aws/), and are tagged for [sustainability](https://registry.opendata.aws/tag/sustainability/). You can also explore a list of those datasets [here](https://sustainability.aboutamazon.com/tech-for-good/asdi-data-catalog-overview).

### Accessing datasets

To access the data, you can either use the [AWS Command Line Interface](https://aws.amazon.com/cli/)or use HTTP. See an example below for the [NOAA&#39;s National Water Model](https://registry.opendata.aws/noaa-nwm-pds/) dataset.

AWS Command Line Interface

aws s3 ls s3://noaa-nwm-pds/

aws s3 cp s3://noaa-nwm-pds/nwm.20190923/short\_range/nwm.t19z.short\_range.terrain\_rt.f01

8.conus.nc .

Via HTTP

http:// noaa-nwm-pds.s3.amazonaws.com/ nwm.20190923/short\_range/nwm.t19z.short\_range

.terrain\_rt.f018.conus.nc

### Querying and analyzing data

In general, there are three options for working with ASDI data: query or process it in place, transfer it to your own AWS account, or download it.

Depending on their content and structure, some datasets can be queried directly without having to be transferred or downloaded. This can be done using [AWS Athena](https://aws.amazon.com/athena/), which lets you define a schema for existing data residing in flat files, and then query it using standard SQL. For an in-depth example using ASDI data, please see this blog post [Visualize over 200 years of global climate data using Amazon Athena and Amazon QuickSight](https://aws.amazon.com/blogs/big-data/visualize-over-200-years-of-global-climate-data-using-amazon-athena-and-amazon-quicksight/) or [Querying OpenStreetMap with Amazon Athena](https://aws.amazon.com/blogs/big-data/querying-openstreetmap-with-amazon-athena/).

Data can also be copied into your own AWS account and then be queried, analyzed or transformed however you choose. You can transfer data from S3 using AWS SDKs or the CLI, details of which can be found below. You can see examples of using the AWS Python SDK to work with S3 [here](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html). Note that transferring data to your own bucket may lead to storage and egress fees so we encourage you, as much as possible, to run your analysis on the data hosted in the Public Dataset _buckets_.

There are a number of options available if you want to transform ASDI into a format better suited for your purposes, including [AWS Glue](https://aws.amazon.com/glue/), an ETL service, [Apache Spark](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark.html), and Amazon Kinesis, a streaming service that can [transform JSON](https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html) into Apache [Parquet](https://parquet.apache.org/) or [ORC](https://orc.apache.org/), tabular data formats that provide more efficient querying. Learn more about using tabular formats with Athena [here](https://docs.aws.amazon.com/athena/latest/ug/columnar-storage.html). Tabular data may not be the ideal structure if you are looking to analyze geospatial data. Instead, [Cloud-Optimized Geotiff](https://www.cogeo.org/) (COG) is a good format to explore (see [Landsat data on AWS](https://registry.opendata.aws/landsat-8/)).

### AWS compute options

Although you can download ASDI data for use on-premises, this pattern leads to duplication of storage, incurs data transfer latency and can make it difficult to discern data provenance. By doing computation on AWS, close to where ASDI data resides, you can reduce latency and increase access speeds, more easily work with large volumes of data, and allow collaborators access to your work. It also makes available to you an array of cloud services well-suited for [research and scientific computing](https://aws.amazon.com/government-education/research-and-technical-computing/). See the AWS documentation for a [full overview of all AWS compute modalities](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html). Below is a brief summary of some of those most relevant to analyzing ASDI data for sustainability applications.

#### Amazon EC2

[Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/) allows you to create Linux or Windows-based server instances on AWS, which you can configure to meet your needs. [Add an example of how this is being used by a sustainability application -- sustainability tutorials??]

#### Amazon ECS

Docker containers allow you to package code and dependent libraries in a convenient, self-contained unit. Containers run on top of host operating systems, are lighter weight than full instances, and are designed to be easily portable between different compute environments. For instance, a container running on a laptop should be able to run without modification in the cloud. Containers can be used to run most workloads--data analysis, web applications, GIS servers, etc--that a traditional cloud instance might be used for.

There are a number of ways to manage container-based workloads on AWS including:

- --[AWS Batch](https://aws.amazon.com/batch/) which enables developers, scientists, and engineers to easily and efficiently run hundreds of thousands of batch computing jobs on AWS.
- --[AWS Fargate](https://aws.amazon.com/fargate/) which is a compute engine for Amazon ECS that allows you to run containers without having to manage servers or clusters.
- --[Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (Amazon ECS) which is a highly scalable, high-performance container orchestration service that supports Docker containers and allows you to easily run and scale containerized applications on AWS.
- --[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) which makes it easy to deploy, manage, and scale containerized applications using Kubernetes on AWS.

#### AWS Lambda

AWS Lambda is an event-driven service in which functions are triggered in response to things like HTTP calls or notifications from other services, for instance when a file is uploaded to S3. To create a Lambda function you upload the function code, configure the event it&#39;s tied to, and AWS manages the underlying infrastructure involved--you have no need to provision servers or containers. Lambdas are typically single-purpose functions, and need to be able to run in a limited timeframe and memory footprint: a maximum of 15 minutes and 3GB, respectively (longer running processes are more appropriate for containers or running directly on EC2). A group of Lambda functions can interoperate to form an application, and they are well-suited to [microservice architectures](https://en.wikipedia.org/wiki/Microservices).

### SDK &amp; CLI access

Software Development Kits, or SDKs, are code libraries specific to a programming language, which package functionality related to a specific software package, framework, platform, or service. For example there are SDKs to help developers to build [ArcGIS applications using Java](https://developers.arcgis.com/java/latest/), or to access [NOAA data using Python](https://pypi.org/project/noaa-sdk/).

AWS has [official SDKs](https://aws.amazon.com/tools/) for many popular languages, which make it easier to work with AWS services from within applications or programs written in those languages. There are also community-created SDKs and libraries are available for some languages not officially supported.

#### Python

There is an officially supported [AWS SDK](https://aws.amazon.com/sdk-for-python/), and the [numpy library](https://numpy.org/) supports many scientific and mathematical tasks.

#### C

C99 is supported by an open-source AWS project on Github, [awslabs/aws-c-common](https://github.com/awslabs/aws-c-common). Note there is an [official SDK for C++](https://aws.amazon.com/tools/).

#### Other AWS-supported languages

Official SDKs are available for Python, JavaScript, Node.js, C++, Go, Ruby, .NET, and PHP. See the AWS [SDKs and Programming Toolkits](https://aws.amazon.com/tools/) page for details.

#### Matlab

Matlab natively supports [reading and writing data to and from S3](https://www.mathworks.com/help/matlab/import_export/work-with-remote-data.html#bvn_hcu-2).

#### R

The community-run [cloudyr project](http://cloudyr.github.io/) has packages supporting many AWS storage and compute services, including S3.

#### CLI

You can also call AWS APIs using the [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/). This library, available for Linux, Mac, and Windows, lets you control AWS services from the command line, and automate them through scripts. If you&#39;re operating in an environment, for instance Fortran, for which there is no SDK, you can invoke the CLI from your programs, or write wrappers around them to do so.

### Additional resources

This guide covers a selection of services likely to be used with ASDI data. There are a great many other learning resources available. Good places to start include

* [AWS 10-minute tutorials](https://aws.amazon.com/getting-started/tutorials/)
* [AWS Getting Started Resource Center](https://aws.amazon.com/getting-started/)
* [AWS Researcher's Handbook](https://aws.amazon.com/government-education/research-and-technical-computing/research-cloud-program/#join)


