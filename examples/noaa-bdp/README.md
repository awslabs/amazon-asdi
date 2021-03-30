# Working with NOAA Model Data from the AWS Open Data Program

As part of the [NOAA Big Data Program](https://www.noaa.gov/organization/information-technology/big-data-program), there are currently 30 datasets from NOAA available on AWS. These datasets span weather, climate, and oceans. 

The data are in [Amazon S3](https://aws.amazon.com/s3/) buckets, generally with one bucket per model. The data are in their original format and file structure when possible. Cloud optimized versions of some models are also available.

You access data in S3 buckets using HTTPS and tools like wget or curl. You can also use the [AWS CLI](https://aws.amazon.com/cli/) to access the data. No AWS account is necessary to access the data. 

We list detailed examples for models listed here

* [GFS](#global-forecast-system-gfs)
* [GEFS](#global-ensemble-forecast-system-gefs)
* [HRRR](#high-resolution-rapid-refresh-hrrr)
* [RAP](#rapid-refresh-model-rap)
* [NBM](#national-blend-of-models-nbm)
* [NWM](#national-water-model-nwm)

For other models and datasets including NEXRAD, NDFD, and NAM check out their respective pages on the [Registry of Open Data on AWS.](https://registry.opendata.aws)

## Push Notifications for New Data

Datasets made available on AWS often have associated [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) topics available for receiving new object notifications. These are push notifications for when a new file (i.e. new GFS forecast hour) is available on S3\. You can use these notifications to kick off automated processing pipelines for working with the data instead of polling for data availability. 

There is an example of converting GOES-16 & GOES-17 ABI images to cloud optimized geotiffs with Lambda upon new object notification at 

Here is an example of how to receive the new object notification into the [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) where it can be used for further processing. 

## Global Forecast System (GFS)

If you are downloading the data from

```

https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/gfs.<date>/<hour>/<file>

```

You can download it from AWS at

```

https://noaa-gfs-bdp-pds.s3.amazonaws.com/gfs.<date>/<hour>/<file>

```

or explore all the files in the bucket at [https://noaa-gfs-bdp-pds.s3.amazonaws.com/index.html](https://noaa-gfs-bdp-pds.s3.amazonaws.com/index.html)

Data from the last 30 days are available on AWS for GFS.

Learn more about [GFS on the Registry of Open Data on AWS ](https://registry.opendata.aws/noaa-gfs-bdp-pds/)

## Global Ensemble Forecast System (GEFS)

If you are downloading data from

```

https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/prod/gefs.<date>/<hour>/<file>

```

You can download it from AWS at

```

https://noaa-gefs-pds.s3.amazonaws.com/gefs.<date>/<hour>/<file>

```

or explore all the files in the bucket at [https://noaa-gefs-pds.s3.amazonaws.com/index.html](https://noaa-gefs-pds.s3.amazonaws.com/index.html)

Data from 2017-present are available on AWS for GEFS.

Learn more about [GEFS on the Registry of Open Data on AWS](https://registry.opendata.aws/noaa-gefs/)[ ](https://registry.opendata.aws/noaa-hrrr-pds/)

## High Resolution Rapid Refresh (HRRR)

If you are downloading data from

```

https://nomads.ncep.noaa.gov/pub/data/nccf/com/hrrr/prod/hrrr.<date>/<file>

```

You can download it from AWS at

```

https://noaa-hrrr-bdp-pds.s3.amazonaws.com/hrrr.<date>/<file>

```

or explore all the files in the bucket at [https://noaa-hrrr-bdp-pds.s3.amazonaws.com/index.html](https://noaa-hrrr-bdp-pds.s3.amazonaws.com/index.html)

Data from 2014-present are available on AWS for HRRR.

HRRR data are also available in cloud-optimized ZARR format. Browse the HRRR ZARR bucket at [https://hrrrzarr.s3.amazonaws.com/index.html](https://hrrrzarr.s3.amazonaws.com/index.html)

Learn more about [HRRR on the Registry of Open Data on AWS ](https://registry.opendata.aws/noaa-hrrr-pds/)

## Rapid Refresh Model (RAP)

If you are downloading data from

```

https://nomads.ncep.noaa.gov/pub/data/nccf/com/rap/prod/rap.<date>/<file>

```

You can download it from AWS at

```

https://noaa-rap-pds.s3.amazonaws.com/rap.<date>/<file>

```

or explore all the files in the bucket at [https://noaa-rap-pds.s3.amazonaws.com/index.html](https://noaa-rap-pds.s3.amazonaws.com/index.html)

Learn more about [RAP on the Registry of Open Data on AWS](https://registry.opendata.aws/noaa-rap/)[ ](https://registry.opendata.aws/noaa-hrrr-pds/)

## National Blend of Models (NBM)

If you are downloading data from

```

https://nomads.ncep.noaa.gov/pub/data/nccf/com/blend/prod/blend.<date>/<hour>/<file>

```

You can download it from AWS at

```

https://noaa-nbm-grib2-pds.s3.amazonaws.com/blend.<date>/<hour>/<file>

```

or explore all the files in the bucket at [https://noaa-nbm-grib2-pds.s3.amazonaws.com/index.html](https://noaa-nbm-grib2-pds.s3.amazonaws.com/index.html)

Data are available from 2020-05-18 to present. 

NBM data are also available in Cloud-Optimized Geotiff (COG) format. Browse the NBM COG  bucket at [https://noaa-nbm-pds.s3.amazonaws.com/index.html](https://noaa-nbm-pds.s3.amazonaws.com/index.html)

Learn more about [NBM on the Registry of Open Data on AWS](https://registry.opendata.aws/noaa-nbm/)[ ](https://registry.opendata.aws/noaa-hrrr-pds/)

## National Water Model (NWM)

If you are downloading data from

```

https://nomads.ncep.noaa.gov/pub/data/nccf/com/nwm/prod/nwm.<date>/<file>

```

You can download it from AWS at

```

https://noaa-nwm-pds.s3.amazonaws.com/nwm.<date>/<file>

```

or explore all the files in the bucket at [https://noaa-nwm-pds.s3.amazonaws.com/index.html](https://noaa-nwm-pds.s3.amazonaws.com/index.html)

Data from the last 30 days are available on AWS for NWM.

Learn more about [NWM on the Registry of Open Data on AWS ](https://registry.opendata.aws/noaa-nwm-pds/)
