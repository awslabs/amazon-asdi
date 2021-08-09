# Working with NOAA GFS Grib Data

This notebook and Dockerfile provide a means to quickly get started working with the NOAA Global Forecast System (GFS) dataset which provides weather forecasts for 2+ weeks. The GFS data is part of the [AWS Public Dataset program](http://opendata.aws/) and more details on the data itself can be found at [GFS on the Registry of Open Data](https://registry.opendata.aws/noaa-gfs-bdp-pds/).

This notebook shows how to query the data with AWS Athena, and perform simple plotting functions to start visualizing the data.

## Build Docker

```
docker build -t gfs .
```

## Run Jupyter Notebook

```
docker run --rm -p 8888:8888 -v $(pwd)/notebook:/home/jovyan -ti gfs
```

## SSH Tunneling to your EC2 instance

```
ssh -N -L 8888:127.0.0.1:8888 ec2-user@<yourec2ip>
```
